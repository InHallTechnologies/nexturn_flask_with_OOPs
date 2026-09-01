import sys
import os
from pathlib import Path

# Add the src directory to Python path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

try:
    import serverless_wsgi
    from api_test.main import app

    def handler(event, context):
        # Strip Netlify function prefix if present in the event path
        if "path" in event and isinstance(event["path"], str):
            prefix = "/.netlify/functions/api"
            if event["path"].startswith(prefix):
                event["path"] = event["path"][len(prefix):] or "/"

        return serverless_wsgi.handle_request(app, event, context)
except Exception as e:
    # Return error response if imports fail
    def handler(event, context):
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }

