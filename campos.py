import yfinance as yf

stock = yf.Ticker("AAPL")
info = stock.info
for key in sorted(info.keys()):
    print(f"{key}: {info[key]}")