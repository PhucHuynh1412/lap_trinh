import mplfinance as mpf
import pandas as pd

# Đọc dữ liệu từ tập tin CSV
data = pd.read_csv('stock_prices.csv', index_col=0, parse_dates=True)

# Tạo biểu đồ nến liên tục
mpf.plot(data, type='candle', style='charles', volume=True, show_nontrading=True)

