import yfinance

netflix = yfinance.Ticker('XKRX')
netflix_info = netflix.info
print(netflix_info['regularMarketPrice'])
