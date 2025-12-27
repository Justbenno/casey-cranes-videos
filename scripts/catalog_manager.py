#!/usr/bin/env python3
"""
Casey Crane Hire Video Catalog Management Tool

This script provides utilities to manage the video catalog efficiently:
- List all videos
- Validate metadata against schema
- Generate statistics and reports
- Check for missing information
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime
import argparse

# Configuration constants
METADATA_DIR = "metadata"
SCHEMA_FILE = "schemas/video-metadata-schema.json"
VIDEO_ID_PREFIX = "CCH-"
VIDEO_ID_PATTERN = r"^CCH-\d{3,}$"


class VideoCatalog:
    """Video catalog management class"""
    
    def __init__(self, base_path: str = ".", metadata_dir: str = None, schema_file: str = None):
        self.base_path = Path(base_path)
        self.metadata_dir = self.base_path / (metadata_dir or METADATA_DIR)
        self.schema_path = self.base_path / (schema_file or SCHEMA_FILE)
        
    def load_schema(self) -> Dict[str, Any]:
        """Load the JSON schema"""
        if not self.schema_path.exists():
            print(f"Warning: Schema not found at {self.schema_path}")
            return {}
        
        with open(self.schema_path, 'r') as f:
            return json.load(f)
    
    def list_videos(self) -> List[Dict[str, Any]]:
        """List all videos in the catalog"""
        videos = []
        
        if not self.metadata_dir.exists():
            return videos
        
        pattern = f"{VIDEO_ID_PREFIX}*.json"
        for json_file in sorted(self.metadata_dir.glob(pattern)):
            try:
                with open(json_file, 'r') as f:
                    video = json.load(f)
                    videos.append(video)
            except json.JSONDecodeError as e:
                print(f"Error loading {json_file}: {e}")
        
        return videos
    
    def validate_video(self, video: Dict[str, Any]) -> List[str]:
        """Validate a video against required fields and return list of issues"""
        issues = []
        
        # Check required fields
        required_fields = ["id", "title", "dateRecorded", "status"]
        for field in required_fields:
            if field not in video or not video[field]:
                issues.append(f"Missing required field: {field}")
        
        # Check ID format
        if "id" in video:
            import re
            if not re.match(VIDEO_ID_PATTERN, video["id"]):
                issues.append(f"Invalid ID format: {video['id']} (should match {VIDEO_ID_PATTERN})")
        
        # Check status value
        valid_statuses = ["published", "cataloged", "archived", "in_production"]
        if "status" in video and video["status"] not in valid_statuses:
            issues.append(f"Invalid status: {video['status']}")
        
        return issues
    
    def get_statistics(self) -> Dict[str, Any]:
        """Generate statistics about the video catalog"""
        videos = self.list_videos()
        
        stats = {
            "total_videos": len(videos),
            "by_status": {},
            "by_type": {},
            "published_platforms": {},
            "incomplete_branding": 0,
            "missing_equipment": 0,
            "last_updated": datetime.now().isoformat()
        }
        
        for video in videos:
            # Status count
            status = video.get("status", "unknown")
            stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
            
            # Type count
            vtype = video.get("videoType", "unknown")
            stats["by_type"][vtype] = stats["by_type"].get(vtype, 0) + 1
            
            # Platform counts
            for platform in video.get("platforms", []):
                name = platform.get("name", "unknown")
                if platform.get("published", False):
                    stats["published_platforms"][name] = stats["published_platforms"].get(name, 0) + 1
            
            # Branding check
            branding = video.get("branding", {})
            if not all([
                branding.get("whiteBoomsVerified", False),
                branding.get("yellowHeadboardsVerified", False),
                branding.get("logoVisible", False),
                branding.get("qualityCheckCompleted", False)
            ]):
                stats["incomplete_branding"] += 1
            
            # Equipment check
            if not video.get("equipment"):
                stats["missing_equipment"] += 1
        
        return stats
    
    def generate_report(self) -> str:
        """Generate a human-readable report"""
        videos = self.list_videos()
        stats = self.get_statistics()
        
        report = ["# Casey Crane Hire Video Catalog Report", ""]
        report.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Total Videos**: {stats['total_videos']}")
        report.append("")
        
        # Status breakdown
        report.append("## Videos by Status")
        for status, count in sorted(stats['by_status'].items()):
            report.append(f"- **{status.title()}**: {count}")
        report.append("")
        
        # Type breakdown
        if stats['by_type']:
            report.append("## Videos by Type")
            for vtype, count in sorted(stats['by_type'].items()):
                report.append(f"- **{vtype.replace('_', ' ').title()}**: {count}")
            report.append("")
        
        # Platform stats
        if stats['published_platforms']:
            report.append("## Published Videos by Platform")
            for platform, count in sorted(stats['published_platforms'].items()):
                report.append(f"- **{platform.title()}**: {count}")
            report.append("")
        
        # Issues
        report.append("## Attention Required")
        report.append(f"- **Videos with incomplete branding**: {stats['incomplete_branding']}")
        report.append(f"- **Videos missing equipment info**: {stats['missing_equipment']}")
        report.append("")
        
        # Video list
        report.append("## All Videos")
        for video in videos:
            report.append(f"### {video.get('id', 'Unknown')} - {video.get('title', 'Untitled')}")
            report.append(f"- **Status**: {video.get('status', 'unknown')}")
            report.append(f"- **Type**: {video.get('videoType', 'unknown')}")
            report.append(f"- **Date Recorded**: {video.get('dateRecorded', 'unknown')}")
            
            # Validation
            issues = self.validate_video(video)
            if issues:
                report.append("- **Issues**:")
                for issue in issues:
                    report.append(f"  - {issue}")
            
            report.append("")
        
        return "\n".join(report)
    
    def check_completeness(self) -> None:
        """Check all videos for completeness and print results"""
        videos = self.list_videos()
        
        print(f"\n{'='*60}")
        print("Video Catalog Completeness Check")
        print(f"{'='*60}\n")
        
        if not videos:
            print("No videos found in catalog.")
            return
        
        total_issues = 0
        
        for video in videos:
            video_id = video.get("id", "Unknown")
            title = video.get("title", "Untitled")
            
            issues = self.validate_video(video)
            
            if issues:
                print(f"❌ {video_id} - {title}")
                for issue in issues:
                    print(f"   - {issue}")
                print()
                total_issues += len(issues)
            else:
                print(f"✅ {video_id} - {title}")
        
        print(f"\n{'='*60}")
        print(f"Total Videos: {len(videos)}")
        print(f"Total Issues: {total_issues}")
        print(f"{'='*60}\n")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Casey Crane Hire Video Catalog Management Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s list       List all videos in the catalog
  %(prog)s stats      Show statistics about the catalog
  %(prog)s report     Generate a full markdown report
  %(prog)s check      Check all videos for completeness
        """
    )
    
    parser.add_argument(
        "command",
        choices=["list", "stats", "report", "check"],
        help="Command to execute"
    )
    
    parser.add_argument(
        "--base-path",
        default=".",
        help="Base path to the repository (default: current directory)"
    )
    
    args = parser.parse_args()
    
    catalog = VideoCatalog(base_path=args.base_path)
    
    if args.command == "list":
        videos = catalog.list_videos()
        print(f"\nFound {len(videos)} video(s):\n")
        for video in videos:
            print(f"{video.get('id', 'Unknown')} - {video.get('title', 'Untitled')} [{video.get('status', 'unknown')}]")
    
    elif args.command == "stats":
        stats = catalog.get_statistics()
        print(json.dumps(stats, indent=2))
    
    elif args.command == "report":
        report = catalog.generate_report()
        print(report)
    
    elif args.command == "check":
        catalog.check_completeness()


if __name__ == "__main__":
    main()
