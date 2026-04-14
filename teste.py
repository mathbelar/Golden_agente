from backend.data_search import get_stock_data
import json

data = get_stock_data("AAPL")
print(json.dumps(data, indent=2, ensure_ascii=False))