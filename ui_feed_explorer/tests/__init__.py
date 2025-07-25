"""
Test suite for the LinkedIn Feed Explorer UI.
"""

import sys
from pathlib import Path

# Add the ui_feed_explorer module to the path for testing
ui_path = Path(__file__).parent.parent
if str(ui_path) not in sys.path:
    sys.path.insert(0, str(ui_path))
