# Golden_agente


Agente de análise de investimentos com IA. Dado um ticker de ação, o agente coleta dados de mercado, indicadores fundamentalistas e notícias recentes, e gera um relatório completo com recomendação de compra, espera ou venda.

---

## Como funciona

1. Usuário digita o ticker (ex: `AAPL`, `VALE3`)
2. O backend busca dados em tempo real via `yfinance`
3. Os dados são enviados para um LLM (GPT-4o mini via GitHub Models)
4. O agente retorna um relatório estruturado com análise e recomendação

---

## Stack

| Camada | Tecnologia |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| Dados de mercado | yfinance |
| LLM | GPT-4o mini (GitHub Models) |

---

##  Como rodar localmente

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/investment-agent.git
cd investment-agent
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure o `.env`
Crie um arquivo `.env` na raiz com:

> Gere seu token gratuito em [GitHub Models](https://github.com/marketplace/models) aqui você pode escolher o modelo que prefere, desse modo altere o modelo em model="gpt-4o-mini",

### 4. Inicie o backend
```bash
uvicorn backend.main:app --reload
```

### 5. Abra o frontend
Abra o arquivo `frontend/index.html` no navegador.


---

## Exemplo de uso

Digite um ticker como `VALE3` ou `AAPL` e clique em **Analisar**. O agente retorna:

- 📊 Visão Geral
- ✅ Pontos Positivos
- ⚠️ Riscos
- 📈 Valuation
- 🏁 Recomendação (COMPRAR / AGUARDAR / EVITAR)