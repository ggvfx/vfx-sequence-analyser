"""
VFX Sequence Analyser - Entry Point.

This module initializes the PySide6 application, loads the global configuration,
and orchestrates the connection between the UI, the Media Engine, and the AI logic.
"""

import sys
from PySide6.QtWidgets import QApplication
from src.ui.main_window import MainWindow
from src.core.config import current_session

def main():
    """
    Initializes the application and shows the primary UI.
    """
    app = QApplication(sys.argv)
    
    # TODO: Apply global QSS stylesheets here
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()