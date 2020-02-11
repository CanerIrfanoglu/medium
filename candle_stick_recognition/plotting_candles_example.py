from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./btc_data.csv')

o = df['open'].astype(float)
h = df['high'].astype(float)
l = df['low'].astype(float)
c = df['close'].astype(float)

trace = go.Candlestick(
            open=o,
            high=h,
            low=l,
            close=c)
data = [trace]

plot(data, filename='go_candle1.html')

