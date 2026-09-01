# Netlify Deployment Checklist

Use this checklist to prepare and deploy your Student Management API to Netlify.

## Pre-Deployment Checklist

### Code Preparation
- [ ] All code committed to Git
- [ ] No uncommitted changes
- [ ] Push all changes to main branch
- [ ] Verify all dependencies in `requirements.txt`
- [ ] Test locally: `python src/api_test/main.py`
- [ ] Verify API works: `curl http://localhost:8000/test`

### Configuration Files
- [ ] `netlify.toml` - Configured with correct build settings ✅
- [ ] `runtime.txt` - Python version set to 3.12 ✅
- [ ] `netlify/requirements.txt` - Contains aws-lambda-wsgi ✅
- [ ] `netlify/functions/api.py` - Handler created ✅
- [ ] `public/index.html` - Welcome page created ✅
- [ ] `.gitignore` - Updated with Netlify artifacts ✅

### Repository Setup
- [ ] Repository on GitHub, GitLab, or Bitbucket
- [ ] Repository is public (or you have access rights)
- [ ] Netlify can access your Git provider

## Deployment Steps

### Step 1: Create Netlify Account
- [ ] Visit https://app.netlify.com
- [ ] Sign up using Git provider (GitHub/GitLab/Bitbucket)

### Step 2: Connect Repository
- [ ] Click "Add new site" → "Import an existing project"
- [ ] Select your Git provider
- [ ] Authorize Netlify
- [ ] Select your `api_test` repository

### Step 3: Configure Build Settings
The following should be auto-detected from `netlify.toml`:

Build Settings:
- [ ] Base directory: (empty/root)
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Publish directory: `public`
- [ ] Functions directory: `netlify/functions`

Environment Variables:
- [ ] PYTHON_VERSION: `3.12`

### Step 4: Deploy
- [ ] Review settings
- [ ] Click "Deploy site"
- [ ] Wait for build to complete (2-5 minutes)
- [ ] Verify deployment succeeded

## Post-Deployment Verification

### Build Status
- [ ] No build errors in deploy log
- [ ] Deploy log shows "pip install" successful
- [ ] Deploy marked as "Published" (green)

### API Testing
- [ ] Visit `https://your-site-name.netlify.app` - See welcome page
- [ ] Test endpoint: `https://your-site-name.netlify.app/test`
- [ ] Test GET: `https://your-site-name.netlify.app/students`
- [ ] Test POST: Create a student via cURL or Postman

### Example Test Commands
```bash
# After deployment, replace with your actual URL
SITE_URL="https://your-site-name.netlify.app"

# Test health check
curl ${SITE_URL}/test

# Get all students
curl ${SITE_URL}/students

# Add a student
curl -X POST ${SITE_URL}/students \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Student",
    "age": 20,
    "marks": 85,
    "course": "CS"
  }'
```

## Troubleshooting

### Build Fails
- [ ] Check build log for error messages
- [ ] Verify all dependencies in `requirements.txt`
- [ ] Ensure `netlify.toml` has correct syntax
- [ ] Check Python version in `runtime.txt`

### 404 Errors on API Routes
- [ ] Verify `netlify.toml` redirects are correct
- [ ] Check that `netlify/functions/api.py` exists
- [ ] Verify functions directory setting in Netlify UI

### Import Errors
- [ ] Check Python path in `netlify/functions/api.py`
- [ ] Verify all modules in `src/api_test/` are present
- [ ] Ensure dependencies are in `requirements.txt`

### API Not Responding
- [ ] Check function logs in Netlify UI (Functions tab)
- [ ] Verify CORS headers if calling from frontend
- [ ] Check cold start delay (first request may take 3-5 seconds)

## Site Settings Reference

After deployment, you can manage your site via Netlify UI:

**Site Settings Location:**
1. Go to https://app.netlify.com
2. Select your site
3. Navigate to different tabs:
   - **Overview** - Deploy status and site info
   - **Deploys** - Deployment history and logs
   - **Build & deploy** - Build settings and environment variables
   - **Functions** - Function logs and metrics
   - **Redirects & rewrites** - URL routing configuration
   - **Custom domain** - Set up your own domain

## Environment Variables

To add environment variables (e.g., API keys, database URLs):

1. Site settings → Build & deploy → Environment
2. Click "Edit variables"
3. Add key-value pairs
4. Save and redeploy

Your code can access them via `os.environ['VARIABLE_NAME']`

## Redeployment

To redeploy after making changes:

### Option 1: Automatic (Recommended)
- Simply push changes to your main branch
- Netlify automatically rebuilds and deploys

### Option 2: Manual
1. Go to site in Netlify
2. Go to Deploys
3. Click "Trigger deploy" → "Deploy site"

## Monitoring & Logs

### Access Logs
1. Site → Deploys → Click on a deployment
2. View build log and deployment logs

### Monitor Functions
1. Site → Functions
2. View function invocations and errors
3. Set up notifications for failed deployments

## Custom Domain (Optional)

1. Site settings → Domain management
2. Add custom domain
3. Update DNS settings with your domain provider
4. Netlify provides free HTTPS/SSL certificate

## Success! 🎉

Your API is now live! Share the URL with users to start using your Student Management API.

---

**Need help?** Check [NETLIFY_DEPLOYMENT.md](./NETLIFY_DEPLOYMENT.md) for detailed deployment guide.
