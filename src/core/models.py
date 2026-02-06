"""
Core Data Models for VFX Sequence Analyser.

This module defines the foundational schemas using Pydantic. 
These models act as the 'Source of Truth' for shot data, technical metadata, 
and AI-generated analysis, ensuring consistency across the UI and Export modules.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


# --- SUPPORTING MODELS ---

class ShotMetadata(BaseModel):
    """Technical details extracted from the file or burn-ins."""
    source_path: str
    codec: str
    resolution: str
    fps: float
    pixel_aspect: float = 1.0


class VisualElement(BaseModel):
    """Specific items identified within a shot (e.g., Greenscreen, Character)."""
    label: str = Field(..., description="The name of the element (e.g., 'Spanner')")
    confidence: float = 0.0
    bounding_box: Optional[List[float]] = None  # [ymin, xmin, ymax, xmax] normalized
    is_vfx_flag: bool = False  # True if it's a tracking marker, greenscreen, etc.


# --- CORE SHOT MODEL ---

class ShotBreakdown(BaseModel):
    """The primary data structure representing a single VFX Shot."""
    shot_id: str = Field(..., description="The name of the shot (e.g., 'SQ010_SH010')")
    
    # Timing (Using Integers to avoid float drift)
    frame_start: int
    frame_end: int
    handle_start: int = 0
    handle_end: int = 0
    
    # Timecode Strings (OCR or Calculated)
    tc_start: str = "00:00:00:00"
    tc_end: str = "00:00:00:00"
    
    # Classification
    source_type: str = "Plate"  # Plate, Previs, Storyboard, etc.
    framing: str = "MS"  # WS, MS, CU, ECU
    camera_movement: str = "Static"
    
    # Description synthesis
    ai_description: str = ""
    user_notes: Optional[str] = None
    
    # Identity and Elements
    elements: List[VisualElement] = []
    thumbnail_path: Optional[str] = None

    @property
    def duration_frames(self) -> int:
        """Calculates total frame count including handles."""
        return (self.frame_end - self.frame_start) + 1