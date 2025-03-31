import spacy
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import string
from typing import Dict, List, Union

nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

def analyze_sentiment(text: str) -> Dict[str, Union[str, float]]:
    """Analyze text sentiment using TextBlob"""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    return {
        "sentiment": sentiment,
        "polarity": polarity,
        "subjectivity": subjectivity
    }

def extract_keywords(text: str, top_n: int = 5) -> List[Dict[str, float]]:
    """Extract keywords using TF-IDF"""
    def preprocess(text):
        tokens = word_tokenize(text.lower())
        return [t for t in tokens if t not in stop_words and t not in string.punctuation]
    
    processed_text = " ".join(preprocess(text))
    vectorizer = TfidfVectorizer(max_features=top_n)
    X = vectorizer.fit_transform([processed_text])
    features = vectorizer.get_feature_names_out()
    scores = X.toarray()[0]
    
    return [{"word": word, "score": float(score)} 
            for word, score in zip(features, scores)]

def extract_entities(text: str) -> List[Dict[str, str]]:
    """Extract named entities using spaCy"""
    doc = nlp(text)
    return [{"text": ent.text, "label": ent.label_} 
            for ent in doc.ents]