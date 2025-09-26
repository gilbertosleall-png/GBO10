# Protótipo de backend FastAPI
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def home():
    return {"msg": "API Balanceador pronta"}