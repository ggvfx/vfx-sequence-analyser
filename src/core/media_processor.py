"""
Media Processor (FFmpeg Wrapper).

Handles technical media operations: frame extraction for thumbnails, 
generating proxy clips for the UI, and reading file-level metadata.
"""

import subprocess
from src.core.models import ShotMetadata

class MediaProcessor:
    """Interface for FFmpeg and OpenCV media operations."""

    def get_metadata(self, file_path: str) -> ShotMetadata:
        """Probes the video file for resolution, fps, and codec."""
        pass

    def extract_thumbnail(self, video_path: str, frame: int, output_path: str, width: int = 512):
        """Extracts and scales a single frame using FFmpeg."""
        pass