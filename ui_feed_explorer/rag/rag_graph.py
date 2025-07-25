"""
LangGraph-based RAG workflow for LinkedIn feed question answering.
"""

import logging
from typing import Dict, List, Any, Optional, TypedDict
import streamlit as st
from .retriever import get_retriever
from .llm_factory import get_configured_llm

try:
    from langgraph.graph import END, StateGraph
    from langchain_core.documents import Document
    from langchain_core.prompts import PromptTemplate
except ImportError as e:
    try:
        # Fallback for older versions
        from langgraph.graph import END, StateGraph
        from langchain.schema import Document
        from langchain.prompts import PromptTemplate
    except ImportError:
        st.error(f"Missing required dependencies: {e}")
        st.info("Please install: pip install langgraph langchain langchain-core")

logger = logging.getLogger(__name__)

class FeedRAGState(TypedDict):
    """State for the Feed RAG workflow."""
    query: str
    documents: List[Document]
    filtered_documents: List[Document]
    answer: str
    citations: List[str]
    confidence_score: float
    search_metadata: Dict[str, Any]
    error: Optional[str]

# Prompt templates
RELEVANCE_PROMPT = PromptTemplate(
    input_variables=["query", "document"],
    template="""
You are an expert at evaluating document relevance for question answering.

Query: {query}

Document: {document}

Is this document relevant to answering the query? Consider:
1. Does it contain information that helps answer the question?
2. Is the content directly related to the query topic?
3. Would this document be useful in forming a comprehensive answer?

Respond with ONLY "RELEVANT" or "NOT_RELEVANT" followed by a brief explanation.

Response:"""
)

ANSWER_PROMPT = PromptTemplate(
    input_variables=["query", "context", "citations"],
    template="""
You are an expert analyst answering questions about LinkedIn posts and professional content.

Query: {query}

Context from LinkedIn posts:
{context}

Instructions:
1. Answer the question based ONLY on the provided context
2. If the context doesn't contain enough information, say so clearly
3. Include specific details and examples from the posts when relevant
4. Cite specific LinkedIn posts using the format [Author Name - Post excerpt]
5. Maintain professional tone appropriate for business/professional context

Available citations: {citations}

Provide a comprehensive and accurate answer:"""
)

def build_rag_graph(collection_name: str = "linkedin_posts") -> StateGraph:
    """
    Build a LangGraph workflow for Self-RAG over LinkedIn posts.
    
    Args:
        collection_name: ChromaDB collection name
        
    Returns:
        Compiled LangGraph workflow
    """
    
    def retrieve_documents(state: FeedRAGState) -> FeedRAGState:
        """Retrieve relevant documents from vector store."""
        try:
            query = state["query"]
            logger.info(f"Retrieving documents for query: {query}")
            
            retriever = get_retriever(collection_name, {"k": 8})
            documents = retriever._get_relevant_documents(query)
            
            # Add search metadata
            search_metadata = {
                "total_retrieved": len(documents),
                "collection": collection_name,
                "avg_similarity": sum(doc.metadata.get("similarity_score", 0.0) for doc in documents) / len(documents) if documents else 0.0
            }
            
            state["documents"] = documents
            state["search_metadata"] = search_metadata
            
            logger.info(f"Retrieved {len(documents)} documents")
            return state
            
        except Exception as e:
            logger.error(f"Error in retrieve_documents: {e}")
            state["error"] = f"Retrieval failed: {str(e)}"
            state["documents"] = []
            state["search_metadata"] = {}
            return state
    
    def rank_documents(state: FeedRAGState) -> FeedRAGState:
        """Rank and filter documents by relevance using LLM."""
        try:
            documents = state["documents"]
            query = state["query"]
            
            if not documents:
                state["filtered_documents"] = []
                return state
            
            logger.info(f"Ranking {len(documents)} documents for relevance")
            
            llm = get_configured_llm()
            filtered_docs = []
            
            for doc in documents:
                try:
                    # Check relevance using LLM
                    relevance_prompt = RELEVANCE_PROMPT.format(
                        query=query,
                        document=doc.page_content[:500]  # Limit for prompt efficiency
                    )
                    
                    response = llm.invoke(relevance_prompt)
                    response_text = response.content if hasattr(response, 'content') else str(response)
                    
                    if "RELEVANT" in response_text.upper():
                        # Add relevance explanation to metadata
                        doc.metadata["relevance_explanation"] = response_text
                        filtered_docs.append(doc)
                        
                except Exception as e:
                    logger.warning(f"Error evaluating document relevance: {e}")
                    # Include document if evaluation fails (fail-safe)
                    filtered_docs.append(doc)
            
            # If no docs pass relevance check, use top 3 by similarity
            if not filtered_docs and documents:
                filtered_docs = sorted(
                    documents,
                    key=lambda x: x.metadata.get("similarity_score", 0.0),
                    reverse=True
                )[:3]
                logger.info("No documents passed relevance check, using top 3 by similarity")
            
            state["filtered_documents"] = filtered_docs
            logger.info(f"Filtered to {len(filtered_docs)} relevant documents")
            
            return state
            
        except Exception as e:
            logger.error(f"Error in rank_documents: {e}")
            # Fallback: use original documents
            state["filtered_documents"] = state["documents"][:3]
            return state
    
    def generate_answer(state: FeedRAGState) -> FeedRAGState:
        """Generate final answer using filtered documents."""
        try:
            query = state["query"]
            documents = state["filtered_documents"]
            
            if not documents:
                state["answer"] = "I couldn't find any relevant LinkedIn posts to answer your question. Please try a different query or check if the data has been indexed."
                state["citations"] = []
                state["confidence_score"] = 0.0
                return state
            
            logger.info(f"Generating answer using {len(documents)} documents")
            
            # Prepare context and citations
            context_parts = []
            citations = []
            
            for i, doc in enumerate(documents):
                author = doc.metadata.get("author", "Unknown Author")
                content_preview = doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
                similarity = doc.metadata.get("similarity_score", 0.0)
                
                context_parts.append(f"Post {i+1} by {author}:\n{doc.page_content}")
                citations.append(f"[{author} - {content_preview}] (Similarity: {similarity:.2f})")
            
            context = "\n\n".join(context_parts)
            citations_text = "\n".join(citations)
            
            # Generate answer
            llm = get_configured_llm()
            answer_prompt = ANSWER_PROMPT.format(
                query=query,
                context=context,
                citations=citations_text
            )
            
            response = llm.invoke(answer_prompt)
            answer = response.content if hasattr(response, 'content') else str(response)
            
            # Calculate confidence based on similarity scores and number of docs
            avg_similarity = sum(doc.metadata.get("similarity_score", 0.0) for doc in documents) / len(documents)
            doc_count_factor = min(len(documents) / 3.0, 1.0)  # Normalize to max of 3 docs
            confidence_score = (avg_similarity + doc_count_factor) / 2.0
            
            state["answer"] = answer
            state["citations"] = citations
            state["confidence_score"] = confidence_score
            
            logger.info(f"Generated answer with confidence: {confidence_score:.2f}")
            return state
            
        except Exception as e:
            logger.error(f"Error in generate_answer: {e}")
            state["answer"] = f"I encountered an error while generating the answer: {str(e)}"
            state["citations"] = []
            state["confidence_score"] = 0.0
            return state
    
    # Build the graph
    workflow = StateGraph(FeedRAGState)
    
    # Add nodes
    workflow.add_node("retrieve", retrieve_documents)
    workflow.add_node("rank", rank_documents)
    workflow.add_node("answer", generate_answer)
    
    # Add edges
    workflow.add_edge("retrieve", "rank")
    workflow.add_edge("rank", "answer")
    workflow.add_edge("answer", END)
    
    # Set entry point
    workflow.set_entry_point("retrieve")
    
    return workflow.compile()

def run_rag_query(query: str, 
                 collection_name: str = "linkedin_posts") -> Dict[str, Any]:
    """
    Run a RAG query against the LinkedIn posts.
    
    Args:
        query: User question
        collection_name: ChromaDB collection name
        
    Returns:
        Dictionary with answer and metadata
    """
    try:
        # Build and run workflow
        workflow = build_rag_graph(collection_name)
        
        initial_state = FeedRAGState(
            query=query,
            documents=[],
            filtered_documents=[],
            answer="",
            citations=[],
            confidence_score=0.0,
            search_metadata={},
            error=None
        )
        
        # Execute workflow
        result = workflow.invoke(initial_state)
        
        return {
            "query": query,
            "answer": result["answer"],
            "citations": result["citations"],
            "confidence_score": result["confidence_score"],
            "search_metadata": result["search_metadata"],
            "document_count": len(result["filtered_documents"]),
            "error": result.get("error")
        }
        
    except Exception as e:
        logger.error(f"RAG query failed: {e}")
        return {
            "query": query,
            "answer": f"I encountered an error processing your query: {str(e)}",
            "citations": [],
            "confidence_score": 0.0,
            "search_metadata": {},
            "document_count": 0,
            "error": str(e)
        }

def test_rag_workflow(collection_name: str = "linkedin_posts") -> Dict[str, Any]:
    """
    Test the RAG workflow with sample queries.
    
    Args:
        collection_name: Collection to test against
        
    Returns:
        Test results
    """
    test_queries = [
        "What are people saying about artificial intelligence?",
        "What career advice is being shared?",
        "What trends are mentioned in the posts?"
    ]
    
    results = []
    
    for query in test_queries:
        try:
            result = run_rag_query(query, collection_name)
            results.append({
                "query": query,
                "success": not bool(result.get("error")),
                "answer_length": len(result["answer"]),
                "citations_count": len(result["citations"]),
                "confidence": result["confidence_score"]
            })
        except Exception as e:
            results.append({
                "query": query,
                "success": False,
                "error": str(e)
            })
    
    return {
        "total_tests": len(test_queries),
        "successful_tests": sum(1 for r in results if r.get("success", False)),
        "results": results
    } 