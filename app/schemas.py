from pydantic import BaseModel
from typing import List, Dict, Union

class TextInput(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    polarity: float
    subjectivity: float

class KeywordsResponse(BaseModel):
    keywords: List[Dict[str, float]]

class EntitiesResponse(BaseModel):
    entities: List[Dict[str, str]]