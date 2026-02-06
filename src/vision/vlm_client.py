"""
Vision-Language Model (VLM) Client.

Interface for local models like Florence-2 or Moondream2. 
Handles 'The Eyes' of the tool: Captioning, OCR, and Object Detection.
"""

from typing import List, Dict
from src.core.models import VisualElement

# --- MODEL INTERFACE ---

class VisionClient:
    """Manages local VLM inference for visual analysis."""

    def __init__(self, model_name: str = "florence-2"):
        self.model_name = model_name

    def get_shot_caption(self, image_path: str) -> str:
        """Generates a raw natural language description of the frame."""
        pass

    def detect_vfx_elements(self, image_path: str) -> List[VisualElement]:
        """Scans for Greenscreens, Tracking Markers, and Props."""
        pass

    def perform_ocr(self, image_path: str) -> Dict[str, str]:
        """Reads Plate burn-ins for Shot Names and Timecodes."""
        pass