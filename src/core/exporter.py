"""
VFX Export Engine.

Handles the serialization of ShotBreakdown data into professional formats.
Primary focus is XlsxWriter for Excel sheets with embedded thumbnails.
"""

from typing import List
from src.core.models import ShotBreakdown

class VFXExporter:
    """Serializes session data into Excel, CSV, or Studio-specific JSON."""

    def to_excel(self, shots: List[ShotBreakdown], export_path: str):
        """Generates a bidding-ready Excel sheet with images."""
        pass

    def to_csv(self, shots: List[ShotBreakdown], export_path: str):
        """Standard CSV export for database ingestion."""
        pass