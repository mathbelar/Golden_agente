import sys
sys.path.insert(0, "backend")

from agent import analyze_stock

result = analyze_stock("AAPL")
print(result)