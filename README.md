# Student Management API

A Flask-based REST API for managing student records. Easily deployable to Netlify as a serverless application.

## Features

- ✅ RESTful API for student management
- ✅ Add, retrieve, and list students
- ✅ Unique student IDs
- ✅ Serverless deployment ready
- ✅ CORS-enabled for frontend integration

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd api_test
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python src/api_test/main.py
   ```

4. **Test the API**
   ```bash
   curl http://localhost:8000/test
   ```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/students` | Add a new student |
| GET | `/students` | Get all students |
| GET | `/students/<id>` | Get a specific student |
| GET | `/test` | Health check |

### Request/Response Examples

**Add Student:**
```bash
curl -X POST http://localhost:8000/students \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "age": 20,
    "marks": 92,
    "course": "Computer Science"
  }'
```

**Get All Students:**
```bash
curl http://localhost:8000/students
```

**Get Student by ID:**
```bash
curl http://localhost:8000/students/<student_id>
```

## Deployment

### Deploy to Netlify

See [NETLIFY_DEPLOYMENT.md](./NETLIFY_DEPLOYMENT.md) for complete deployment instructions.

Quick deploy:
1. Push code to GitHub, GitLab, or Bitbucket
2. Connect repository to Netlify
3. Netlify will automatically build and deploy using `netlify.toml`

## Project Structure

```
api_test/
├── src/
│   └── api_test/
│       ├── main.py              # Flask app and routes
│       ├── Student.py           # Student model
│       ├── StudentManager.py     # Student management logic
│       └── MOCK_DATA.json        # Sample data
├── netlify/
│   ├── functions/
│   │   └── api.py              # Serverless function handler
│   └── requirements.txt          # Function dependencies
├── public/                       # Static files (if needed)
├── netlify.toml                 # Netlify configuration
├── runtime.txt                  # Python version specification
├── requirements.txt             # Python dependencies
└── pyproject.toml              # Project metadata
```

## Technologies

- **Backend**: Flask 3.1.3
- **Python**: 3.12
- **Deployment**: Netlify (Serverless Functions)
- **Package Manager**: uv

## Dependencies

- Flask 3.1.3
- requests 2.34.2
- currencyconverter 0.18.21
- aws-lambda-wsgi 2.0.3 (for serverless deployment)

## Development

### Install Development Dependencies

```bash
pip install -r requirements.txt
```

### Add New Dependencies

```bash
pip install <package-name>
pip freeze > requirements.txt
```

Or using uv:
```bash
uv pip install <package-name>
uv export --format requirements-txt > requirements.txt
```

## License

MIT

## Author

Rishabh Verma
