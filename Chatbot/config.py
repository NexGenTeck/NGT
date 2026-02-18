"""
Configuration module for the NexGenTeck AI Chatbot.
Loads environment variables and provides centralized configuration.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Centralized configuration for the chatbot backend."""
    
    # API Keys
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    
    # Website Configuration
    WEBSITE_URL: str = os.getenv("WEBSITE_URL", "https://nexgenteck.com")
    # When enabled, scraper can ingest from local translation files.
    # Keep disabled in production to avoid stale local content overriding live site data.
    USE_TRANSLATION_EXTRACTOR: bool = os.getenv("USE_TRANSLATION_EXTRACTOR", "false").lower() == "true"
    
    # CORS Configuration - Restricted to production and local development
    # Override via environment variable for specific deployments
    CORS_ORIGINS: list = os.getenv(
        "CORS_ORIGINS", 
        "https://nexgenteck.github.io,https://muhammadhasaan82.github.io,https://nexgenteck.com,http://localhost:5173,http://localhost:3000"
    ).split(",")
    
    # Model Configuration
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "BAAI/bge-m3")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")
    
    # RAG Configuration
    MAX_CONTEXT_DOCS: int = int(os.getenv("MAX_CONTEXT_DOCS", "5"))
    RELEVANCE_THRESHOLD: float = float(os.getenv("RELEVANCE_THRESHOLD", "1.5"))

    # Re-ranking Configuration
    # Cross-encoder re-ranks a wider candidate pool down to MAX_CONTEXT_DOCS,
    # giving the LLM a tighter, higher-signal context window.
    ENABLE_RERANKING: bool = os.getenv("ENABLE_RERANKING", "true").lower() == "true"
    RERANK_MODEL: str = os.getenv("RERANK_MODEL", "cross-encoder/ms-marco-MiniLM-L-6-v2")
    # Fetch this many candidates from Qdrant, then re-rank down to MAX_CONTEXT_DOCS
    RERANK_CANDIDATE_DOCS: int = int(os.getenv("RERANK_CANDIDATE_DOCS", "25"))

    # LLM Parameters
    LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", "0.7"))
    LLM_MAX_TOKENS: int = int(os.getenv("LLM_MAX_TOKENS", "1024"))
    
    # Qdrant Configuration (in-memory by default)
    QDRANT_URL: str = os.getenv("QDRANT_URL", ":memory:")
    COLLECTION_NAME: str = os.getenv("COLLECTION_NAME", "nexgenteck_knowledge")
    
    @classmethod
    def validate(cls) -> bool:
        """Validate that required configuration is present."""
        if not cls.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY environment variable is required")
        return True


# Create a singleton config instance
config = Config()
