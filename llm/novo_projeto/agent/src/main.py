from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextoRequest(BaseModel):
    texto: str

@app.post("/nlp")
async def nlp(request: TextoRequest):
    entidades = f"Skills extraídas de: {request.texto[:50]}"
    return {"entidades": entidades}