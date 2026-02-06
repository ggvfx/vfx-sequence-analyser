"""
Ollama Intelligence Client.

Synthesizes raw visual data into professional VFX-speak descriptions.
Uses Llama 3.2 to ensure output matches industry-standard terminology.
"""

from typing import List
from src.core.models import VisualElement

# --- INTELLIGENCE LOGIC ---

class OllamaClient:
    """The 'Brain' that formats metadata into human-readable bidding notes."""

    def __init__(self, model: str = "llama3.2"):
        self.model = model

    async def generate_vfx_description(self, framing: str, elements: List[VisualElement]) -> str:
        """
        Takes technical tags and converts them to a professional sentence.
        
        Example: (MS + John Doe + Spanner) -> 'MS on John Doe as he manipulates Spanner.'
        """
        pass

    def validate_json_response(self, raw_text: str) -> dict:
        """Ensures Ollama returns a valid minified JSON object."""
        pass