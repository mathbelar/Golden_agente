from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from agent import analyze_stock

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#json esperado, no caso so ta esperando o ticker
class TickerRequest(BaseModel):
    ticker: str

@app.post("/analyze")
async def analyze(request: TickerRequest):
    report = analyze_stock(request.ticker)
    return {"report": report}