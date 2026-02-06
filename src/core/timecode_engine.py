"""
SMPTE Timecode Engine.

Provides frame-accurate timecode math. This module avoids floating-point 
drift by using integer-based frame calculations for all VFX 'In' and 'Out' points.
"""

class TimecodeHandler:
    """Handles conversions between frame counts and SMPTE timecode strings."""
    
    def __init__(self, fps: float = 23.976):
        self.fps = fps

    def frames_to_tc(self, frames: int) -> str:
        """Converts an integer frame count to HH:MM:SS:FF."""
        pass

    def tc_to_frames(self, tc_string: str) -> int:
        """Converts an HH:MM:SS:FF string back to an integer frame count."""
        pass