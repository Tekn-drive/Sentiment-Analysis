from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = "model"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

class TextInput(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def to_lowercase(cls, v):
        return v.lower()

@app.post("/predict")
def predict(data: TextInput):
    inputs = tokenizer(data.text, return_tensors="pt", truncation=True, padding=True)

    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    prediction = torch.argmax(probs, dim=1).item()
    confidence = probs[0][prediction].item()
    sentiment_dictionary = {0: "sadness", 1: "neutral", 2:"anger", 3:"fear", 4:"joy"}
    return {"label": sentiment_dictionary[prediction], "confidence": confidence}