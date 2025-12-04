# Mobility-AI Displacement Analysis

A comprehensive research project exploring the relationship between economic mobility and AI-driven job displacement risk across U.S. counties.

**Authors:** Cesar Monagas and London Chamberlain

## 🔬 Research Hypothesis

Counties with historically low intergenerational economic mobility will exhibit significantly higher AI job displacement risk creating a 'double disadvantage' where technology reinforces existing patterns of limited economic opportunity.

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Launch Dashboard

**Option 1: Using the launch script (recommended)**
```bash
chmod +x scripts/launch_dashboard.sh
./scripts/launch_dashboard.sh
```

**Option 2: Direct Python command**
```bash
python src/dashboard/interactive_dashboard.py
```

The dashboard will open at: **http://127.0.0.1:8050/**

### 🌐 Online Access

**GitHub Pages (Static):** [View Dashboard](https://cesarmonagas15.github.io/mobility-ai-displacement-analysis/)

For full interactive features, see [Deployment Guide](docs/DEPLOYMENT.md) for hosting options.

## 📁 Project Structure

```
mobility-ai-displacement-analysis/
├── data/
│   ├── raw/                          # Original data files
│   │   ├── County Trends Estimates.csv
│   │   ├── Economic Census Data July 15 2025.xlsx
│   │   └── AIOE Data Appendix.xlsx
│   └── processed/                    # Cleaned and merged datasets
│       ├── merged_clean.csv
│       └── merged_clean.xlsx
├── src/
│   └── dashboard/                    # Dashboard application
│       └── interactive_dashboard.py
├── notebooks/                        # Jupyter notebooks
│   └── Analysis.ipynb
├── outputs/
│   ├── figures/                      # Static visualizations (PNG)
│   └── reports/                      # Interactive reports (HTML)
├── docs/                             # Documentation
│   ├── DASHBOARD_README.md
│   ├── DASHBOARD_GUIDE.md
│   └── QUICK_REFERENCE.md
├── scripts/                          # Utility scripts
│   ├── launch_dashboard.sh
│   └── check_dependencies.py
├── README.md
└── requirements.txt
```

## ✨ Dashboard Features

The interactive dashboard includes:

1. **KPI Cards** - Real-time statistics showing total counties, average scores, double disadvantage percentage, and correlation
2. **Geographic Choropleth Map** - County-level visualization with 3 viewing modes (classification, mobility, AI exposure)
3. **Correlation Analysis** - State and county-level scatter plots with regression lines and statistics
4. **Distribution Charts** - Histograms showing mobility and AI exposure distributions
5. **Category Breakdown** - Visual representation of county classifications
6. **Rankings** - Toggleable state/county rankings by top/worst performers

For detailed instructions, see [docs/DASHBOARD_README.md](docs/DASHBOARD_README.md)

## 🔬 About the Research

This project combines two critical datasets to understand economic vulnerability in the age of AI:

### Data Sources

1. **Opportunity Insights - County Trends Estimates**
   - Intergenerational economic mobility metrics
   - County-level granularity across the United States
   
2. **Economic Census - AI Occupational Exposure (AIOE)**
   - AI job displacement risk scores
   - Based on task automation potential

### Methodology

- **Geographic Level**: County-level analysis (3,000+ U.S. counties)
- **Statistical Analysis**: Pearson correlation, regression analysis, quadrant classification
- **Classification System**: 
  - Double Disadvantage (Low mobility + High AI risk)
  - Tech Disruption (High mobility + High AI risk)
  - Safe (High mobility + Low AI risk)
  - Stagnant Protected (Low mobility + Low AI risk)

### Key Findings

- **Pearson correlation**: -0.148 (weak negative, p < 0.001)
- **27.7%** of counties face "Double Disadvantage" (low mobility + high AI risk)
- Significant regional variation in vulnerability patterns
- Technology risks reinforcing existing economic inequality

## 📊 Usage

### Running the Dashboard
```bash
# From project root
python src/dashboard/interactive_dashboard.py
```

### Exploring Data in Notebooks
```bash
jupyter notebook notebooks/Analysis.ipynb
```

### Viewing Generated Reports
- Static figures: `outputs/figures/`
- Interactive reports: `outputs/reports/`

## 🤝 Contributing

This is a research project. For questions or collaboration inquiries, please contact the authors.

## 📄 License

[Add your license information here]

## 📚 Citation

If you use this research or dashboard in your work, please cite:

```
Monagas, C., & Chamberlain, L. (2025). 
Mobility-AI Displacement Analysis: Examining the Double Disadvantage 
of Low Economic Mobility and High AI Job Displacement Risk.
```
