import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table as dt
import pandas as pd
import plotly.express as px
import json
import sqlite3

from app import app, db


server = app.server


# define database models ( will be moved to models.py once we get this working)
class Environment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime)
	temperature = db.Column(db.Float)
	humidity = db.Column(db.Float)

	def __repr__(self):
		return '<Temperature {}>'.format(self.temperature)


# intermediate step in our transition from csv to db (will go away once we clean
# this up a bit)
conn = sqlite3.connect('smartPot.db')
sql = "SELECT * FROM environment"
df = pd.read_sql(sql, con=conn, parse_dates=['timestamp'])








# OBJECTS

# dataframes (going away for now as we make the transition to database) (DOES SEEM TO BE WORKING)
# df = pd.read_csv('/home/pi/secondDashing/data/tempData.csv', parse_dates=['timestamp'])
df.sort_values('timestamp', inplace=True)

# temperature dataframes (commenting out for now to see if we can work just from callback)
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
                        ),
                        dcc.Interval(
                            id='temperature-interval',
                            interval= 5*60*1000, # 5 minutes by 60 seconds by 1000 millisecons
                            n_intervals=0
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
                        )
                    ]
                )
                ]
        ),
        html.Div(
	    id='intermediate-value',
            style={'display': 'none'}
       )
    ]
)



# testing the interval dcc component
# will transition this into the other callbacks once we  confirm functionality
@app.callback(
    [Output('intermediate-value', 'children'),
     Output('temperature-raw-data', 'data'),
     Output('temperature-graph', 'figure'),
     Output('humidity-raw-data', 'data'),
     Output('humidity-graph', 'figure')],
    Input('temperature-interval', 'n_intervals'))
def update_data(n):
    # read in up to date data
    conn = sqlite3.connect('smartPot.db')
    sql = "SELECT * FROM environment"
    df = pd.read_sql(sql, con=conn, parse_dates=['timestamp'])

    # prep hidden dataset
    datasets = {
        'df': df.to_json(orient='split', date_format='iso')
    }

    # dataframes
    dft = df[['timestamp', 'temperature']]
    dfh = df[['timestamp', 'humidity']]

    # figures
    figt = px.scatter(dft, x='timestamp', y='temperature')
    figh = px.scatter(dfh, x='timestamp', y='humidity')


    return json.dumps(datasets), dft.to_dict('records'), figt, dfh.to_dict('records'), figh









# host on local network at <server IP>:8050
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False)

# run locally
# if __name__ == '__main__':
#     app.run_server(debug=True)


