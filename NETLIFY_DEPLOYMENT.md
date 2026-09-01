# Netlify Deployment Guide

This guide will help you deploy the Student Management API to Netlify.

## Prerequisites

- Netlify account (create one at https://netlify.com)
- Git repository (GitHub, GitLab, or Bitbucket)
- Your project pushed to a Git provider

## Deployment Steps

### 1. Connect Your Repository to Netlify

1. Visit [Netlify](https://app.netlify.com)
2. Click **Add new site** → **Import an existing project**
3. Select your Git provider (GitHub, GitLab, Bitbucket)
4. Authorize Netlify to access your repositories
5. Select this repository

### 2. Configure Build Settings

The following settings should be auto-detected from `netlify.toml`:

- **Base directory**: (leave empty or use root)
- **Build command**: `pip install -r requirements.txt`
- **Publish directory**: `public`
- **Functions directory**: `netlify/functions`
- **Python version**: `3.12` (set in Build environment variables)

### 3. Deploy

1. Click **Deploy site**
2. Wait for the build to complete
3. Your API will be available at `https://your-site-name.netlify.app`

## API Endpoints

After deployment, your API endpoints will be available at:

- `GET /students` - Get all students
- `GET /students/<student_id>` - Get a specific student
- `POST /students` - Add a new student
- `GET /test` - Health check endpoint

### Example Requests

```bash
# Get all students
curl https://your-site-name.netlify.app/students

# Add a new student
curl -X POST https://your-site-name.netlify.app/students \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "age": 20,
    "marks": 85,
    "course": "Computer Science"
  }'

# Get a specific student
curl https://your-site-name.netlify.app/students/<student_id>

# Test endpoint
curl https://your-site-name.netlify.app/test
```

## Environment Variables

If you need to add environment variables:

1. Go to **Site settings** → **Build & deploy** → **Environment**
2. Click **Edit variables**
3. Add your variables
4. Redeploy your site

## Troubleshooting

### Build Fails with Module Import Errors

Make sure all dependencies are in `requirements.txt`. Check that the build log shows `pip install` completing successfully.

### 404 Errors on API Routes

Ensure the `netlify.toml` redirects are correctly configured. Routes like `/students`, `/students/<id>`, and `/test` should redirect to the serverless function.

### Cold Start Issues

Netlify Functions may have cold start delays (a few seconds). This is normal for serverless deployments.

### Local Testing

To test locally before deploying:

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Run locally
netlify dev
```

This will start a local server at `http://localhost:8888` with the same routing as production.

## Project Structure

```
.
├── netlify/
│   ├── functions/
│   │   └── api.py          # Serverless function handler
│   └── requirements.txt     # Function-specific dependencies
├── src/
│   └── api_test/
│       ├── main.py         # Flask application
│       ├── Student.py      # Student model
│       ├── StudentManager.py # Business logic
│       └── MOCK_DATA.json   # Sample data
├── public/                  # Static files (if needed)
├── netlify.toml            # Netlify configuration
├── runtime.txt             # Python version
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project metadata
└── README.md               # Project documentation
```

## Additional Resources

- [Netlify Python Functions](https://docs.netlify.com/functions/overview/)
- [aws-lambda-wsgi Documentation](https://github.com/adamchainz/aws-lambda-wsgi)
- [Flask Documentation](https://flask.palletsprojects.com/)
