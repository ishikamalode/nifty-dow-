!pip install yfinance --quiet

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")
start = "2021-01-01"
end = None   # Current date

tickers = { 
    "Dow Jones": "^DJI",
    "NASDAQ": "^IXIC",
    "NIFTY 50": "^NSEI"
}

# Fetching data
data = {name: yf.download(ticker, start=start, end=end) for name, ticker in tickers.items()}

# Display first rows of each
for name in data:
    print(f"\n--- {name} Data ---\n")
    display(data[name].head())
plt.figure(figsize=(12,14))

# Dow Jones
plt.subplot(3,1,1)
plt.plot(data["Dow Jones"]["Close"], label="Dow Jones", linewidth=2)
plt.title("Dow Jones Index (2021 - Present)")
plt.ylabel("Price")
plt.legend()

# NASDAQ
plt.subplot(3,1,2)
plt.plot(data["NASDAQ"]["Close"], color="orange", label="NASDAQ", linewidth=2)
plt.title("NASDAQ Index (2021 - Present)")
plt.ylabel("Price")
plt.legend()

# NIFTY 50
plt.subplot(3,1,3)
plt.plot(data["NIFTY 50"]["Close"], color="green", label="NIFTY 50", linewidth=2)
plt.title("NIFTY 50 Index (2021 - Present)")
plt.ylabel("Price")
plt.legend()

plt.tight_layout()
plt.show()
