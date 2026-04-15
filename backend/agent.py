import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from data_search import get_stock_data

load_dotenv()

client = OpenAI(base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN"),
)

def analyze_stock(ticker: str) -> str:
    data = get_stock_data(ticker)

    prompt = f"""
Você é um analista de investimentos experiente. Analise as informações abaixo sobre a ação {ticker} e gere um relatório completo em português.

# Dados de Mercado
{json.dumps(data["price_data"], indent=2, ensure_ascii=False)}

# Indicadores Fundamentalistas
{json.dumps(data["fundamentals"], indent=2, ensure_ascii=False)}

# Notícias Recentes
{json.dumps(data["news"], indent=2, ensure_ascii=False)}

---

Gere um relatório com exatamente estas seções:

**Visão Geral:**
Resumo da empresa e momento atual.

**Pontos Positivos:**
Liste os principais pontos fortes com base nos dados.

**Riscos:**
Liste os principais riscos e pontos de atenção.

**Valuation:**
Analise se o preço atual parece justo com base nos múltiplos.

**Recomendação:**
COMPRAR, AGUARDAR ou EVITAR — com justificativa clara e objetiva.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,
    )

    return response.choices[0].message.content
