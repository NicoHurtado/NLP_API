# NLP API

**Tech Stack:** FastAPI · spaCy · TextBlob · NLTK · scikit-learn

## Overview

NLP API is a RESTful service for performing Natural Language Processing (NLP) tasks, including:

- Sentiment Analysis
- Keyword Extraction (TF-IDF)
- Named Entity Recognition (NER)

Access the interactive documentation at `/docs`.

---

## Endpoints

### `POST /sentiment`

**Description:** Analyze sentiment using TextBlob.  
**Request Body:**

```json
{
  "text": "Your input text here"
}
```

**Response:**

```json
{
  "sentiment": "positive | negative | neutral",
  "polarity": float,
  "subjectivity": float
}
```

---

### `POST /keywords?top_n=5`

**Description:** Extract top-N keywords using TF-IDF.  
**Query Params:** `top_n` (default: 5)  
**Request Body:**

```json
{
  "text": "Your input text here"
}
```

**Response:**

```json
{
  "keywords": [
    { "word": "example", "score": 0.123 },
    ...
  ]
}
```

---

### `POST /entities`

**Description:** Extract named entities using spaCy.  
**Request Body:**

```json
{
  "text": "Your input text here"
}
```

**Response:**

```json
{
  "entities": [
    { "text": "Google", "label": "ORG" },
    ...
  ]
}
```

---

### `GET /`

Returns a welcome message and suggests using `/docs`.

---

## Installation

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Download NLTK Data

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## Run the API

```bash
uvicorn main:app --reload
```

---

## Dependencies

```
fastapi>=0.68.0
uvicorn>=0.15.0
spacy>=3.2.0
textblob>=0.15.3
nltk>=3.6.0
scikit-learn>=1.0.0
python-multipart>=0.0.5
```