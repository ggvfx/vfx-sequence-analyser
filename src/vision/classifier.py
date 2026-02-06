"""
Source Media Classifier.

Identifies if the incoming video stream consists of live-action 'Plates', 
'Previs' (CGI), 'Storyboards', or 'Animatics'.
"""

class SourceClassifier:
    """Analyzes visual style to categorize media type."""

    def classify_sequence(self, thumbnail_paths: List[str]) -> str:
        """Returns the predominant source type for the sequence."""
        pass