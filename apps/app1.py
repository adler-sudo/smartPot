from components.functions import *


vital = 'temperature'

layout1 = html.Div([
    generate_graph(vital),
    basic_table()
])

layout2 = html.Div([
    generate_summary_stats(df, vital)
])

