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


def get_destaques() -> list:
    candidates = [
        "VALE3.SA", "PETR4.SA", "ITUB4.SA", "WEGE3.SA", "EGIE3.SA",
        "AAPL", "NVDA", "MSFT"
    ]

    stocks_data = []
    for ticker in candidates:
        try:
            data = get_stock_data(ticker)
            # manda so o essencial
            stocks_data.append({
                "ticker": ticker.replace(".SA", ""),
                "nome": data["price_data"]["nome"],
                "preco_atual": data["price_data"]["preco_atual"],
                "p_l": data["fundamentals"]["p_l"],
                "roe": data["fundamentals"]["roe"],
                "crescimento_receita": data["fundamentals"]["crescimento_receita"],
                "crescimento_lucro": data["fundamentals"]["crescimento_lucro"],
                "margem_lucro": data["fundamentals"]["margem_lucro"],
                "recomendacao_analistas": data["fundamentals"]["recomendacao_analistas"],
                "preco_alvo_medio": data["fundamentals"]["preco_alvo_medio"],
            })
        except:
            continue

    prompt = f"""
Você é um analista de investimentos. Com base nos dados abaixo, escolha as 3 ações mais atrativas para investir agora.

Dados:
{json.dumps(stocks_data, indent=2, ensure_ascii=False)}

Responda APENAS em JSON válido, sem texto extra, neste formato:
[
  {{
    "ticker": "TICKER",
    "nome": "Nome da empresa",
    "motivo": "Motivo em 1 frase curta",
    "recomendacao": "COMPRAR"
  }}
]
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
    )

    import re
    text = response.choices[0].message.content
    text = re.sub(r"```json|```", "", text).strip()
    return json.loads(text)