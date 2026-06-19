# Tax Operations Workspace Instructions

Use `prompts/TAX-MSTR-SYSTEM-001.md` as the governing system instruction for tax evidence operations in this workspace.

## Operating Defaults

- Run in READ-ONLY + REVIEW-FIRST mode unless explicit approval is provided.
- Never modify source evidence files; work on controlled copies only.
- Never invent facts; use: "Not located", "Requires confirmation", or "Unable to verify" when evidence is missing.
- Log all significant actions into `logs/operations_log.csv`.
- Use the default response format:
  1. Objective
  2. Risks
  3. Proposed Action
  4. Expected Outcome
  5. Approval Requirement
  6. Status

## Scope Control

Allowed baseline automation scope for first phase:

SCAN → CLASSIFY → REGISTER

Do not perform autonomous submissions, deletions, cloud sync, or outbound email actions.
