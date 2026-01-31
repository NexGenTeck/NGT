"""
RAG Pipeline using LangGraph for the NexGenTeck AI Chatbot.
Fully softcoded - uses LLM for all interpretation.
The chatbot is trained on website content and uses that as context for all responses.
"""

from typing import Dict, List, TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import logging

from config import config
from vector_store import vector_store
from sentiment import llm_analyzer

logger = logging.getLogger(__name__)


class ChatState(TypedDict):
    """State for the RAG pipeline."""
    message: str
    analysis: Dict
    context: List[str]
    response: str
    error: str


async def analyze_message(state: ChatState) -> ChatState:
    """
    Analyze the user message using LLM.
    No hardcoded patterns - LLM determines intent and needs.
    
    Args:
        state: Current pipeline state
        
    Returns:
        Updated state with analysis
    """
    logger.info("Analyzing message with LLM")
    
    try:
        analysis = await llm_analyzer.analyze(state['message'])
        state['analysis'] = analysis
        logger.info(f"LLM determined: greeting={analysis.get('is_greeting')}, needs_context={analysis.get('needs_context')}")
    except Exception as e:
        logger.error(f"Analysis error: {e}")
        state['analysis'] = {
            'is_greeting': False,
            'needs_context': True,
            'intent': 'general',
            'sentiment': 'neutral'
        }
    
    return state


def should_retrieve(state: ChatState) -> str:
    """
    Route based on LLM's decision about whether context is needed.
    
    Args:
        state: Current pipeline state
        
    Returns:
        Next node name
    """
    analysis = state.get('analysis', {})
    
    # LLM decides if context is needed - no hardcoded rules
    if llm_analyzer.should_retrieve_context(analysis):
        return "retrieve_context"
    else:
        return "generate_response"


async def retrieve_context(state: ChatState) -> ChatState:
    """
    Retrieve relevant context from the website knowledge base.
    This is the ONLY source of information for the chatbot.
    
    Args:
        state: Current pipeline state
        
    Returns:
        Updated state with context
    """
    logger.info("Retrieving context from website knowledge base")
    
    try:
        # Build search query using LLM-identified topics
        search_query = llm_analyzer.get_search_query(
            state['message'], 
            state['analysis']
        )
        
        # Search for relevant documents from scraped website
        results = vector_store.search(
            query=search_query,
            n_results=config.MAX_CONTEXT_DOCS
        )
        
        # Extract content from results
        context = []
        for doc, distance, metadata in results:
            source = metadata.get('source', 'website')
            context.append(f"[Source: {source}]\n{doc}")
            logger.debug(f"Retrieved (distance={distance:.3f}): {doc[:100]}...")
        
        state['context'] = context
        logger.info(f"Retrieved {len(context)} relevant documents from website")
        
    except Exception as e:
        logger.error(f"Context retrieval error: {e}")
        state['context'] = []
    
    return state


async def generate_response(state: ChatState) -> ChatState:
    """
    Generate a response using Groq LLM with website context.
    The LLM uses ONLY the website content to respond.
    
    Args:
        state: Current pipeline state
        
    Returns:
        Updated state with response
    """
    logger.info("Generating LLM response using website context")
    
    try:
        # Initialize Groq client
        llm = ChatGroq(
            api_key=config.GROQ_API_KEY,
            model=config.LLM_MODEL,
            temperature=config.LLM_TEMPERATURE,
            max_tokens=config.LLM_MAX_TOKENS
        )
        
        # Build system prompt with website context
        system_prompt = build_system_prompt(state['context'], state['analysis'])
        
        # Generate response
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=state['message'])
        ]
        
        response = llm.invoke(messages)
        state['response'] = response.content
        
        logger.info("Response generated successfully")
        
    except Exception as e:
        logger.error(f"LLM generation error: {e}")
        state['error'] = str(e)
        state['response'] = get_fallback_response()
    
    return state


def build_system_prompt(context: List[str], analysis: Dict) -> str:
    """
    Build the AgenticRAG system prompt with website context.
    Implements lead generation awareness and professional RAG responses.
    
    Args:
        context: Retrieved context documents from website
        analysis: LLM analysis of the message
        
    Returns:
        System prompt string
    """
    # AgenticRAG Senior Engineer Prompt
    base_prompt = """You are the Lead AI Engineer for NexGenTeck - a cutting-edge technology company.

=== ROLE & MISSION ===
You manage an AgenticRAG pipeline that handles two specific tasks:
1. **Chatbot Support**: Answer complex technical questions using retrieved documentation
2. **Lead Generation**: Identify when a user wants to "Contact Us" or "Hire Us" and capture their intent

=== OPERATIONAL CONSTRAINTS ===
**Precision (CRITICAL):**
- ONLY answer based on the retrieved context from our Qdrant vector store
- If the answer isn't in the context, say: "I don't have that specific information, but I can connect you with our human team."
- NEVER hallucinate or make up information about services, pricing, or team members
- If asked about a service we don't offer, explicitly state: "We don't currently offer [service name]"

**Language Requirement:**
- **STRICTLY ENGLISH ONLY**: You must respond ONLY in English, regardless of the user's language.
- If a user speaks another language, politely respond in English explaining you only speak English for now.

**Data Handling:**
- If a user provides a name, email, or project detail, acknowledge it professionally
- When detecting "Contact Us" or "Hire Us" intent, inform them: "I'll ensure your inquiry reaches our team. A lead has been noted in our system."

**Tone:**
- Professional, innovative, and concise
- We are a NexGen solutions startup - emphasize cutting-edge technology
- Speak as part of the team ("we offer", "our services", "our team")

=== RAG PIPELINE STATUS ===
Backend: 8GB Premium Intel server with Docker
Vector Store: Qdrant with BAAI/bge-m3 embeddings
LLM: Llama 3.3 70B via Groq (high-speed inference)
Status: Optimized for high-speed RAG retrieval
"""
    
    # Add retrieved context from Qdrant
    if context:
        context_text = "\n\n---\n\n".join(context)
        base_prompt += f"""
=== RETRIEVED CONTEXT (from Qdrant Vector Embeddings) ===

{context_text}

=== END OF RETRIEVED CONTEXT ===

Use ONLY the information above to respond. If the user's question cannot be answered from this context, acknowledge the limitation and offer to connect them with our team.
"""
    else:
        base_prompt += """
=== CONTEXT STATUS ===
No specific vector embeddings were retrieved for this query.
Provide a helpful general response about NexGenTeck's services without making up specifics.
Offer to connect them with our human team for detailed information.
"""
    
    # Intent-based response tuning
    sentiment = analysis.get('sentiment', 'neutral')
    intent = analysis.get('intent', 'general')
    
    # Lead Generation Detection
    if analysis.get('is_lead_intent') or intent in ['contact', 'hire', 'quote']:
        base_prompt += """
=== LEAD GENERATION DETECTED ===
The user has expressed interest in contacting us or hiring our services.
- Acknowledge their interest enthusiastically
- Ask what specific service or project they're interested in (if not mentioned)
- Inform them: "I'm noting this as a lead in our system. Our team will reach out shortly!"
- If they provide contact details, confirm you've captured them
"""
    
    # Sentiment-Intent Reconciliation
    if sentiment == 'negative' and intent in ['question', 'request']:
        base_prompt += """
Note: The user's tone may seem frustrated, but they are seeking information.
Focus on being helpful and providing accurate information rather than being overly apologetic.
"""
    elif sentiment == 'negative' or intent == 'complaint':
        base_prompt += """
The user has a concern. Be especially empathetic, solution-oriented, and offer to escalate to our human team if needed.
"""
    elif analysis.get('is_greeting'):
        base_prompt += """
=== GREETING DETECTED ===
The user is greeting you. Keep your response SHORT and friendly (1-2 sentences max).
Example: "Hi! Welcome to NexGenTeck. How can I help you today?"
Do NOT give long introductions or list all services. Just greet back warmly and ask how you can help.
"""
    
    return base_prompt


def get_fallback_response() -> str:
    """
    Generate a fallback response when LLM fails.
    
    Returns:
        Fallback response string
    """
    return (
        "I apologize, but I'm having some technical difficulties right now. "
        "Please try again in a moment, or contact us directly at info@nexgenteck.com "
        "for immediate assistance with your questions about our services."
    )


def build_rag_pipeline() -> StateGraph:
    """
    Build the LangGraph RAG pipeline.
    Fully LLM-driven with no hardcoded routing.
    
    Returns:
        Compiled state graph
    """
    # Create the graph
    workflow = StateGraph(ChatState)
    
    # Add nodes
    workflow.add_node("analyze", analyze_message)
    workflow.add_node("retrieve_context", retrieve_context)
    workflow.add_node("generate_response", generate_response)
    
    # Set entry point
    workflow.set_entry_point("analyze")
    
    # LLM decides the routing - no hardcoded greeting detection
    workflow.add_conditional_edges(
        "analyze",
        should_retrieve,
        {
            "retrieve_context": "retrieve_context",
            "generate_response": "generate_response"
        }
    )
    
    # After retrieval, always generate
    workflow.add_edge("retrieve_context", "generate_response")
    workflow.add_edge("generate_response", END)
    
    return workflow.compile()


# Create the pipeline instance
rag_pipeline = build_rag_pipeline()


async def process_message(message: str) -> str:
    """
    Process a user message through the RAG pipeline.
    Uses LLM for all interpretation and website content for context.
    
    Args:
        message: User's message
        
    Returns:
        Bot's response
    """
    logger.info(f"Processing message: {message[:50]}...")
    
    # Initialize state
    initial_state: ChatState = {
        'message': message,
        'analysis': {},
        'context': [],
        'response': '',
        'error': ''
    }
    
    # Run the pipeline
    try:
        result = await rag_pipeline.ainvoke(initial_state)
        return result.get('response', get_fallback_response())
    except Exception as e:
        logger.error(f"Pipeline error: {e}")
        return get_fallback_response()
