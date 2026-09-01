import sys
import os
from pathlib import Path

# Add the src directory to Python path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

try:
    from api_test.main import app
    from mangum import Mangum
    
    # Create the handler
    handler = Mangum(app, lifespan="off")
except Exception as e:
    # Return error response if imports fail
    def handler(event, context):
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
