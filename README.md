# Mobility-AI Displacement Analysis

## 📊 Interactive Dashboard

This project includes a comprehensive interactive dashboard that integrates all visualizations and analysis into a single, user-friendly interface.

### 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
python interactive_dashboard.py
```

Or use the launch script:
```bash
chmod +x launch_dashboard.sh
./launch_dashboard.sh
```

The dashboard will open at: **http://127.0.0.1:8050/**

### ✨ Dashboard Features

The interactive dashboard includes:

1. **5 Interactive KPI Cards** - Real-time statistics and metrics
2. **Geographic Choropleth Map** - County-level visualization with 3 viewing modes
3. **Correlation Analysis** - State and county-level scatter plots with regression
4. **Distribution Charts** - Histograms for mobility and AI exposure scores
5. **Category Breakdown** - Visual representation of county classifications
6. **State Rankings** - Top performers by mobility and AI protection

For detailed instructions, see [DASHBOARD_README.md](DASHBOARD_README.md)

## 📁 Project Files

- `interactive_dashboard.py` - Main dashboard application
- `Analysis.ipynb` - Jupyter notebook with exploratory analysis
- `merged_clean.csv` - Cleaned and merged dataset
- `*.html` - Individual interactive visualizations
- `*.png` - Static visualization exports

## 🔬 About the Analysis

This project explores the relationship between economic mobility and AI-driven job displacement risk across U.S. counties, combining:
- **Opportunity Insights**: County-level economic mobility data
- **Economic Census**: AI Occupational Exposure (AIOE) data

### Key Findings

- Pearson correlation: **-0.148** (weak negative, p < 0.001)
- **27.7%** of counties face "Double Disadvantage" (low mobility + high AI risk)
- Significant regional variation in vulnerability patterns

## 📊 Data Sources

- County Trends Estimates: Economic mobility scores by county
- AIOE Data Appendix: AI exposure scores by geographic area
