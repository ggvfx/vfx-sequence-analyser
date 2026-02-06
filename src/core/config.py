"""
Application Configuration and Session State.

This module manages the default settings and the active user session state
using Python dataclasses. It acts as the central hub for global parameters 
like model selection, handle counts, and directory paths.
"""

from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class AppConfig:
    """
    Global settings for the VFX Sequence Analyser.
    Initial values represent the 'Industry Defaults'.
    """
    # Editorial Defaults
    default_handles: int = 8
    frame_rate: float = 23.976
    timecode_start: str = "01:00:00:00"
    
    # AI & Vision Settings
    vlm_model: str = "florence-2"     # Options: florence-2, moondream2
    ollama_model: str = "llama3.2"    # The 'Brain' for description synthesis
    compute_device: str = "auto"      # cuda, cpu, or mps
    worker_threads: int = 4           # Controlled by 'Eco vs Power' UI toggle
    
    # Media Extraction
    thumbnail_size: int = 512         # Width in pixels
    extract_fades: bool = True        # Should scene detection look for dissolves?
    
    # Paths
    last_import_dir: Optional[str] = None
    export_dir: Optional[str] = None

    def to_dict(self):
        """Converts the config to a dictionary for JSON export."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        """Creates a config instance from a dictionary (JSON load)."""
        return cls(**data)


# --- SINGLETON INSTANCE ---
# This ensures every module accesses the SAME session data.
current_session = AppConfig()