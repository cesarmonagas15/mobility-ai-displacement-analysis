# Project Structure Guide

## Overview

This project follows standard research software development best practices with a clear separation of concerns between data, code, outputs, and documentation.

## Directory Structure

### 📂 `data/`
**Purpose**: All data files, both raw and processed

- **`data/raw/`**: Original, unmodified data files
  - `County Trends Estimates.csv` - Mobility data from Opportunity Insights
  - `Economic Census Data July 15 2025.xlsx` - Economic census data
  - `AIOE Data Appendix.xlsx` - AI Occupational Exposure data
  - ⚠️ **Never modify files in this directory**

- **`data/processed/`**: Cleaned, merged, and analysis-ready datasets
  - `merged_clean.csv` - Primary dataset used by dashboard
  - `merged_clean.xlsx` - Excel version of merged dataset

### 💻 `src/`
**Purpose**: Source code for the project

- **`src/dashboard/`**: Dashboard application code
  - `interactive_dashboard.py` - Main Dash application with all visualizations

### 📓 `notebooks/`
**Purpose**: Jupyter notebooks for exploratory analysis and documentation

- `Analysis.ipynb` - Main exploratory data analysis notebook

### 📊 `outputs/`
**Purpose**: Generated outputs from analysis and visualizations

- **`outputs/figures/`**: Static visualization exports (PNG format)
  - County analysis plots
  - State-level visualizations
  - Distribution plots
  - Correlation visualizations

- **`outputs/reports/`**: Interactive HTML reports
  - Interactive Plotly visualizations
  - Geographic visualizations

### 📚 `docs/`
**Purpose**: Project documentation

- `DASHBOARD_README.md` - Dashboard user guide
- `DASHBOARD_GUIDE.md` - Detailed dashboard instructions
- `QUICK_REFERENCE.md` - Quick reference guide
- `PROJECT_STRUCTURE.md` - This file

### 🔧 `scripts/`
**Purpose**: Utility scripts for project management

- `launch_dashboard.sh` - Shell script to launch the dashboard
- `check_dependencies.py` - Dependency verification script

### 📄 Root Files

- `README.md` - Main project documentation
- `requirements.txt` - Python package dependencies
- `.gitignore` - Git ignore patterns

## File Path Conventions

### Relative Paths

All code uses relative paths from appropriate base directories:

- **Dashboard code** (`src/dashboard/`): References data using `../../data/processed/`
- **Notebooks** (`notebooks/`): Reference data using `../data/`
- **Scripts** (`scripts/`): Run from project root

### Running Code

**Always run commands from the project root directory:**

```bash
# Correct
cd /path/to/mobility-ai-displacement-analysis
python src/dashboard/interactive_dashboard.py

# Or use the launch script
./scripts/launch_dashboard.sh
```

## Best Practices

### 1. Data Management
- Keep raw data immutable in `data/raw/`
- Store all processed data in `data/processed/`
- Document data transformations in notebooks

### 2. Code Organization
- Dashboard code in `src/dashboard/`
- Keep functions modular and well-documented
- Use clear variable names

### 3. Outputs
- Save static plots to `outputs/figures/`
- Save interactive visualizations to `outputs/reports/`
- Use descriptive filenames with dates if versioning

### 4. Documentation
- Keep README.md up to date
- Document major changes in `docs/`
- Comment complex code sections

### 5. Version Control
- Use `.gitignore` to exclude unnecessary files
- Commit frequently with clear messages
- Consider excluding large data files from git

## Adding New Files

When adding new components to the project:

| File Type | Location |
|-----------|----------|
| Raw data | `data/raw/` |
| Processed data | `data/processed/` |
| Python scripts | `src/` (create subdirectories as needed) |
| Jupyter notebooks | `notebooks/` |
| Generated figures | `outputs/figures/` |
| HTML reports | `outputs/reports/` |
| Documentation | `docs/` |
| Utility scripts | `scripts/` |

## Questions?

For questions about the project structure or best practices, refer to the main README.md or contact the project authors.

