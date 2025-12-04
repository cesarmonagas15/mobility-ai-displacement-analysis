# 🚀 Dashboard Quick Reference Card

## One-Line Launch
```bash
python interactive_dashboard.py
```
**URL**: http://127.0.0.1:8050/

---

## 📊 5 Main Components

| # | Component | What It Shows | Key Action |
|---|-----------|---------------|------------|
| 1 | **KPI Cards** | Overall statistics | Quick insights |
| 2 | **Map** | Geographic patterns | Hover for details |
| 3 | **Scatter Plot** | Correlation analysis | Toggle state/county |
| 4 | **Distributions** | Data spread | Compare metrics |
| 5 | **Rankings** | Top/bottom states | Sort by metric |

---

## 🎨 Color Legend

| Color | Category | Meaning |
|-------|----------|---------|
| 🔴 Red | Double Disadvantage | Low mobility + High AI risk |
| 🟢 Green | Safe | High mobility + Low AI risk |
| 🟠 Orange | Tech Disruption | High mobility + High AI risk |
| 🔵 Blue | Stagnant Protected | Low mobility + Low AI risk |

---

## 🖱️ Quick Actions

### Map Controls
- **Hover** → See county details
- **Scroll** → Zoom in/out
- **Drag** → Pan around
- **Dropdown** → Change metric

### Scatter Plot
- **Radio** → Switch state/county view
- **Dropdown** → Select state (county mode)
- **Hover** → See exact values
- **Zoom Box** → Drag to zoom

### General
- **Camera Icon** → Export image
- **Double-Click** → Reset view
- **Legend Click** → Show/hide series

---

## 📊 Key Metrics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Total Counties** | 3,134 | Dataset coverage |
| **Avg Mobility** | 0.456 | Percentile rank (0-1) |
| **Avg AI Exposure** | -0.169 | Risk score |
| **Double Disadvantage** | 27.7% | At-risk counties |
| **Correlation** | -0.148*** | Weak negative |

\* p < 0.05, \*\* p < 0.01, \*\*\* p < 0.001

---

## 🎯 Common Tasks

### Find Vulnerable Counties
1. Map → "Classification" mode
2. Look for 🔴 red areas
3. Hover for specifics

### Compare States
1. Rankings table → Find states
2. Scatter → County-Level mode
3. Dropdown → Select each state

### Explore Patterns
1. View all 3 map modes
2. Check distribution charts
3. Look for clustering

### Export Data/Images
1. Hover over chart
2. Click 📸 camera icon
3. Save image

---

## 🔢 Data Ranges

| Variable | Min | Max | Mean | Median |
|----------|-----|-----|------|--------|
| **Mobility Score** | 0.064 | 0.779 | 0.456 | 0.450 |
| **AI Exposure** | -6.06 | 4.20 | -0.169 | -0.130 |

---

## ⚡ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **Ctrl/Cmd + R** | Refresh dashboard |
| **Ctrl/Cmd + F** | Find on page |
| **F11** | Fullscreen (browser) |
| **Ctrl/Cmd + +/-** | Zoom page |

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Dashboard won't start | `pip install -r requirements.txt` |
| Port 8050 in use | Edit line 700: `port=8051` |
| Map not loading | Check internet connection (needs GeoJSON) |
| Data not showing | Verify `merged_clean.csv` exists |

---

## 📚 Documentation Files

- **README.md** → Project overview
- **DASHBOARD_README.md** → Full installation guide
- **DASHBOARD_GUIDE.md** → Detailed visual guide
- **QUICK_REFERENCE.md** → This file

---

## 🆘 Help

**Dashboard Frozen?**
1. Check terminal for errors
2. Press `Ctrl+C` to stop
3. Restart dashboard

**Data Questions?**
- Mobility: Higher = better intergenerational mobility
- AI Exposure: Higher = greater job displacement risk
- FIPS: 5-digit county identifier

**Performance Issues?**
- Close other browser tabs
- Use Chrome for best performance
- Reduce browser zoom level

---

## 📞 Quick Stats at a Glance

```
┌─────────────────────────────────────┐
│  Dataset: 3,134 U.S. Counties       │
│  States: 52 (incl. DC, PR)          │
│  Correlation: -0.148***             │
│  Double Disadvantage: 869 (27.7%)   │
│  Safe Counties: 869 (27.7%)         │
│  Tech Disruption: 698 (22.3%)       │
│  Stagnant Protected: 698 (22.3%)    │
└─────────────────────────────────────┘
```

---

**Print this page for easy reference while using the dashboard!**

*Last Updated: November 2025*

