# Interactive Dashboard - Mobility & AI Displacement Analysis

## 🎯 Overview

This interactive dashboard provides comprehensive visualization and analysis of the relationship between economic mobility and AI-driven job displacement risk across U.S. counties.

## 📊 Dashboard Features

### 1. **Key Performance Indicators (KPIs)** - 5 Interactive Cards
   - **Total Counties**: Complete dataset coverage
   - **Average Mobility Score**: National economic mobility baseline
   - **Average AI Exposure**: National AI displacement risk baseline
   - **Double Disadvantage**: Percentage of counties facing both low mobility AND high AI risk
   - **Correlation Statistics**: Pearson correlation coefficient with significance testing

### 2. **Geographic Choropleth Map** 🗺️
   - Interactive county-level map of the United States
   - Three visualization modes:
     - **County Classification**: 4-quadrant categorization
       - 🔴 Double Disadvantage (Low Mobility + High AI Risk)
       - 🟢 Safe (High Mobility + Low AI Risk)
       - 🟠 Tech Disruption (High Mobility + High AI Risk)
       - 🔵 Stagnant Protected (Low Mobility + Low AI Risk)
     - **Mobility Score**: Gradient visualization of economic mobility
     - **AI Exposure**: Gradient visualization of AI displacement risk
   - Hover tooltips with detailed county information

### 3. **Correlation Analysis Scatter Plot** 📉
   - **State-Level View**: 
     - Bubble size represents number of counties
     - Regression line with 95% confidence interval
     - Statistical significance testing
   - **County-Level View**: 
     - Drill down into any state
     - County-by-county analysis
     - State-specific correlation statistics
   - Real-time metric calculations displayed

### 4. **Distribution Histograms** 📊
   - **Mobility Score Distribution**: 
     - Frequency distribution across all counties
     - Mean and median reference lines
   - **AI Exposure Distribution**: 
     - Frequency distribution of AI risk scores
     - Mean and median reference lines

### 5. **Category Breakdown Chart** 📊
   - Bar chart showing count and percentage of counties in each category
   - Color-coded to match map visualization

### 6. **State Rankings Table** 📋
   - **Top 10 by Mobility Score**: States with best economic mobility
   - **Top 10 by AI Protection**: States with lowest AI displacement risk
   - Includes number of counties per state

## 🚀 Installation & Setup

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Ensure Data Files Are Present

Make sure these files are in the same directory:
- `merged_clean.csv` (main dataset)
- `interactive_dashboard.py` (dashboard script)

### Step 3: Run the Dashboard

```bash
python interactive_dashboard.py
```

### Step 4: Open in Browser

The dashboard will automatically open at: **http://127.0.0.1:8050/**

If it doesn't open automatically, copy and paste this URL into your browser.

## 🎨 How to Use the Dashboard

### Navigation Tips:

1. **KPI Cards** (Top Row):
   - Get instant insights into overall dataset statistics
   - Check correlation significance (✓ = statistically significant)

2. **Geographic Map** (Left Panel):
   - Use dropdown to switch between visualization modes
   - Click and drag to pan
   - Scroll to zoom
   - Hover over counties for detailed information

3. **State Rankings** (Right Panel):
   - Switch between mobility and AI protection rankings
   - Identify best/worst performing states

4. **Correlation Analysis** (Middle Section):
   - Toggle between State and County level
   - When in County mode, select a state from dropdown
   - View regression statistics in the annotation box
   - Hover over points for specific values

5. **Distribution Charts** (Bottom Row):
   - Compare distributions across metrics
   - Identify outliers and patterns
   - View mean/median reference lines

## 📈 Key Insights to Explore

### Research Questions the Dashboard Helps Answer:

1. **Is there a correlation between economic mobility and AI displacement risk?**
   - View: Correlation Analysis (State-Level)
   - Check the Pearson r value and p-value

2. **Which states face the greatest double disadvantage?**
   - View: Geographic Map (Category mode)
   - Look for red counties

3. **Are there regional patterns?**
   - View: Geographic Map (any mode)
   - Look for clustering of similar colors

4. **Which states are most/least vulnerable?**
   - View: State Rankings Table
   - Compare mobility and AI exposure rankings

5. **How do counties within a state compare?**
   - View: Correlation Analysis (County-Level)
   - Select individual states to see variation

## 🔧 Troubleshooting

### Dashboard won't start:
```bash
# Check if required packages are installed
pip list | grep dash

# Reinstall if needed
pip install -r requirements.txt --upgrade
```

### Data not loading:
- Ensure `merged_clean.csv` is in the same directory
- Check file permissions
- Verify CSV format (should have headers: county_fips, state_name, county_name, mobility_score, ai_exposure)

### Port 8050 already in use:
```python
# Edit the last line of interactive_dashboard.py to use a different port:
app.run_server(debug=True, port=8051)  # Change 8050 to 8051 or any available port
```

## 📊 Data Dictionary

| Field | Description | Range |
|-------|-------------|-------|
| `mobility_score` | Economic mobility percentile rank (higher = better intergenerational mobility) | 0.06 - 0.78 |
| `ai_exposure` | AI displacement risk score (higher = greater job displacement risk) | -6.06 - 4.20 |
| `county_fips` | 5-digit FIPS code (unique county identifier) | 01001 - 72153 |
| `state_name` | Full state name | Alabama - Wyoming |
| `county_name` | County name | Various |
| `category` | Quadrant classification | Double Disadvantage, Safe, Tech Disruption, Stagnant Protected |

## 🎯 Technical Architecture

- **Framework**: Plotly Dash with Bootstrap styling
- **Backend**: Python 3.8+
- **Visualization**: Plotly.js (WebGL-accelerated)
- **Data Processing**: Pandas & NumPy
- **Statistics**: SciPy
- **Geographic Data**: US Census Bureau GeoJSON

## 📝 Citation

If using this dashboard for research or presentations, please cite:

```
Mobility-AI Displacement Analysis Dashboard
Data Sources: 
- Opportunity Insights: County-Level Economic Mobility Data
- Economic Census: AI Occupational Exposure (AIOE) Data
```

## 🤝 Support

For questions or issues:
1. Check the Troubleshooting section above
2. Review the data files for integrity
3. Ensure all dependencies are installed

## 🔄 Updates & Maintenance

To update with new data:
1. Replace `merged_clean.csv` with updated data (maintain same column structure)
2. Restart the dashboard
3. All visualizations will automatically update

---

**Enjoy exploring the data!** 📊🚀

