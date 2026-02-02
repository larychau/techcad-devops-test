from fastapi import FastAPI
from pydantic import BaseModel
from model import DummyModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
model = DummyModel()

class CADParams(BaseModel):
    complexity: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(params: CADParams):
    score = model.predict(params.complexity)
    return {"tech_score": score}

Instrumentator().instrument(app).expose(app)
