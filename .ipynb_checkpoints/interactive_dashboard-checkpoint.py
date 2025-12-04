"""
Interactive Dashboard for Mobility-AI Displacement Analysis
=============================================================
A comprehensive dashboard integrating geographic maps, statistical visualizations,
and interactive KPIs to explore the relationship between economic mobility and AI displacement risk.
"""

import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from scipy import stats
import requests
import json

# =============================================================================
# DATA LOADING AND PREPARATION
# =============================================================================

print("Loading data...")
merged_data = pd.read_csv('merged_clean.csv')

# Ensure proper FIPS formatting
merged_data['county_fips'] = merged_data['county_fips'].astype(str).str.zfill(5)

# Clean data: remove infinite values and NaNs
merged_data = merged_data.replace([np.inf, -np.inf], np.nan)
merged_data = merged_data.dropna(subset=['mobility_score', 'ai_exposure'])
print(f"Clean dataset: {len(merged_data)} counties")

# Create state-level aggregations
state_summary = merged_data.groupby('state_name').agg({
    'mobility_score': 'mean',
    'ai_exposure': 'mean',
    'county_fips': 'count'
}).reset_index()
state_summary.rename(columns={'county_fips': 'num_counties'}, inplace=True)

# Calculate quadrant categories
mobility_median = merged_data['mobility_score'].median()
ai_median = merged_data['ai_exposure'].median()

def categorize_county(row):
    if row['mobility_score'] < mobility_median and row['ai_exposure'] > ai_median:
        return 'Double Disadvantage'
    elif row['mobility_score'] >= mobility_median and row['ai_exposure'] <= ai_median:
        return 'Safe'
    elif row['mobility_score'] >= mobility_median and row['ai_exposure'] > ai_median:
        return 'Tech Disruption'
    else:
        return 'Stagnant Protected'

merged_data['category'] = merged_data.apply(categorize_county, axis=1)

# Load GeoJSON for counties
print("Loading geographic data...")
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
counties_geojson = requests.get(url).json()

# Calculate correlation statistics
pearson_r, p_value = stats.pearsonr(merged_data['mobility_score'], merged_data['ai_exposure'])

print("Data loaded successfully!")

# =============================================================================
# VISUALIZATION FUNCTIONS
# =============================================================================

def create_kpi_cards():
    """Create KPI summary cards"""
    
    total_counties = len(merged_data)
    avg_mobility = merged_data['mobility_score'].mean()
    avg_ai_exposure = merged_data['ai_exposure'].mean()
    
    # Count double disadvantage counties
    double_disadvantage = (merged_data['category'] == 'Double Disadvantage').sum()
    dd_pct = (double_disadvantage / total_counties) * 100
    
    # Correlation strength
    corr_strength = abs(pearson_r)
    
    cards = dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Total Counties", className="text-muted"),
                    html.H2(f"{total_counties:,}", className="text-primary"),
                    html.P("Across 52 states", className="text-sm")
                ])
            ], className="shadow-sm")
        ], width=12, md=2),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Avg Mobility Score", className="text-muted"),
                    html.H2(f"{avg_mobility:.3f}", className="text-success"),
                    html.P("Higher = Better Mobility", className="text-sm")
                ])
            ], className="shadow-sm")
        ], width=12, md=2),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Avg AI Exposure", className="text-muted"),
                    html.H2(f"{avg_ai_exposure:.3f}", className="text-warning"),
                    html.P("Higher = More Risk", className="text-sm")
                ])
            ], className="shadow-sm")
        ], width=12, md=2),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Double Disadvantage", className="text-muted"),
                    html.H2(f"{dd_pct:.1f}%", className="text-danger"),
                    html.P(f"{double_disadvantage} counties", className="text-sm")
                ])
            ], className="shadow-sm")
        ], width=12, md=3),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Correlation", className="text-muted"),
                    html.H2(f"{pearson_r:.3f}", className="text-info"),
                    html.P(f"p < 0.001 {'✓' if p_value < 0.05 else '✗'}", className="text-sm")
                ])
            ], className="shadow-sm")
        ], width=12, md=3),
    ], className="mb-4")
    
    return cards


def create_choropleth_map(selected_metric='category'):
    """Create interactive choropleth map"""
    
    if selected_metric == 'category':
        color_map = {
            'Double Disadvantage': '#d62728',
            'Tech Disruption': '#ff7f0e',
            'Safe': '#2ca02c',
            'Stagnant Protected': '#1f77b4'
        }
        
        fig = px.choropleth(
            merged_data,
            geojson=counties_geojson,
            locations='county_fips',
            color='category',
            color_discrete_map=color_map,
            scope="usa",
            hover_data={
                'county_name': True,
                'state_name': True,
                'mobility_score': ':.3f',
                'ai_exposure': ':.3f',
                'county_fips': False,
                'category': True
            },
            labels={'category': 'Classification'},
            title='County Classification: Mobility vs AI Risk'
        )
    elif selected_metric == 'mobility_score':
        fig = px.choropleth(
            merged_data,
            geojson=counties_geojson,
            locations='county_fips',
            color='mobility_score',
            color_continuous_scale='RdYlGn',
            scope="usa",
            hover_data={
                'county_name': True,
                'state_name': True,
                'mobility_score': ':.3f',
                'ai_exposure': ':.3f',
                'county_fips': False
            },
            title='Economic Mobility Score by County'
        )
    else:  # ai_exposure
        fig = px.choropleth(
            merged_data,
            geojson=counties_geojson,
            locations='county_fips',
            color='ai_exposure',
            color_continuous_scale='RdYlGn_r',
            scope="usa",
            hover_data={
                'county_name': True,
                'state_name': True,
                'mobility_score': ':.3f',
                'ai_exposure': ':.3f',
                'county_fips': False
            },
            title='AI Exposure Score by County'
        )
    
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        height=500,
        margin={"r":0,"t":40,"l":0,"b":0},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig


def create_scatter_plot(level='state', selected_state=None):
    """Create scatter plot with regression"""
    
    if level == 'state' or selected_state is None:
        data = state_summary
        x_col, y_col = 'mobility_score', 'ai_exposure'
        size_col = 'num_counties'
        text_col = 'state_name'
        title = 'State-Level: Mobility vs AI Exposure'
        
        # Calculate regression
        slope, intercept, r_value, p_val, std_err = stats.linregress(
            data[x_col], data[y_col]
        )
        
    else:
        data = merged_data[merged_data['state_name'] == selected_state]
        x_col, y_col = 'mobility_score', 'ai_exposure'
        text_col = 'county_name'
        size_col = None
        title = f'{selected_state}: County-Level Mobility vs AI Exposure'
        
        if len(data) >= 3:
            slope, intercept, r_value, p_val, std_err = stats.linregress(
                data[x_col], data[y_col]
            )
        else:
            slope = intercept = r_value = p_val = None
    
    # Create scatter plot
    fig = go.Figure()
    
    # Add scatter points
    if size_col:
        fig.add_trace(go.Scatter(
            x=data[x_col],
            y=data[y_col],
            mode='markers',
            marker=dict(
                size=data[size_col] * 0.5,
                color=data[x_col],
                colorscale='RdYlBu',
                showscale=True,
                colorbar=dict(title="Mobility<br>Score"),
                line=dict(color='black', width=1),
                opacity=0.7
            ),
            text=data[text_col],
            hovertemplate='<b>%{text}</b><br>' +
                          'Mobility: %{x:.3f}<br>' +
                          'AI Exposure: %{y:.3f}<br>' +
                          '<extra></extra>',
            name='Data Points'
        ))
    else:
        fig.add_trace(go.Scatter(
            x=data[x_col],
            y=data[y_col],
            mode='markers',
            marker=dict(
                size=10,
                color=data[x_col],
                colorscale='RdYlBu',
                showscale=True,
                colorbar=dict(title="Mobility<br>Score"),
                line=dict(color='black', width=0.5),
                opacity=0.7
            ),
            text=data[text_col],
            hovertemplate='<b>%{text}</b><br>' +
                          'Mobility: %{x:.3f}<br>' +
                          'AI Exposure: %{y:.3f}<br>' +
                          '<extra></extra>',
            name='Data Points'
        ))
    
    # Add regression line
    if slope is not None:
        x_range = np.linspace(data[x_col].min(), data[x_col].max(), 100)
        y_regression = slope * x_range + intercept
        
        fig.add_trace(go.Scatter(
            x=x_range,
            y=y_regression,
            mode='lines',
            name='Trend Line',
            line=dict(color='red', width=3),
            hovertemplate=f'Linear Trend<br>r={r_value:.3f}<extra></extra>'
        ))
        
        # Add confidence interval
        predict_y = slope * data[x_col].values + intercept
        residuals = data[y_col].values - predict_y
        std_residuals = np.std(residuals)
        ci = 1.96 * std_residuals
        
        fig.add_trace(go.Scatter(
            x=np.concatenate([x_range, x_range[::-1]]),
            y=np.concatenate([y_regression + ci, (y_regression - ci)[::-1]]),
            fill='toself',
            fillcolor='rgba(255,0,0,0.2)',
            line=dict(color='rgba(255,0,0,0)'),
            name='95% CI',
            showlegend=True,
            hoverinfo='skip'
        ))
        
        # Add statistics annotation
        stats_text = f'<b>Statistics</b><br>' + \
                     f'Pearson r = {r_value:.3f}<br>' + \
                     f'R² = {r_value**2:.3f}<br>' + \
                     f'p-value = {p_val:.4f}<br>' + \
                     f'n = {len(data)}<br>'
        
        if p_val < 0.05:
            stats_text += '<i>✓ Significant</i>'
        else:
            stats_text += '<i>Not significant</i>'
        
        fig.add_annotation(
            text=stats_text,
            xref='paper', yref='paper',
            x=0.98, y=0.02,
            xanchor='right', yanchor='bottom',
            showarrow=False,
            bordercolor='black',
            borderwidth=2,
            borderpad=10,
            bgcolor='white',
            opacity=0.9,
            font=dict(size=10)
        )
    
    fig.update_layout(
        title=title,
        xaxis_title='Economic Mobility Score',
        yaxis_title='AI Exposure Score',
        height=450,
        template='plotly_white',
        hovermode='closest',
        showlegend=True,
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,1)'
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray')
    
    return fig


def create_distribution_plots():
    """Create distribution histograms"""
    
    fig = go.Figure()
    
    # Mobility distribution
    fig.add_trace(go.Histogram(
        x=merged_data['mobility_score'],
        name='Mobility Score',
        marker_color='steelblue',
        opacity=0.7,
        nbinsx=40
    ))
    
    fig.update_layout(
        title='Distribution of Economic Mobility Scores',
        xaxis_title='Mobility Score',
        yaxis_title='Frequency',
        height=350,
        template='plotly_white',
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,1)'
    )
    
    # Add mean and median lines
    fig.add_vline(
        x=merged_data['mobility_score'].mean(),
        line_dash="dash",
        line_color="red",
        annotation_text="Mean",
        annotation_position="top"
    )
    fig.add_vline(
        x=merged_data['mobility_score'].median(),
        line_dash="dash",
        line_color="green",
        annotation_text="Median",
        annotation_position="top"
    )
    
    return fig


def create_ai_distribution_plot():
    """Create AI exposure distribution"""
    
    fig = go.Figure()
    
    fig.add_trace(go.Histogram(
        x=merged_data['ai_exposure'],
        name='AI Exposure',
        marker_color='coral',
        opacity=0.7,
        nbinsx=40
    ))
    
    fig.update_layout(
        title='Distribution of AI Exposure Scores',
        xaxis_title='AI Exposure Score',
        yaxis_title='Frequency',
        height=350,
        template='plotly_white',
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,1)'
    )
    
    # Add mean and median lines
    fig.add_vline(
        x=merged_data['ai_exposure'].mean(),
        line_dash="dash",
        line_color="red",
        annotation_text="Mean",
        annotation_position="top"
    )
    fig.add_vline(
        x=merged_data['ai_exposure'].median(),
        line_dash="dash",
        line_color="green",
        annotation_text="Median",
        annotation_position="top"
    )
    
    return fig


def create_category_breakdown():
    """Create category breakdown chart"""
    
    category_counts = merged_data['category'].value_counts()
    
    colors = {
        'Double Disadvantage': '#d62728',
        'Tech Disruption': '#ff7f0e',
        'Safe': '#2ca02c',
        'Stagnant Protected': '#1f77b4'
    }
    
    fig = go.Figure(data=[go.Bar(
        x=category_counts.index,
        y=category_counts.values,
        marker_color=[colors[cat] for cat in category_counts.index],
        text=[f'{val}<br>({val/len(merged_data)*100:.1f}%)' 
              for val in category_counts.values],
        textposition='auto',
    )])
    
    fig.update_layout(
        title='County Classification Breakdown',
        xaxis_title='Category',
        yaxis_title='Number of Counties',
        height=350,
        template='plotly_white',
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,1)'
    )
    
    return fig


def create_state_ranking_table(metric='mobility_score', top_n=10):
    """Create state ranking table"""
    
    if metric == 'mobility_score':
        sorted_data = state_summary.sort_values('mobility_score', ascending=False).head(top_n)
        title = f'Top {top_n} States by Mobility Score'
        metric_col = 'Mobility Score'
    else:
        sorted_data = state_summary.sort_values('ai_exposure', ascending=True).head(top_n)
        title = f'Top {top_n} States by AI Protection (Lowest Exposure)'
        metric_col = 'AI Exposure'
    
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['<b>Rank</b>', '<b>State</b>', f'<b>{metric_col}</b>', '<b>Counties</b>'],
            fill_color='#1f77b4',
            font=dict(color='white', size=12),
            align='left'
        ),
        cells=dict(
            values=[
                list(range(1, len(sorted_data) + 1)),
                sorted_data['state_name'].tolist(),
                [f'{val:.3f}' for val in sorted_data[metric].tolist()],
                sorted_data['num_counties'].tolist()
            ],
            fill_color='lavender',
            align='left',
            font=dict(size=11)
        )
    )])
    
    fig.update_layout(
        title=title,
        height=400,
        margin=dict(l=0, r=0, t=40, b=0),
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig


# =============================================================================
# DASH APP INITIALIZATION
# =============================================================================

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
    suppress_callback_exceptions=True
)

app.title = "Mobility-AI Displacement Dashboard"

# =============================================================================
# APP LAYOUT
# =============================================================================

app.layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H1("📊 Economic Mobility & AI Displacement Analysis", 
                   className="text-primary mb-2"),
            html.P("Interactive dashboard exploring the relationship between economic mobility and AI-driven job displacement risk across U.S. counties",
                  className="lead text-muted"),
            html.Hr()
        ])
    ], className="mt-4 mb-3"),
    
    # KPI Cards
    html.Div(id='kpi-cards'),
    
    # Main Content - Row 1: Map and Controls
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5("🗺️ Geographic Visualization", className="mb-0"),
                ]),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Label("Select Metric:", className="fw-bold"),
                            dcc.Dropdown(
                                id='map-metric-dropdown',
                                options=[
                                    {'label': '📍 County Classification', 'value': 'category'},
                                    {'label': '📈 Mobility Score', 'value': 'mobility_score'},
                                    {'label': '🤖 AI Exposure', 'value': 'ai_exposure'}
                                ],
                                value='category',
                                clearable=False
                            )
                        ], width=12)
                    ], className="mb-3"),
                    dcc.Graph(id='choropleth-map', config={'displayModeBar': False})
                ])
            ], className="shadow-sm")
        ], width=12, lg=8),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5("📋 State Rankings", className="mb-0"),
                ]),
                dbc.CardBody([
                    dcc.Dropdown(
                        id='ranking-metric-dropdown',
                        options=[
                            {'label': '📈 By Mobility Score', 'value': 'mobility_score'},
                            {'label': '🛡️ By AI Protection', 'value': 'ai_exposure'}
                        ],
                        value='mobility_score',
                        clearable=False,
                        className="mb-3"
                    ),
                    dcc.Graph(id='state-ranking-table', config={'displayModeBar': False})
                ])
            ], className="shadow-sm")
        ], width=12, lg=4)
    ], className="mb-4"),
    
    # Main Content - Row 2: Scatter Plot
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5("📉 Correlation Analysis", className="mb-0"),
                ]),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Label("Analysis Level:", className="fw-bold"),
                            dcc.RadioItems(
                                id='scatter-level-radio',
                                options=[
                                    {'label': ' State-Level', 'value': 'state'},
                                    {'label': ' County-Level', 'value': 'county'}
                                ],
                                value='state',
                                inline=True,
                                className="mb-2"
                            )
                        ], width=6),
                        dbc.Col([
                            html.Label("Select State (County-Level only):", className="fw-bold"),
                            dcc.Dropdown(
                                id='state-dropdown',
                                options=[{'label': state, 'value': state} 
                                        for state in sorted(merged_data['state_name'].unique())],
                                value='California',
                                clearable=False,
                                disabled=True
                            )
                        ], width=6)
                    ]),
                    dcc.Graph(id='scatter-plot')
                ])
            ], className="shadow-sm")
        ], width=12)
    ], className="mb-4"),
    
    # Main Content - Row 3: Distribution Charts
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5("📊 Mobility Distribution", className="mb-0"),
                ]),
                dbc.CardBody([
                    dcc.Graph(id='mobility-distribution', figure=create_distribution_plots(),
                             config={'displayModeBar': False})
                ])
            ], className="shadow-sm")
        ], width=12, md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5("📊 AI Exposure Distribution", className="mb-0"),
                ]),
                dbc.CardBody([
                    dcc.Graph(id='ai-distribution', figure=create_ai_distribution_plot(),
                             config={'displayModeBar': False})
                ])
            ], className="shadow-sm")
        ], width=12, md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5("📊 Category Breakdown", className="mb-0"),
                ]),
                dbc.CardBody([
                    dcc.Graph(id='category-breakdown', figure=create_category_breakdown(),
                             config={'displayModeBar': False})
                ])
            ], className="shadow-sm")
        ], width=12, md=4)
    ], className="mb-4"),
    
    # Footer
    dbc.Row([
        dbc.Col([
            html.Hr(),
            html.P([
                "Data Sources: Opportunity Insights (County Trends) & Economic Census (AIOE Data) | ",
                html.A("GitHub", href="#", className="text-decoration-none"),
            ], className="text-center text-muted small")
        ])
    ], className="mb-4")
    
], fluid=True, style={'backgroundColor': '#f8f9fa'})


# =============================================================================
# CALLBACKS
# =============================================================================

@app.callback(
    Output('kpi-cards', 'children'),
    Input('map-metric-dropdown', 'value')
)
def update_kpis(metric):
    return create_kpi_cards()


@app.callback(
    Output('choropleth-map', 'figure'),
    Input('map-metric-dropdown', 'value')
)
def update_map(selected_metric):
    return create_choropleth_map(selected_metric)


@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('scatter-level-radio', 'value'),
     Input('state-dropdown', 'value')]
)
def update_scatter(level, selected_state):
    if level == 'state':
        return create_scatter_plot(level='state')
    else:
        return create_scatter_plot(level='county', selected_state=selected_state)


@app.callback(
    Output('state-dropdown', 'disabled'),
    Input('scatter-level-radio', 'value')
)
def toggle_state_dropdown(level):
    return level == 'state'


@app.callback(
    Output('state-ranking-table', 'figure'),
    Input('ranking-metric-dropdown', 'value')
)
def update_ranking_table(metric):
    return create_state_ranking_table(metric=metric)


# =============================================================================
# RUN APP
# =============================================================================

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 LAUNCHING INTERACTIVE DASHBOARD")
    print("="*70)
    print("📊 Dashboard Features:")
    print("   • 5 Interactive KPI Cards")
    print("   • Geographic Choropleth Map")
    print("   • State/County-Level Scatter Analysis")
    print("   • Distribution Histograms")
    print("   • Category Breakdown Chart")
    print("   • State Rankings Table")
    print("\n🌐 Opening dashboard in your browser...")
    print("   URL: http://127.0.0.1:8050/")
    print("   Press CTRL+C to stop the server")
    print("="*70 + "\n")
    
    app.run(debug=True, port=8050)

