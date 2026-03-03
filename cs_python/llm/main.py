import cv2 # opencv
from fastapi import FastAPI
from ultralytics import YOLO
from sentence_transformers import SentenceTransformer, util
import spacy
import google.generativeai as genai
from config import GEMINI_KEY

app = FastAPI()

# CONFIGURAÇÃO DOS MODELOS 
# NLP: Modelo em português
nlp = spacy.load("pt_core_news_sm")

# Busca Semântica: Modelo leve que roda local (CPU)
search_model = SentenceTransformer('all-MiniLM-L6-v2')

# Visão Computacional: YOLOv8 Nano (mais rápido)
vision_model = YOLO("yolov8n.pt")

# LLM: Configurar API Key do Gemini aqui
genai.configure(api_key=GEMINI_KEY)
llm_model = genai.GenerativeModel('gemini-2.0-flash')

# --- 2. ROTAS DA API (Integração com C#) ---

@app.get("/")
def home():
    return {"status": "Agente Python Online"}

@app.post("/nlp")
def extrair_entidades(texto: str):
    """Extrai nomes, locais e organizações de um texto."""
    doc = nlp(texto)
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    return {"texto": texto, "entidades": entidades}

@app.post("/busca")
def comparar_frases(frase1: str, frase2: str):
    """Calcula a similaridade semântica entre duas frases."""
    emb1 = search_model.encode(frase1)
    emb2 = search_model.encode(frase2)
    score = util.cos_sim(emb1, emb2)
    return {"similaridade": float(score[0][0])}

@app.post("/visao")
def detectar_objetos(caminho_imagem: str):
    """Detecta objetos em uma imagem usando YOLO."""
    results = vision_model(caminho_imagem)
    deteccoes = []
    for r in results:
        for box in r.boxes:
            nome = r.names[int(box.cls)]
            conf = float(box.conf)
            deteccoes.append({"objeto": nome, "confianca": conf})
    return {"deteccoes": deteccoes}

@app.post("/perguntar")
def perguntar_llm(pergunta: str):
    """Envia uma pergunta para o Gemini."""
    response = llm_model.generate_content(pergunta)
    return {"resposta": response.text}

# Para rodar: uvicorn nome_do_arquivo:app --reload