from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict

app = FastAPI()

origins = [
    "http://localhost:5173",  # Vite default
    "http://localhost:3000",  # CRA default (keep if needed)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    features : list[float]

@app.post("/predict")
def pred_api(data : InputData):
    return predict(data.features)

@app.get("/stat")
def stat():
    return {"status":"running"}

