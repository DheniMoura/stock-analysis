import pandas as pd
import matplotlib.pyplot as plt
from stastmodels.tsa.seasonal import seasonal_decompose
import yfinance as yf

ticket = yf.Ticker('ABEV')
# df = ticket.history(period='3y', insterval='1mo')
df = ticket.history(interval='1d', start='2018-01-01', end='2022-01-01')