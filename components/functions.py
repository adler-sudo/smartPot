import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px


df = pd.read_csv('data/tempData.csv', parse_dates=['timestamp'])
df = df[['timestamp', 'humidity', 'temperature']]
df.dropna(inplace=True)


def generate_table(dataframe, vital, max_rows=20):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe[['timestamp', vital]].columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe[['timestamp', vital]].columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


def basic_table():
    return html.Div(
        id='table1',
        style={'margin': '3vw'}
    )


def generate_graph(vital):
    fig = px.scatter(df, x='timestamp', y=vital, title='{} by time'.format(vital), trendline='ols')
    return dcc.Graph(
        id='basic-interactions',
        figure=fig
    )

def generate_summary_stats(dataframe, variable):
    return html.Div(
        id='summary-stats',
        children=[
            html.H4('{} stats'.format(variable)),
            html.P('Average: {:.1f}'.format(dataframe[variable].mean())),
            html.P('High: {:.1f}'.format(dataframe[variable].max())),
            html.P('Low: {:.1f}'.format(dataframe[variable].min()))
            ],
        style={'display': 'inline-block'}
    )