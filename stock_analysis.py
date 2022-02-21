import pandas as pd
import matplotlib.pyplot as plt
from stastmodels.tsa.seasonal import seasonal_decompose
import yfinance as yf

ticket = yf.Ticker('ABEV')
# df = ticket.history(period='3y', insterval='1mo')
df = ticket.history(interval='1d', start='2018-01-01', end='2022-01-01')

# Instalação e importação de biblioecas


import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import yfinance as yf

# Coleta de dados

ticket = yf.Ticker('^BVSP')
df = ticket.history(interval='1d', start='2020-01-01', end='2022-01-01')

df.tail() #mostra as últimas linhas

df[['Close']].info()

df[['Close']].head() #mostra as primeiras linhas

df[['Close']].plot()

Decomposição temporal (modelo aditivo / modelo multiplicativo)

decomposicao = seasonal_decompose(df[['Close']], model='additive', period=30, extrapolate_trend=30)

decomposicao.plot()

decomposicao_multi = seasonal_decompose(df[['Close']], model='multiplicative', period=30, extrapolate_trend=30)

decomposicao_multi.plot()

max(decomposicao.resid)

No gráfico a seguir a linha azul é referente ao valor do ticker, enquanto a linha laranja é a linha de tendência

ax, fig = plt.subplots(figsize=(15,8))

plt.plot(decomposicao.observed)

plt.plot(decomposicao.trend)

fig,(ax1,ax2,ax3,ax4) = plt.subplots(4,1, figsize=(12,8))

decomposicao.observed.plot(ax=ax1)

decomposicao.trend.plot(ax=ax2)

decomposicao.seasonal.plot(ax=ax3)

decomposicao.resid.plot(ax=ax4)

plt.tight_layout() #Serve para melhorar um pouco o layout de apresentação

Cálculo de média móvel

df['Close'].rolling(7).mean() #o método rolling faz a média móvelna janela de tempo determinada

media_movel9d = df['Close'].rolling(9).mean()

media_movel20d = df['Close'].rolling(20).mean()

media_movel50d = df['Close'].rolling(50).mean()

fig, ax = plt.subplots(figsize=(12,5))

plt.plot(media_movel9d, 'orange')

plt.plot(media_movel20d, 'red')

plt.plot(media_movel50d, 'black')

plt.plot(df['Close'])

Extração de features

df.head()

df.reset_index(inplace=True)

df.head()

# Criar features para cada período

df['year'] = df['Date'].dt.year

df['month'] = df['Date'].dt.month

df['day'] = df['Date'].dt.day

df.head()