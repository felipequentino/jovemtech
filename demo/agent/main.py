from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

def flip_string(text):
    return text[::-1]
# hello
# olleh

@app.post("/process")
async def process_ai(data: Message):
    # Simula a lógica de um agente de IA
    response_text = f"O Agente IA processou: {flip_string(data.text)}" 
    return {"reply": response_text}

@app.get("/")
async def home():
    return {"response": "oiiii"}



if __name__ == "__main__":
    # sempre verdade
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

# 255.1.0.27:8000
# 255.1.0.27:3000
# 255.1.0.27:5432 
# 255.1.0.27:8080
# 