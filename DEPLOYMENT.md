# GitHub Pages Setup Guide

## 🚀 Enable GitHub Pages Deployment

To enable automatic deployment to GitHub Pages, follow these steps:

### Step 1: Enable GitHub Pages
1. Go to your repository: https://github.com/muhammadhasaan82/Startup
2. Click on **Settings** (top menu)
3. In the left sidebar, click on **Pages**
4. Under **Build and deployment**:
   - **Source**: Select "GitHub Actions"
   - This will allow the CI/CD pipeline to deploy automatically

### Step 2: Verify Workflow Permissions
1. In your repository, go to **Settings** → **Actions** → **General**
2. Scroll down to **Workflow permissions**
3. Select **"Read and write permissions"**
4. Check **"Allow GitHub Actions to create and approve pull requests"**
5. Click **Save**

### Step 3: Trigger Deployment
The deployment will automatically trigger when you push to the `main` branch.

You can also manually trigger it:
1. Go to **Actions** tab in your repository
2. Click on **Deploy to GitHub Pages** workflow
3. Click **Run workflow** → **Run workflow**

### Step 4: Access Your Live Site
Once deployed (takes 1-2 minutes), your site will be available at:

**https://muhammadhasaan82.github.io/Startup/**

## 📊 Monitoring Deployments

### View Workflow Status
- Go to the **Actions** tab in your repository
- You'll see all workflow runs with their status (✅ success, ❌ failed, 🟡 in progress)
- Click on any run to see detailed logs

### CI/CD Badges
The README.md includes status badges that show:
- [![Deploy](https://github.com/muhammadhasaan82/Startup/actions/workflows/deploy.yml/badge.svg)](https://github.com/muhammadhasaan82/Startup/actions/workflows/deploy.yml) - Deployment status
- [![CI](https://github.com/muhammadhasaan82/Startup/actions/workflows/ci.yml/badge.svg)](https://github.com/muhammadhasaan82/Startup/actions/workflows/ci.yml) - Build/test status

## 🔄 How It Works

### On Every Push to Main:
1. **CI Workflow** runs:
   - Installs dependencies
   - Runs TypeScript type checking
   - Builds the project
   - Verifies build success

2. **Deploy Workflow** runs:
   - Builds the production bundle
   - Uploads artifacts to GitHub Pages
   - Deploys to your live site

### On Pull Requests:
- Only the **CI Workflow** runs
- Ensures code quality before merging
- No deployment happens until merged to main

## 🛠️ Troubleshooting

### Deployment Failed?
1. Check the **Actions** tab for error logs
2. Common issues:
   - Missing permissions (see Step 2 above)
   - Build errors (fix TypeScript/build issues locally first)
   - GitHub Pages not enabled (see Step 1)

### Site Not Loading?
1. Verify the base path in `vite.config.ts` matches your repo name
2. Check browser console for 404 errors
3. Clear browser cache and try again

### Need to Redeploy?
```bash
# Make a small change (or empty commit)
git commit --allow-empty -m "Trigger deployment"
git push
```

## 📝 Notes

- First deployment may take 2-3 minutes
- Subsequent deployments are faster (1-2 minutes)
- GitHub Pages has a soft limit of 10 deployments per hour
- The site uses the `/Startup/` base path (your repo name)

## 🎉 Success!

Once everything is set up, your CI/CD pipeline will:
- ✅ Automatically test every commit
- ✅ Deploy to production on every push to main
- ✅ Provide status badges in your README
- ✅ Give you a live URL to share with the world!

---

**Need help?** Check the [GitHub Pages documentation](https://docs.github.com/en/pages) or open an issue in your repository.
