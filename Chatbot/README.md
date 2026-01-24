# NexGenTeck AI Chatbot Backend

A **fully softcoded** AI chatbot that uses LLM for intent interpretation and RoBERTa for sentiment analysis. No hardcoded regex patterns - the AI understands prompts dynamically.

## Features

- 🧠 **Hybrid Intelligence**: RoBERTa for sentiment + LLM for intent
- 🔍 **RAG Pipeline**: LangGraph orchestrates analyze → retrieve → generate
- 🌍 **Multilingual**: BAAI/bge-m3 embeddings support multiple languages
- � **Website Knowledge**: Auto-scrapes entire website for context
- � **GCP Ready**: Dockerfile for Cloud Run deployment

## Architecture

```
User Message
    ↓
┌───────────────────────────────────┐
│  RoBERTa Sentiment Analysis       │  ← Word-level understanding
│  (cardiffnlp/twitter-roberta)     │
└───────────────────────────────────┘
    ↓
┌───────────────────────────────────┐
│  LLM Intent Detection             │  ← Softcoded, no regex
│  (Llama 3.3 70B via Groq)         │
└───────────────────────────────────┘
    ↓
┌───────────────────────────────────┐
│  Qdrant Vector Search             │  ← Website knowledge
│  (BAAI/bge-m3 embeddings)         │
└───────────────────────────────────┘
    ↓
┌───────────────────────────────────┐
│  LLM Response Generation          │  ← Context-aware response
│  (Llama 3.3 70B via Groq)         │
└───────────────────────────────────┘
    ↓
Response
```

## Models Used

| Component | Model | Purpose |
|-----------|-------|---------|
| Embeddings | `BAAI/bge-m3` | Multilingual text embeddings (1024 dim) |
| Sentiment | `cardiffnlp/twitter-roberta-base-sentiment-latest` | Word-level sentiment analysis |
| LLM | `llama-3.3-70b-versatile` | Intent detection & response generation |

## Quick Start

### 1. Set Up Environment

```bash
cd Chatbot
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Locally

```bash
uvicorn main:app --reload --port 8000
```

### 4. Test the API

```bash
# Health check
curl http://localhost:8000/health

# Send a message
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'

# Ask a question
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What services does NexGenTeck offer?"}'
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Basic info and status |
| `/health` | GET | Health check for monitoring |
| `/chat` | POST | Send a message and get response |
| `/reindex` | POST | Re-scrape website and update knowledge |

## GCP Deployment

### Cloud Run

```bash
# Build and push to Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT/chatbot ./Chatbot

# Deploy to Cloud Run
gcloud run deploy chatbot \
  --image gcr.io/YOUR_PROJECT/chatbot \
  --platform managed \
  --region us-central1 \
  --set-env-vars GROQ_API_KEY=your_key \
  --allow-unauthenticated \
  --memory 4Gi \
  --cpu 2
```

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GROQ_API_KEY` | ✅ | - | Your Groq API key |
| `WEBSITE_URL` | ❌ | https://nexgenteck.com | URL to scrape |
| `EMBEDDING_MODEL` | ❌ | BAAI/bge-m3 | Embedding model |
| `LLM_MODEL` | ❌ | llama-3.3-70b-versatile | Groq model name |
| `LLM_TEMPERATURE` | ❌ | 0.7 | Response creativity |
| `MAX_CONTEXT_DOCS` | ❌ | 5 | Docs to retrieve |

## Project Structure

```
Chatbot/
├── main.py           # FastAPI application
├── config.py         # Environment configuration
├── sentiment.py      # RoBERTa + LLM hybrid analyzer
├── rag_pipeline.py   # LangGraph RAG workflow
├── scraper.py        # Comprehensive website scraper
├── embeddings.py     # BAAI/bge-m3 embedding manager
├── vector_store.py   # Qdrant operations
├── utils.py          # Text utilities
├── requirements.txt  # Python dependencies
├── Dockerfile        # GCP container config
└── .env.example      # Environment template
```

## How It Works (Softcoded)

1. **No Hardcoded Patterns**: Intent is detected by LLM, not regex
2. **RoBERTa Sentiment**: Uses word dictionary for accurate sentiment
3. **LLM Intent**: Understands "What services do you offer?" without patterns
4. **Website Context**: All responses based on scraped website content

## License

Proprietary - NexGenTeck © 2026
