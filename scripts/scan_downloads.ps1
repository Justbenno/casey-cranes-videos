<#
.SYNOPSIS
  Read-only scan of Windows Downloads folder for tax evidence intake.

.DESCRIPTION
  Exports a manifest CSV with file metadata and SHA256 hashes.
  Does not move, rename, or modify source files.
#>

param(
  [Parameter(Mandatory = $false)]
  [string]$SourcePath = "$env:USERPROFILE\Downloads",

  [Parameter(Mandatory = $false)]
  [string]$OutputPath = ".\logs\downloads_scan_manifest.csv",

  [Parameter(Mandatory = $false)]
  [string]$OperationsLog = ".\logs\operations_log.csv",

  [Parameter(Mandatory = $false)]
  [string]$Operator = "unknown-operator"
)

if (-not (Test-Path -LiteralPath $SourcePath)) {
  Write-Error "Source directory not found: $SourcePath"
  exit 1
}

$files = Get-ChildItem -LiteralPath $SourcePath -File -Recurse | Sort-Object FullName

$outputDir = Split-Path -Parent $OutputPath
if ($outputDir -and -not (Test-Path -LiteralPath $outputDir)) {
  New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

$rows = foreach ($file in $files) {
  $hash = Get-FileHash -Algorithm SHA256 -LiteralPath $file.FullName
  [pscustomobject]@{
    source_path       = $file.FullName
    file_name         = $file.Name
    file_extension    = $file.Extension.ToLowerInvariant()
    file_size_bytes   = $file.Length
    modified_time_utc = $file.LastWriteTimeUtc.ToString("o")
    sha256            = $hash.Hash.ToLowerInvariant()
  }
}

$rows | Export-Csv -Path $OutputPath -NoTypeInformation -Encoding UTF8

Write-Host "Scanned $($rows.Count) file(s)"
Write-Host "Manifest written to: $OutputPath"
Write-Host "Operator: $Operator"

# Append operation-log entry for chain-of-custody parity with scan_drive.py
$logDir = Split-Path -Parent $OperationsLog
if ($logDir -and -not (Test-Path -LiteralPath $logDir)) {
  New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

$needsHeader = -not (Test-Path -LiteralPath $OperationsLog) -or (Get-Item -LiteralPath $OperationsLog).Length -eq 0
$timestampUtc = (Get-Date).ToUniversalTime().ToString("o")
$logRow = [pscustomobject]@{
  timestamp_utc        = $timestampUtc
  action               = "scan"
  source_location      = (Resolve-Path -LiteralPath $SourcePath).Path
  destination_location = [System.IO.Path]::GetFullPath($OutputPath)
  file_count           = $rows.Count
  operator             = $Operator
  status               = "success"
  notes                = "Read-only scan completed"
}

if ($needsHeader) {
  $logRow | Export-Csv -Path $OperationsLog -NoTypeInformation -Encoding UTF8
} else {
  $logRow | Export-Csv -Path $OperationsLog -NoTypeInformation -Encoding UTF8 -Append
}
