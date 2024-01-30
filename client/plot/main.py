import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import random, wave 
import numpy as np 
import plotly.express as px 
# Initialize the Dash app
# app = dash.Dash(__name__)

# # Define the layout of the app

# app.layout = html.Div([
#     html.H4('Stock price analysis'),
#     dcc.Graph(id="time-series-chart"),
# ])

spf = wave.open("./plot/adc+1706187291.4861112.wav", "r")
signal = spf.readframes(-1)
signal = np.fromstring(signal, dtype=int)
fs = spf.getframerate()
Time = np.linspace(0, len(signal) / fs, num=len(signal))

# print(len(signal), fs)


# # Callback function to update the graph

# @app.callback()
# def display_time_series(ticker):
#    #  df = px.data.stocks() # replace with your own data source
#     fig = px.line(df, x='date', y=ticker)
#     return fig

# if __name__ == "__main__":
#    app.run_server(debug=True, port=8051)

# import plotly.express as px
# fig = px.line(x=Time, y=signal)
# fig.show()