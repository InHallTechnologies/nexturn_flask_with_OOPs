import sys
import os
from pathlib import Path

# Add the src directory to Python path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from api_test.main import app
from aws_lambda_wsgi import response

def handler(event, context):
    """
    Netlify Functions handler that wraps the Flask app.
    Converts Lambda events/context to WSGI format and back.
    """
    return response(app, event, context)
