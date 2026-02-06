"""
VFX Feature Detector.

Specific computer vision logic to scan frames for technical VFX elements 
like Greenscreens, Blue-screens, and Tracking Markers.
"""

from src.core.models import VisualElement

class VFXFeatureDetector:
    """Scans frames for technical elements requiring specific VFX work."""

    def scan_for_greenscreen(self, image_path: str) -> VisualElement:
        """Detects green/blue screen area and returns confidence."""
        pass

    def find_tracking_markers(self, image_path: str) -> List[VisualElement]:
        """Locates 'X' or 'Square' tracking markers on set."""
        pass