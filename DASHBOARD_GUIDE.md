# 📊 Interactive Dashboard - Visual Guide

## Dashboard Layout Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│  📊 Economic Mobility & AI Displacement Analysis                    │
│  Interactive dashboard exploring relationship between mobility       │
│  and AI-driven job displacement risk                                │
├─────────────────────────────────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                      │
│  │ KPI  │ │ KPI  │ │ KPI  │ │ KPI  │ │ KPI  │   ← 5 KPI Cards     │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘                      │
├────────────────────────────────────┬────────────────────────────────┤
│  🗺️ Geographic Visualization       │  📋 State Rankings            │
│  ┌──────────────────────────────┐  │  ┌──────────────────────────┐ │
│  │ [Dropdown: Select Metric]    │  │  │ [Dropdown: Rank By]      │ │
│  └──────────────────────────────┘  │  └──────────────────────────┘ │
│  ┌──────────────────────────────┐  │  ┌──────────────────────────┐ │
│  │                              │  │  │ Rank │ State │ Score    │ │
│  │    Interactive USA Map       │  │  │   1  │ ...   │ 0.XXX   │ │
│  │    (Choropleth)              │  │  │   2  │ ...   │ 0.XXX   │ │
│  │                              │  │  │  ... │ ...   │ ...     │ │
│  └──────────────────────────────┘  │  └──────────────────────────┘ │
├────────────────────────────────────┴────────────────────────────────┤
│  📉 Correlation Analysis                                            │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │ ○ State-Level  ○ County-Level  [Dropdown: Select State]       │ │
│  └────────────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │              Scatter Plot with Regression                      │ │
│  │              (Interactive hover, zoom, pan)                    │ │
│  └────────────────────────────────────────────────────────────────┘ │
├──────────────────────────┬──────────────────────────┬──────────────┤
│ 📊 Mobility Distribution │ 📊 AI Exposure Dist.    │ 📊 Category  │
│ ┌──────────────────────┐ │ ┌──────────────────────┐ │ Breakdown   │
│ │   Histogram          │ │ │   Histogram          │ │ ┌─────────┐ │
│ │   (with mean/median) │ │ │   (with mean/median) │ │ │Bar Chart│ │
│ └──────────────────────┘ │ └──────────────────────┘ │ └─────────┘ │
└──────────────────────────┴──────────────────────────┴──────────────┘
```

## Component Details

### 1. KPI Cards (Top Row)

Five real-time metric cards providing instant insights:

```
┌─────────────────┐
│ Total Counties  │
│     3,134       │ ← Large number display
│ Across 52 states│ ← Contextual info
└─────────────────┘
```

**Metrics Displayed:**
- 📊 Total Counties: Dataset size
- 📈 Avg Mobility Score: 0.456 (national average)
- ⚠️ Avg AI Exposure: -0.169 (national average)
- 🔴 Double Disadvantage: 27.7% (critical metric)
- 📉 Correlation: -0.148 (statistical relationship)

### 2. Geographic Visualization (Left Panel)

**Interactive Features:**
- 🖱️ Hover: View county details
- 🔍 Zoom: Scroll wheel
- 👆 Pan: Click and drag
- 📍 Click: Select county (future feature)

**Dropdown Options:**
1. **County Classification** (Default)
   - 🔴 Red = Double Disadvantage
   - 🟢 Green = Safe
   - 🟠 Orange = Tech Disruption
   - 🔵 Blue = Stagnant Protected

2. **Mobility Score**
   - Gradient: Red (low) → Yellow → Green (high)
   - Shows economic mobility patterns

3. **AI Exposure**
   - Gradient: Green (low risk) → Yellow → Red (high risk)
   - Shows AI displacement vulnerability

### 3. State Rankings Table (Right Panel)

**Two Ranking Modes:**

**Mode 1: By Mobility Score**
```
┌──────┬────────────────┬─────────┬──────────┐
│ Rank │ State          │ Score   │ Counties │
├──────┼────────────────┼─────────┼──────────┤
│  1   │ North Dakota   │ 0.513   │    53    │
│  2   │ South Dakota   │ 0.502   │    66    │
│  3   │ Iowa           │ 0.496   │    99    │
│ ...  │ ...            │ ...     │   ...    │
└──────┴────────────────┴─────────┴──────────┘
```

**Mode 2: By AI Protection (Lowest Exposure)**
```
┌──────┬────────────────┬─────────┬──────────┐
│ Rank │ State          │ AI Exp  │ Counties │
├──────┼────────────────┼─────────┼──────────┤
│  1   │ Montana        │ -0.823  │    56    │
│  2   │ Wyoming        │ -0.709  │    23    │
│ ...  │ ...            │ ...     │   ...    │
└──────┴────────────────┴─────────┴──────────┘
```

### 4. Correlation Analysis (Center Panel)

**State-Level View:**
```
Y-axis: AI Exposure Score
│
│    •         • ←  Bubbles sized by # of counties
│  •     •   •
│    •    •        ↗ Trend line (red)
│  •   •    •    ┊  ± 95% confidence interval (shaded)
│    •   •
└─────────────────── X-axis: Mobility Score

Statistics Box (bottom-right):
┌──────────────────────┐
│ Pearson r = -0.148   │
│ R² = 0.022           │
│ p-value < 0.001      │
│ n = 52 states        │
│ ✓ Significant        │
└──────────────────────┘
```

**County-Level View:**
- Select any state from dropdown
- Shows county-by-county variation within that state
- Regression line specific to that state
- Useful for identifying state-level patterns

**Interactive Controls:**
- ○ **State-Level** (default): View all states
- ○ **County-Level**: Drill down into specific states
- **[Select State ▼]**: Choose state (enabled in County mode)

### 5. Distribution Charts (Bottom Row)

**Three side-by-side histograms:**

**Chart 1: Mobility Distribution**
```
Frequency
│
│   ┌─┐
│   │ │  ┌─┐
│ ┌─┤ ├──┤ ├─┐
│ │ │ │  │ │ │
└─┴─┴─┴──┴─┴─┴─── Mobility Score
  ^Mean  ^Median
```

**Chart 2: AI Exposure Distribution**
```
Frequency
│     ┌─┐
│ ┌─┐ │ │ ┌─┐
│ │ ├─┤ ├─┤ │
│ │ │ │ │ │ │
└─┴─┴─┴─┴─┴─┴─── AI Exposure
    ^Median ^Mean
```

**Chart 3: Category Breakdown**
```
Count
│
│ ██  869 (27.7%)
│ ██  
│ ██  ██  698 (22.3%)
│ ██  ██  ██  ██
└─┴───┴───┴───┴─── Categories
  DD  Safe Dis Prot

DD = Double Disadvantage
Dis = Tech Disruption
Prot = Stagnant Protected
```

## 🖱️ Interaction Guide

### Hovering
- **Map**: See county name, state, mobility score, AI exposure
- **Scatter Plot**: See specific values and labels
- **Charts**: View exact values at any point

### Clicking
- **Dropdown Menus**: Switch visualization modes
- **Radio Buttons**: Toggle between analysis levels
- **Legend Items**: Show/hide data series (on charts)

### Zooming & Panning
- **Map**: Scroll to zoom, drag to pan
- **Scatter Plot**: Click and drag to zoom box, double-click to reset
- **All Charts**: Interactive Plotly controls in top-right corner

## 📊 Use Case Scenarios

### Scenario 1: National Overview
**Goal**: Understand overall relationship between mobility and AI risk

**Steps**:
1. Look at KPI cards for quick stats
2. View Geographic Map in "Classification" mode
3. Check State-Level scatter plot for correlation
4. Review distribution charts for patterns

**What to Look For**:
- Regional clustering on map
- Correlation strength in scatter plot
- Distribution shapes (normal, skewed, bimodal)

### Scenario 2: State Comparison
**Goal**: Compare two specific states

**Steps**:
1. View State Rankings table
2. Switch to County-Level in correlation analysis
3. Select first state, note statistics
4. Select second state, compare

**What to Look For**:
- Different correlation patterns
- Within-state variation
- Number of "double disadvantage" counties

### Scenario 3: Identify Vulnerable Areas
**Goal**: Find counties needing intervention

**Steps**:
1. Set Map to "Classification" mode
2. Look for red (Double Disadvantage) counties
3. Hover over red areas for specifics
4. Check state rankings to see state-level patterns

**What to Look For**:
- Clusters of red counties
- States with high percentages of DD counties
- Geographic patterns (rural vs urban, regional)

### Scenario 4: Data Exploration
**Goal**: Find interesting patterns and outliers

**Steps**:
1. Switch Map between all three modes
2. Toggle scatter plot between state and county levels
3. Hover over outliers
4. Check distribution charts for unusual patterns

**What to Look For**:
- Counties with extreme values
- States that don't follow the trend
- Bimodal or unusual distributions

## 🎨 Color Coding Reference

### County Classification Colors
- 🔴 **#d62728** (Red) = Double Disadvantage
  - Low mobility + High AI risk
  - Most vulnerable counties

- 🟠 **#ff7f0e** (Orange) = Tech Disruption
  - High mobility + High AI risk
  - Adapting to change but at risk

- 🟢 **#2ca02c** (Green) = Safe
  - High mobility + Low AI risk
  - Best positioned counties

- 🔵 **#1f77b4** (Blue) = Stagnant Protected
  - Low mobility + Low AI risk
  - Low risk but limited opportunity

### Continuous Scales
- **Mobility**: Red → Yellow → Green (RdYlGn)
- **AI Exposure**: Green → Yellow → Red (RdYlGn_r, reversed)

## 🔧 Advanced Features

### Export Capabilities
- **📸 Static Image**: Click camera icon in chart controls
- **📊 Data**: Hover over points to see values
- **🔗 Share**: Copy URL (preserves current view)

### Performance Tips
- Dashboard is optimized for 3,000+ data points
- Map uses WebGL for smooth rendering
- All visualizations are responsive
- Works best in Chrome, Firefox, Safari

## ❓ FAQ

**Q: Why is the correlation negative?**
A: Negative correlation (-0.148) means higher mobility tends to associate with slightly lower AI risk, though the relationship is weak.

**Q: What does "Double Disadvantage" mean?**
A: Counties that score below median on mobility AND above median on AI risk—facing both low economic opportunity and high job displacement risk.

**Q: Can I zoom into specific regions?**
A: Yes! Click and drag on the map, or use scroll wheel to zoom. Double-click to reset.

**Q: Why aren't all counties shown?**
A: The dataset includes 3,134 of 3,243 U.S. counties (96.6%) based on data availability.

**Q: How do I interpret the p-value?**
A: p < 0.05 indicates statistical significance. Our p < 0.001 means the correlation is highly unlikely to be due to chance.

---

**Ready to explore?** Run the dashboard with:
```bash
python interactive_dashboard.py
```

Then navigate to: http://127.0.0.1:8050/

