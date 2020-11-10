import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table as dt
import pandas as pd
import plotly.express as px
import json

from app import app


# OBJECTS

# dataframes
df = pd.read_csv('data/tempData.csv', parse_dates=['timestamp'])

# temperature dataframes
dft = df[['timestamp', 'temperature']]
temp_mean = round(dft.temperature.mean(), 1)
temp_high = dft.temperature.max()
temp_low = dft.temperature.min()

temp_stats = {
    'Average': [temp_mean],
    'High': [temp_high],
    'Low': [temp_low]
}

dfts = pd.DataFrame(data=temp_stats)


# humidity dataframes
dfh = df[['timestamp', 'humidity']]
hum_mean = round(dfh.humidity.mean(), 1)
hum_high = dfh.humidity.max()
hum_low = dfh.humidity.min()

hum_stats = {
    'Average': [hum_mean],
    'High': [hum_high],
    'Low': [hum_low]
}

dfhs = pd.DataFrame(data=hum_stats)


# figures
# temperature figures
figt = px.scatter(df,
                  x="timestamp",
                  y="temperature",
                  color="temperature",
                  title="Temperature by time",
                  color_continuous_scale='Reds'
                  )

figt.update_layout(
    {'plot_bgcolor': 'rgba(0,0,0,0)'},
    font=dict(
        family="Verdana",
        size=14,
        color='black',
    ),
    coloraxis_showscale=False
)

# humidity figures
figh = px.scatter(df,
                  x="timestamp",
                  y="humidity",
                  color="humidity",
                  title="Humidity by time",
                  color_continuous_scale='Blues'
                  )

figh.update_layout(
    {'plot_bgcolor': 'rgba(0,0,0,0)'},
    font=dict(
        family="verdana",
        size=14,
        color='black'
    ),
    coloraxis_showscale=False
)



# application layout
app.layout = html.Div(
    id="main",
    children=[
        html.Div(
            id="header",
            children=[
            html.H1("Welcome to smartPot",
                    style={
                        'marginBottom': 0
                    })
                ]
        ),

        html.Div(
            id="sub-header",
            children=[
                html.H5("A comprehensive plant management application",
                        style={
                            'marginTop': 0
                        })
            ],
        ),

        html.Div(
            id="links"
        ),

        html.Div(
            id="core-elements",
            children=[


# TEMPERATURE DIV
                html.Div(
                    id="temperature-div",
                    style={
                        'marginBottom': 25,
                        'marginTop': 25,
                        'marginLeft': 15,
                        'marginRight': 15,
                        'border': '1px black solid',
                        'width': '47%',
                        'display': 'inline-block'
                    },
                    children=[
                        html.H2('Temperature'),
                        html.Div(
                            id="temperature-stats",
                            children=[
                                dt.DataTable(
                                    id="temperature-summary-table",
                                    style_header={
                                        'fontWeight': 'bold'
                                    },
                                    style_table={
                                    },
                                    style_cell={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                        'fontSize': 16,
                                        'font-family': 'Verdana',
                                        'textAlign': 'center',
                                        'minWidth': '50px', 'width': '50px', 'maxWidth': '50px'
                                    },
                                    fixed_rows={'headers': True},
                                    columns=[{"name": i, "id": i} for i in dfts.columns],
                                    data=dfts.to_dict('records')
                                )
                            ]
                        ),

                        dcc.Graph(
                            id="temperature-graph",
                            figure=figt
                        ),

                        dt.DataTable(
                            id="temperature-raw-data",
                            style_header={
                                'fontWeight': 'bold'
                            },
                            style_table={
                                'height': '300px',
                                'overflowY': 'auto',
                                'marginTop': 50
                            },
                            style_cell={
                                'whiteSpace': 'normal',
                                'height': 'auto',
                                'fontSize': 12,
                                'font-family': 'Verdana',
                                'textAlign': 'left',
                                'minWidth': '50px', 'width': '50px', 'maxWidth': '50px'
                            },
                            fixed_rows={'headers': True},
                            columns=[{"name": i, "id": i} for i in dft.columns],
                            data=dft.to_dict('records')
                        )
                    ],
                ),


# HUMIDITY DIV
                html.Div(
                    id="humidity-div",
                    style={
                        'marginBottom': 25,
                        'marginTop': 25,
                        'marginRight': 15,
                        'marginLeft': 15,
                        'border': '1px black solid',
                        'width': '47%',
                        'display': 'inline-block'
                    },
                    children=[
                        html.H2("Humidity"),
                        html.Div(
                            id="humidity-stats",
                            children=[
                                dt.DataTable(
                                    id="humidity-summary-table",
                                    style_header={
                                        'fontWeight': 'bold'
                                    },
                                    style_table={
                                    },
                                    style_cell={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                        'fontSize': 16,
                                        'font-family': 'Verdana',
                                        'textAlign': 'center',
                                        'minWidth': '50px', 'width': '50px', 'maxWidth': '50px'
                                    },
                                    columns=[{"name": i, "id": i} for i in dfhs.columns],
                                    data=dfhs.to_dict('records')
                                )
                            ]
                        ),

                        dcc.Graph(
                            id="humidity-graph",
                            figure=figh
                        ),

                        dt.DataTable(
                            id="humidity-raw-data",
                            style_header={
                                'fontWeight': 'bold'
                            },
                            style_table={
                                'height': '300px',
                                'overflowY': 'auto',
                                'marginTop': 50
                            },
                            style_cell={
                                'whiteSpace': 'normal',
                                'height': 'auto',
                                'fontSize': 12,
                                'font-family': 'Verdana',
                                'textAlign': 'left',
                                'minWidth': '50px', 'width': '50px', 'maxWidth': '50px'
                            },
                            fixed_rows={'headers': True},
                            columns=[{"name": i, "id": i} for i in dfh.columns],
                            data=dfh.to_dict('records')
                        )
                    ]
                )
                ]
        )
    ]
)



# CALLBACKS
# update temperature raw data table when zoom in on graph
@app.callback(
    [Output('temperature-raw-data', 'data'),
     Output('temperature-summary-table', 'data')],
    [Input('temperature-graph', 'relayoutData')])
def temperature_table_adjust(relayoutData):
    try:
        dft_copy = dft.copy()

        xmin = relayoutData['xaxis.range[0]']
        xmax = relayoutData['xaxis.range[1]']

        mask = (dft_copy['timestamp'] > xmin) & (dft_copy['timestamp'] < xmax)

        dft_copy = dft_copy.loc[mask]

    except (TypeError, KeyError):
        dft_copy = dft.copy()

    data = dft_copy.to_dict('records')

    # may make more sense in future to split this up into its own callback?
    temp_mean = round(dft_copy.temperature.mean(), 1)
    temp_high = dft_copy.temperature.max()
    temp_low = dft_copy.temperature.min()

    temp_stats_copy = temp_stats.copy()

    temp_stats_copy['Average'] = [temp_mean]
    temp_stats_copy['High'] = [temp_high]
    temp_stats_copy['Low'] = [temp_low]

    data_sums_pd = pd.DataFrame(data=temp_stats_copy)
    data_sums = data_sums_pd.to_dict('records')

    return data, data_sums


# update temperature raw data table when zoom in on graph
@app.callback(
    [Output('humidity-raw-data', 'data'),
    Output('humidity-summary-table', 'data')],
    [Input('humidity-graph', 'relayoutData')])
def humidity_table_adjust(relayoutData):
    try:
        dfh_copy = dfh.copy()

        xmin = relayoutData['xaxis.range[0]']
        xmax = relayoutData['xaxis.range[1]']

        mask = (dfh_copy['timestamp'] > xmin) & (dfh_copy['timestamp'] < xmax)

        dfh_copy = dfh_copy.loc[mask]

    except (TypeError, KeyError):
        dfh_copy = dfh.copy()

    data = dfh_copy.to_dict('records')

    # may make more sense in future to split this up into its own callback?
    hum_mean = round(dfh_copy.humidity.mean(), 1)
    hum_high = dfh_copy.humidity.max()
    hum_low = dfh_copy.humidity.min()

    hum_stats_copy = hum_stats.copy()

    hum_stats_copy['Average'] = [hum_mean]
    hum_stats_copy['High'] = [hum_high]
    hum_stats_copy['Low'] = [hum_low]

    data_sums_pd = pd.DataFrame(data=hum_stats_copy)
    data_sums = data_sums_pd.to_dict('records')

    return data, data_sums










# host on local network at 10.0.0.96:8050
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False)

# run locally
# if __name__ == '__main__':
#     app.run_server(debug=True)


