import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Set the stock symbol and download historical data from Yahoo Finance
symbol = "AAPL"
df = yf.download(symbol, start="2016-01-01", end="2022-02-16")

# Calculate the 20-day and 50-day moving averages
ma20 = df["Close"].rolling(window=20).mean()
ma50 = df["Close"].rolling(window=50).mean()

# Calculate the historical volatility over a 30-day period
log_returns = np.log(1 + df["Close"].pct_change())
volatility = log_returns.rolling(window=30).std() * np.sqrt(252)

# Plot the stock prices, moving averages, and volatility
plt.figure(figsize=(10, 6))
plt.plot(df["Close"])
plt.plot(ma20, label="MA20")
plt.plot(ma50, label="MA50")
plt.plot(volatility, label="Volatility")
plt.legend()
plt.title(f"{symbol} Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()