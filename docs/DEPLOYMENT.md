# Deployment Guide

This guide covers options for deploying the Mobility-AI Displacement Analysis dashboard.

## Option 1: GitHub Pages (Static - Limited Interactivity)

GitHub Pages serves static files only. The Dash dashboard requires a Python server for full interactivity.

### Quick Static Export

```bash
python scripts/export_static_dashboard.py
```

This creates a static HTML page at `docs/dashboard/index.html` that can be served on GitHub Pages.

**Limitations:**
- No interactive callbacks
- No dynamic filtering
- Read-only view

### Enable GitHub Pages

1. Go to your repository Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main` (or `gh-pages`)
4. Folder: `/docs`
5. Save

The dashboard will be available at: `https://cesarmonagas15.github.io/mobility-ai-displacement-analysis/`

## Option 2: Render (Recommended - Full Interactivity)

[Render](https://render.com) offers free hosting for Python web applications.

### Steps:

1. **Create a `render.yaml` file** (already created in repo root)
2. **Connect GitHub repository** to Render
3. **Deploy automatically** on every push

### Manual Setup:

1. Sign up at [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name:** `mobility-ai-dashboard`
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python src/dashboard/interactive_dashboard.py`
   - **Port:** `8050` (Render sets PORT automatically)

Render will provide a URL like: `https://mobility-ai-dashboard.onrender.com`

## Option 3: Railway

[Railway](https://railway.app) is another excellent option for hosting Dash apps.

### Steps:

1. Sign up at [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway auto-detects Python and installs dependencies
5. Set start command: `python src/dashboard/interactive_dashboard.py`
6. Railway automatically assigns a URL

## Option 4: Heroku

[Heroku](https://www.heroku.com) supports Python web applications.

### Steps:

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: python src/dashboard/interactive_dashboard.py --host 0.0.0.0 --port $PORT
   ```
3. Deploy:
   ```bash
   heroku create mobility-ai-dashboard
   git push heroku main
   ```

## Option 5: Local Development

For local testing and development:

```bash
# Install dependencies
pip install -r requirements.txt

# Run dashboard
python src/dashboard/interactive_dashboard.py

# Or use the launch script
./scripts/launch_dashboard.sh
```

The dashboard will be available at: `http://127.0.0.1:8050/`

## Environment Variables

If deploying to a hosting service, you may want to set:

- `PORT`: Server port (usually set automatically by hosting service)
- `HOST`: Server host (usually `0.0.0.0` for public access)

## Troubleshooting

### Port Issues
- Hosting services usually set `PORT` automatically
- Update dashboard code to use: `port=int(os.environ.get('PORT', 8050))`

### Data File Paths
- Ensure data files are included in deployment
- Use relative paths (already configured in code)

### Dependencies
- All required packages are in `requirements.txt`
- Hosting services install these automatically

## Recommended Approach

**For full interactivity:** Use **Render** or **Railway** (both free tiers available)
**For static showcase:** Use **GitHub Pages** with exported HTML

