from fastapi import FastAPI, HTTPException
from .models import analyze_sentiment, extract_keywords, extract_entities
from .schemas import TextInput, SentimentResponse, KeywordsResponse, EntitiesResponse

app = FastAPI(
    title="NLP API",
    description="API for text analysis including sentiment analysis, keyword extraction, and entity recognition",
    version="1.0.0"
)

@app.post("/sentiment", response_model=SentimentResponse)
async def get_sentiment(input_data: TextInput):
    try:
        return analyze_sentiment(input_data.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/keywords", response_model=KeywordsResponse)
async def get_keywords(input_data: TextInput, top_n: int = 5):
    try:
        return {"keywords": extract_keywords(input_data.text, top_n)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/entities", response_model=EntitiesResponse)
async def get_entities(input_data: TextInput):
    try:
        return {"entities": extract_entities(input_data.text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the NLP API. Use /docs for documentation."}