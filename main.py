from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict
from RAG import rag_service
from autofill import parse_data

@asynccontextmanager
async def lifespan(app: FastAPI):
    rag_service.load_index()
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    features: list[float]

class RAGRequest(BaseModel):
    question: str

class InputData(BaseModel):
    features : list[float]

class ParseTextRequest(BaseModel):
    text: str

@app.post("/predict")
def pred_api(data : InputData):
    return predict(data.features)

@app.get("/stat")
def stat():
    return {"status":"running"}

@app.post("/rag/ask")
async def ask_rag(request: RAGRequest):
    """
    New endpoint for RAG queries.
    Expects JSON: { "question": "your question here" }
    """
    try:
        result = rag_service.ask(request.question)
        
        if "error" in result:
             raise HTTPException(status_code=500, detail=result["error"])
             
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/parse-text")
def parse_text(payload: ParseTextRequest):
    """
    Input:
    { "text": "age 32 bmi 26 blood pressure 130 over 85" }

    Output:
    { "parsed_fields": { ... } }
    """
    parsed = parse_data(payload.text)
    return {"parsed_fields": parsed}