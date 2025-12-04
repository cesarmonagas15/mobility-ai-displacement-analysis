#!/usr/bin/env python3
"""
Export Dashboard to Static HTML for GitHub Pages
================================================
This script exports the Dash dashboard to static HTML files that can be served on GitHub Pages.
Note: Interactive callbacks will not work in static HTML - this is a read-only version.
"""

import os
import sys

# Add src directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(script_dir, '..', 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

def export_static_dashboard():
    """Export dashboard to static HTML"""
    
    print("="*60)
    print("EXPORTING DASHBOARD TO STATIC HTML")
    print("="*60)
    
    # Import dashboard app
    from dashboard.interactive_dashboard import app
    
    # Create output directory
    output_dir = os.path.join(script_dir, '..', 'docs', 'dashboard')
    os.makedirs(output_dir, exist_ok=True)
    
    # Export to HTML
    output_path = os.path.join(output_dir, 'index.html')
    
    print(f"\nExporting dashboard to: {output_path}")
    print("Note: Interactive features will be limited in static HTML")
    
    # Create a simple HTML wrapper with the dashboard
    # Note: Dash apps can't be fully static, so we'll create a basic version
    # For full interactivity, use a hosting service like Render or Railway
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobility-AI Displacement Analysis Dashboard</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #0d6efd;
            margin-bottom: 10px;
        }
        .lead {
            color: #6c757d;
            font-size: 1.1rem;
            margin-bottom: 15px;
        }
        .info-box {
            background: #fff3cd;
            border: 1px solid #ffc107;
            border-radius: 5px;
            padding: 15px;
            margin: 20px 0;
        }
        .info-box h3 {
            margin-top: 0;
            color: #856404;
        }
        .deploy-link {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 20px;
            background: #0d6efd;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .deploy-link:hover {
            background: #0b5ed7;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>▪ Economic Mobility & AI Displacement Analysis</h1>
        <p class="lead">Interactive dashboard exploring the relationship between economic mobility and AI-driven job displacement risk across U.S. counties</p>
        <p style="font-style: italic; color: #6c757d;">Created by Cesar Monagas and London Chamberlain</p>
        
        <div class="info-box">
            <h3>📊 Interactive Dashboard</h3>
            <p>This static page provides an overview. For the full interactive dashboard with all features, please:</p>
            <ol>
                <li><strong>Run locally:</strong> Clone the repository and run <code>python src/dashboard/interactive_dashboard.py</code></li>
                <li><strong>Deploy to a hosting service:</strong> See <code>docs/DEPLOYMENT.md</code> for instructions on deploying to Render, Railway, or Heroku</li>
            </ol>
            <a href="https://github.com/cesarmonagas15/mobility-ai-displacement-analysis" class="deploy-link" target="_blank">
                View on GitHub →
            </a>
        </div>
        
        <h2>Research Hypothesis</h2>
        <p style="font-style: italic;">
            Counties with historically low intergenerational economic mobility will exhibit significantly higher AI job displacement risk creating a 'double disadvantage' where technology reinforces existing patterns of limited economic opportunity.
        </p>
        
        <h2>Key Findings</h2>
        <ul>
            <li><strong>Pearson correlation:</strong> -0.148 (weak negative, p < 0.001)</li>
            <li><strong>27.7%</strong> of counties face "Double Disadvantage" (low mobility + high AI risk)</li>
            <li>Significant regional variation in vulnerability patterns</li>
            <li>Technology risks reinforcing existing economic inequality</li>
        </ul>
        
        <h2>Getting Started</h2>
        <p>To run the interactive dashboard:</p>
        <pre style="background: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto;">
# Install dependencies
pip install -r requirements.txt

# Run dashboard
python src/dashboard/interactive_dashboard.py
        </pre>
        
        <p>The dashboard will open at <code>http://127.0.0.1:8050/</code></p>
        
        <hr style="margin: 30px 0;">
        
        <p style="text-align: center; color: #6c757d; font-size: 0.9rem;">
            Data Sources: Opportunity Insights (County Trends) & Economic Census (AIOE Data) | 
            <a href="https://github.com/cesarmonagas15/mobility-ai-displacement-analysis" target="_blank" style="color: #0d6efd;">GitHub</a>
        </p>
    </div>
</body>
</html>
"""
    
    with open(output_path, 'w') as f:
        f.write(html_content)
    
    print(f"\n✓ Static HTML exported to: {output_path}")
    print("\nNote: For full interactive features, deploy to a hosting service.")
    print("See docs/DEPLOYMENT.md for deployment options.")
    
    return output_path

if __name__ == "__main__":
    export_static_dashboard()

