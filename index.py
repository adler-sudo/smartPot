import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table as dt

from app import app
from apps import app1, app2

from components.functions import df


app.layout = html.Div([
    html.Div([
        html.H1('Welcome to the smartPot',
                style={'width': '80%', 'display': 'inline-block'}),
        html.Div(
            id='page-content2',
            style={'height': '4em', 'width': '20%', 'vertical-align': 'middle', 'display': 'inline-block'}
        ),
        html.Div([
            html.H3('Dive into a vital sign'),
            dcc.Link('Temperature', href='/app1'),
            html.Br(),
            dcc.Link('Humidity', href='/app2'),
            ]
        )
        ]
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(
        id='page-content'
    )
])


@app.callback([Output('page-content', 'children'),
               Output('page-content2', 'children')],
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app1':
        return app1.layout1, app1.layout2
    elif pathname == '/app2':
        return app2.layout1, app2.layout2


@app.callback(
    Output('table1', 'children'),
    [Input('basic-interactions', 'relayoutData')])
def update_table(relayoutData):
    try:
        xmin = relayoutData['xaxis.range[0]']
        xmax = relayoutData['xaxis.range[1]']
        mask = (df['timestamp'] > xmin) & (df['timestamp'] < xmax)
        dff = df.loc[mask]
    except (TypeError, KeyError):
        dff = df

    data = dff.to_dict('rows')
    columns = [{"name": i, "id": i} for i in (dff.columns)]

    return dt.DataTable(
        data=data,
        columns=columns,
        style_table={
            'height': 300,
            'overflowY': 'scroll'
        }
    )



if __name__ == '__main__':
    app.run_server(debug=True)