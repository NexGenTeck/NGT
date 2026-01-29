# NexGenTeck Chatbot Backend

A FastAPI-based AgenticRAG chatbot backend for NexGenTeck, featuring intelligent intent detection and lead generation.

## Features

- **AgenticRAG Pipeline**: Retrieval-Augmented Generation using Qdrant vector store
- **Lead Generation**: Automatic detection of contact/hire intent
- **Sentiment Analysis**: Hybrid RoBERTa + LLM sentiment/intent analysis
- **Fast Inference**: Llama 3.3 70B via Groq for high-speed responses

## Tech Stack

- **Framework**: FastAPI
- **Vector Store**: Qdrant (in-memory or external)
- **Embeddings**: BAAI/bge-m3
- **LLM**: Llama 3.3 70B via Groq
- **Sentiment**: RoBERTa (transformers)

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   # or using uv
   uv sync
   ```

2. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

3. **Run the server**:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   # or using uv
   uv run uvicorn main:app --reload
   ```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check with document count |
| `/chat` | POST | Send a message and get AI response |
| `/reindex` | POST | Re-scrape website and update knowledge base |

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | Groq API key (required) | - |
| `WEBSITE_URL` | Website to scrape | `https://nexgenteck.com` |
| `CORS_ORIGINS` | Allowed origins | Production URLs |
| `QDRANT_URL` | External Qdrant URL | `:memory:` |

## Project Structure

```
Chatbot/
├── main.py          # FastAPI app & endpoints
├── config.py        # Configuration & environment
├── rag_pipeline.py  # AgenticRAG pipeline with LangGraph
├── sentiment.py     # Sentiment & intent analysis
├── vector_store.py  # Qdrant integration
├── embeddings.py    # BGE-M3 embedding model
├── scraper.py       # Website scraper
└── requirements.txt # Python dependencies
```

## License

MIT © NexGenTeck