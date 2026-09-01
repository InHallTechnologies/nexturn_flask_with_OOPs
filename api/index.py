import sys
import os

# Add `src` directory to system path so `api_test` package can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from api_test import app
