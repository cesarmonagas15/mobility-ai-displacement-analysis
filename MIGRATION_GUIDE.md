# Project Structure Migration Guide

## What Changed?

The project has been reorganized from a flat structure to a standard research project layout following best practices used in academic and professional research software development.

## Before vs After

### Before (Flat Structure)
```
mobility-ai-displacement-analysis/
├── interactive_dashboard.py
├── Analysis.ipynb
├── merged_clean.csv
├── County Trends Estimates.csv
├── *.png (all figures)
├── *.html (all reports)
├── *.md (all docs)
└── ...
```

### After (Organized Structure)
```
mobility-ai-displacement-analysis/
├── data/
│   ├── raw/              # Original data
│   └── processed/        # Cleaned data
├── src/
│   └── dashboard/        # Dashboard code
├── notebooks/            # Jupyter notebooks
├── outputs/
│   ├── figures/          # PNG visualizations
│   └── reports/          # HTML reports
├── docs/                 # Documentation
└── scripts/              # Utility scripts
```

## File Locations

| File Type | Old Location | New Location |
|-----------|-------------|--------------|
| Dashboard | `./interactive_dashboard.py` | `src/dashboard/interactive_dashboard.py` |
| Notebooks | `./Analysis.ipynb` | `notebooks/Analysis.ipynb` |
| Raw data | `./*.csv`, `./*.xlsx` | `data/raw/` |
| Processed data | `./merged_clean.csv` | `data/processed/merged_clean.csv` |
| Figures | `./*.png` | `outputs/figures/` |
| Reports | `./*.html` | `outputs/reports/` |
| Documentation | `./*.md` | `docs/` + root `README.md` |
| Scripts | `./launch_dashboard.sh` | `scripts/launch_dashboard.sh` |

## How to Use the New Structure

### Running the Dashboard

**Old way:**
```bash
python interactive_dashboard.py
```

**New way:**
```bash
# From project root
python src/dashboard/interactive_dashboard.py

# Or use the launch script
./scripts/launch_dashboard.sh
```

### Accessing Data Files

The dashboard now automatically locates data files using relative paths. No manual configuration needed!

### Finding Files

- **Looking for figures?** → Check `outputs/figures/`
- **Need documentation?** → Check `docs/` or `README.md`
- **Want raw data?** → Check `data/raw/`
- **Need the clean dataset?** → Check `data/processed/`

## Benefits of the New Structure

### 1. **Clarity**
Each directory has a single, clear purpose. No more hunting through dozens of files in one folder.

### 2. **Reproducibility**
Standard structure makes it easy for other researchers to understand and replicate your work.

### 3. **Scalability**
As the project grows, adding new components is straightforward.

### 4. **Version Control**
Easier to manage what should/shouldn't be in git with organized structure.

### 5. **Collaboration**
Team members can quickly orient themselves using familiar conventions.

### 6. **Professional Standards**
Follows best practices from research software engineering.

## Common Tasks

### Add New Visualization
1. Generate in notebook or script
2. Save PNG to `outputs/figures/`
3. Save HTML to `outputs/reports/`

### Add New Data Source
1. Place original file in `data/raw/`
2. Process it (notebook or script)
3. Save cleaned version to `data/processed/`
4. Document in README or notebook

### Add New Documentation
1. Create `.md` file in `docs/`
2. Link from main `README.md` if needed

### Add New Analysis Script
1. Create in `src/` (create subdirectories as needed)
2. Import data from `data/processed/`
3. Save outputs to `outputs/`

## Need Help?

- **Project structure details**: See `docs/PROJECT_STRUCTURE.md`
- **Dashboard guide**: See `docs/DASHBOARD_README.md`
- **General info**: See `README.md`

## Questions or Issues?

If you encounter any issues with the new structure or have questions, please contact the project authors: Cesar Monagas and London Chamberlain.

---

**Migration completed**: December 2025

