import yfinance as yf

def get_stock_data(ticker: str) -> dict:
    stock = yf.Ticker(ticker)
    info = stock.info # da pra usar o info mas ele parece mais devagar

    # Preço e dados de mercado

    price_data = {
        "ticker": ticker.upper(),
        "nome": info.get("longName", "N/A"),
        "preco_atual": info.get("regularMarketPrice", "N/A"),
        "variacao_52s_max": info.get("fiftyTwoWeekHigh", "N/A"),
        "variacao_52s_min": info.get("fiftyTwoWeekLow", "N/A"),
        "market_cap": info.get("marketCap", "N/A"),
        "volume": info.get("regularMarketVolume", "N/A"),
        "media_50d": info.get("fiftyDayAverage", "N/A"),
        "media_200d": info.get("twoHundredDayAverage", "N/A"),
    }

    # indicadores
    fundamentals = {
        "p_l": info.get("trailingPE", "N/A"),
        "p_vp": info.get("priceToBook", "N/A"),
        "roe": info.get("returnOnEquity", "N/A"),
        "roa": info.get("returnOnAssets", "N/A"),
        "divida_total": info.get("totalDebt", "N/A"),
        "caixa_total": info.get("totalCash", "N/A"),
        "receita": info.get("totalRevenue", "N/A"),
        "lucro_liquido": info.get("netIncomeToCommon", "N/A"),
        "margem_lucro": info.get("profitMargins", "N/A"),
        "margem_operacional": info.get("operatingMargins", "N/A"),
        "dividend_yield": info.get("dividendYield", "N/A"),
        "ebitda": info.get("ebitda", "N/A"),
        "crescimento_receita": info.get("revenueGrowth", "N/A"),
        "crescimento_lucro": info.get("earningsGrowth", "N/A"),
        "recomendacao_analistas": info.get("averageAnalystRating", "N/A"),
        "preco_alvo_medio": info.get("targetMeanPrice", "N/A"),
        "setor": info.get("sector", "N/A"),
        "industria": info.get("industry", "N/A"),
    }

    # noticias

    news = []
    for item in stock.news[:5]:
        content = item.get("content", {})
        news.append({
            "titulo": content.get("title", "N/A"),
            "resumo": content.get("summary", "N/A"),
        })
    return {
        "price_data": price_data,
        "fundamentals": fundamentals,
        "news": news,
    }