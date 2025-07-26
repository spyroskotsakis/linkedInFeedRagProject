#!/usr/bin/env python3
"""
LinkedIn Feed Explorer - Production Version

Streamlit application with RAG API integration for production deployment.
"""

import streamlit as st
import polars as pl
import logging
import httpx
import asyncio
from pathlib import Path
from datetime import datetime
import json

# Import utilities
from utils.data_loader import get_export_dirs, load_export, get_export_metadata, validate_dataframe
from utils.grid import render_grid, show_grid_stats, export_filtered_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="LinkedIn Feed Explorer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0d6efd;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #0d6efd;
    }
    .rag-response {
        background-color: #f8f9fa;
        border-left: 4px solid #28a745;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
    }
    .rag-source {
        background-color: #fff3cd;
        border-left: 3px solid #ffc107;
        padding: 0.5rem;
        margin: 0.5rem 0;
        border-radius: 0.25rem;
        font-size: 0.9rem;
    }
    .status-healthy {
        color: #28a745;
        font-weight: bold;
    }
    .status-unhealthy {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# RAG API Configuration
import os
RAG_API_URL = os.getenv("RAG_API_URL", "http://rag-api:8000")

class RAGAPIClient:
    """Client for interacting with the RAG API service."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def health_check(self) -> dict:
        """Check RAG API health."""
        try:
            response = await self.client.get(f"{self.base_url}/health")
            return response.json()
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return {"status": "unhealthy", "error": str(e)}
    
    async def query(self, query: str, collection_name: str = "linkedin_posts", max_results: int = 10) -> dict:
        """Query the RAG system."""
        try:
            payload = {
                "query": query,
                "collection_name": collection_name,
                "max_results": max_results
            }
            response = await self.client.post(f"{self.base_url}/query", json=payload)
            return response.json()
        except Exception as e:
            logger.error(f"Query failed: {e}")
            return {"error": str(e)}
    
    async def index_data(self, data_path: str, collection_name: str = "linkedin_posts") -> dict:
        """Index data in the RAG system."""
        try:
            payload = {
                "data_path": data_path,
                "collection_name": collection_name
            }
            response = await self.client.post(f"{self.base_url}/index", json=payload)
            return response.json()
        except Exception as e:
            logger.error(f"Indexing failed: {e}")
            return {"error": str(e)}
    
    async def get_collections(self) -> dict:
        """Get available collections."""
        try:
            response = await self.client.get(f"{self.base_url}/collections")
            return response.json()
        except Exception as e:
            logger.error(f"Failed to get collections: {e}")
            return {"error": str(e)}
    
    async def get_collection_stats(self, collection_name: str) -> dict:
        """Get collection statistics."""
        try:
            response = await self.client.get(f"{self.base_url}/collections/{collection_name}/stats")
            return response.json()
        except Exception as e:
            logger.error(f"Failed to get collection stats: {e}")
            return {"error": str(e)}
    
    async def update_config(self, provider: str, model: str = None, temperature: float = 0.1, max_tokens: int = 2048) -> dict:
        """Update RAG configuration."""
        try:
            payload = {
                "provider": provider,
                "model": model,
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            response = await self.client.post(f"{self.base_url}/config", json=payload)
            return response.json()
        except Exception as e:
            logger.error(f"Failed to update config: {e}")
            return {"error": str(e)}
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()

def get_engagement_value(row, field, default=0):
    """Extract engagement value from either new or old format."""
    try:
        # Try new format: engagement.likes
        if hasattr(row, 'engagement') and row.engagement:
            if isinstance(row.engagement, dict):
                return row.engagement.get(field, default)
            elif hasattr(row.engagement, field):
                return getattr(row.engagement, field, default)
        # Try old format: direct likes column
        elif hasattr(row, field):
            return getattr(row, field, default)
    except:
        pass
    return default

def get_post_timestamp(row):
    """Extract and format post timestamp."""
    try:
        # Try new format: timestamp field
        if hasattr(row, 'timestamp') and getattr(row, 'timestamp'):
            timestamp = getattr(row, 'timestamp')
            if timestamp:
                return timestamp
    except:
        pass
    
    try:
        # Try old format: posted_at field
        if hasattr(row, 'posted_at') and getattr(row, 'posted_at'):
            posted_at = getattr(row, 'posted_at')
            if posted_at:
                return posted_at
    except:
        pass
    
    return None

def get_avatar_url(row):
    """Extract avatar URL from author_metadata."""
    try:
        if hasattr(row, 'author_metadata') and getattr(row, 'author_metadata'):
            author_metadata = getattr(row, 'author_metadata')
            if isinstance(author_metadata, dict) and 'avatar_url' in author_metadata:
                avatar_url = author_metadata['avatar_url']
                if avatar_url and avatar_url.strip():
                    return avatar_url
    except:
        pass
    
    return None

def get_post_type(row):
    """Extract post_type from post_metadata."""
    try:
        if hasattr(row, 'post_metadata') and getattr(row, 'post_metadata'):
            post_metadata = getattr(row, 'post_metadata')
            if isinstance(post_metadata, dict) and 'post_type' in post_metadata:
                post_type = post_metadata['post_type']
                if post_type and post_type.strip():
                    return post_type
    except:
        pass
    return None

async def check_rag_health():
    """Check RAG API health status."""
    rag_client = RAGAPIClient(RAG_API_URL)
    try:
        health = await rag_client.health_check()
        await rag_client.close()
        return health
    except Exception as e:
        await rag_client.close()
        return {"status": "unhealthy", "error": str(e)}

async def query_rag_system(query: str, collection_name: str = "linkedin_posts", max_results: int = 10):
    """Query the RAG system."""
    rag_client = RAGAPIClient(RAG_API_URL)
    try:
        result = await rag_client.query(query, collection_name, max_results)
        await rag_client.close()
        return result
    except Exception as e:
        await rag_client.close()
        return {"error": str(e)}

async def index_data_in_rag(data_path: str, collection_name: str = "linkedin_posts"):
    """Index data in the RAG system."""
    rag_client = RAGAPIClient(RAG_API_URL)
    try:
        result = await rag_client.index_data(data_path, collection_name)
        await rag_client.close()
        return result
    except Exception as e:
        await rag_client.close()
        return {"error": str(e)}

def main():
    """Main application function."""
    st.markdown('<h1 class="main-header">📊 LinkedIn Feed Explorer</h1>', unsafe_allow_html=True)
    
    # Initialize RAG client
    if "rag_client" not in st.session_state:
        st.session_state.rag_client = RAGAPIClient(RAG_API_URL)
    
    # Sidebar
    st.sidebar.header("📁 Data Selection")
    
    # RAG Status Check
    st.sidebar.markdown("### 🔍 RAG System Status")
    
    # Check RAG health
    if st.sidebar.button("🔄 Check RAG Status"):
        with st.spinner("Checking RAG system..."):
            health = asyncio.run(check_rag_health())
            
            if health.get("status") == "healthy":
                st.sidebar.success("✅ RAG API Healthy")
                st.sidebar.json(health.get("components", {}))
            else:
                st.sidebar.error("❌ RAG API Unhealthy")
                st.sidebar.error(health.get("error", "Unknown error"))
    
    # Get available export directories
    export_dirs = get_export_dirs()
    
    if not export_dirs:
        st.sidebar.error("❌ No data exports found!")
        st.sidebar.info("Please run the LinkedIn scraper first to generate data exports.")
        st.stop()
    
    # Export selection
    selected_dir = st.sidebar.selectbox(
        "Select Data Export:",
        export_dirs,
        format_func=lambda x: x.name if hasattr(x, 'name') else str(x)
    )
    
    if not selected_dir:
        st.warning("Please select a data export from the sidebar.")
        st.stop()
    
    # Load data
    try:
        df = load_export(selected_dir)
        
        if df.is_empty():
            st.error("❌ No data found in the selected export!")
            st.stop()
        
        # Get metadata
        metadata = get_export_metadata(selected_dir)
        selected_dir_name = selected_dir.name if hasattr(selected_dir, 'name') else str(selected_dir)
        
        # Display metadata
        st.sidebar.success(f"✅ Loaded {len(df):,} posts")
        export_created = metadata.get('created')
        if export_created:
            export_date_str = datetime.fromtimestamp(export_created).strftime('%Y-%m-%d %H:%M')
        else:
            export_date_str = 'Unknown'
        st.sidebar.info(f"📅 Export: {export_date_str}")
        
    except Exception as e:
        st.error(f"❌ Failed to load data: {e}")
        st.stop()
    
    # Main content
    if df.is_empty():
        st.info("🔍 No data found in the selected export.")
        st.stop()
    
    # Create tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Overview",
        "📄 Data Grid", 
        "🖼️ Card View",
        "📈 Analytics",
        "🔍 RAG Search"
    ])
    
    with tab1:
        st.header("📊 Dataset Overview")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Posts", f"{len(df):,}")
        with col2:
            if "author" in df.columns:
                unique_authors = df.select(pl.col("author").n_unique()).item()
                st.metric("Unique Authors", f"{unique_authors:,}")
        with col3:
            # Calculate total likes from engagement data
            total_likes = 0
            try:
                # Try new format: engagement.likes
                if "engagement" in df.columns:
                    total_likes = df.select(pl.col("engagement").struct.field("likes").sum()).item()
                # Try old format: direct likes column
                elif "likes" in df.columns:
                    total_likes = df.select(pl.col("likes").sum()).item()
            except:
                pass
            st.metric("Total Likes", f"{total_likes:,}")
        with col4:
            # Calculate total comments from engagement data
            total_comments = 0
            try:
                # Try new format: engagement.comments
                if "engagement" in df.columns:
                    total_comments = df.select(pl.col("engagement").struct.field("comments").sum()).item()
                # Try old format: direct comments column
                elif "comments" in df.columns:
                    total_comments = df.select(pl.col("comments").sum()).item()
            except:
                pass
            st.metric("Total Comments", f"{total_comments:,}")
        
        # Sample data preview
        st.markdown("### 👀 Sample Posts")
        sample_df = df.head(3)
        for i, row in enumerate(sample_df.to_pandas().itertuples()):
            author = getattr(row, 'author', 'Unknown Author')
            avatar_url = get_avatar_url(row)
            post_type = get_post_type(row)
            
            with st.expander(f"Post {i+1}: {author}"):
                # Author info with avatar
                col1, col2 = st.columns([1, 4])
                with col1:
                    if avatar_url:
                        st.image(avatar_url, width=40)
                    else:
                        st.markdown("👤")
                with col2:
                    st.markdown(f"**{author}**")
                    st.markdown("**Post Content:**")
                
                content = getattr(row, 'content', 'No content')
                st.write(content[:200] + "..." if len(content) > 200 else content)
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    likes = get_engagement_value(row, 'likes', 0)
                    st.write(f"👍 {likes} likes")
                with col2:
                    comments = get_engagement_value(row, 'comments', 0)
                    st.write(f"💬 {comments} comments")
                with col3:
                    shares = get_engagement_value(row, 'shares', 0)
                    st.write(f"🔗 {shares} shares")
                with col4:
                    url = getattr(row, 'url', '')
                    if url:
                        st.markdown(f"[🔗 View]({url})")
                    if post_type:
                        st.markdown(f"**Post Type:** {post_type}")
    
    with tab2:
        st.header("📄 Interactive Data Grid")
        
        # Render grid
        try:
            grid_response = render_grid(df, height=600)
            show_grid_stats(df, grid_response)
            
            # Export functionality
            if grid_response and 'data' in grid_response:
                export_filtered_data(grid_response, f"linkedin_filtered_{selected_dir_name}.csv")
                
        except Exception as e:
            st.error(f"Failed to render grid: {e}")
            st.info("Falling back to simple dataframe view...")
            st.dataframe(df.to_pandas(), height=600)
    
    with tab3:
        st.header("🖼️ Card View")
        
        # Card view controls
        card_col1, card_col2 = st.columns([3, 1])
        
        with card_col2:
            st.markdown("**Display Options**")
            
            # Author filter
            if "author" in df.columns:
                authors = df.select(pl.col("author").unique()).to_series().to_list()
                authors = [""] + sorted([a for a in authors if a])
                selected_author = st.selectbox("Filter by Author:", authors)
                
                if selected_author:
                    df_filtered = df.filter(pl.col("author") == selected_author)
                else:
                    df_filtered = df
            else:
                df_filtered = df
            
            # Posts per page
            posts_per_page = st.slider("Posts per page:", 5, 50, 10)
            
            # Show engagement
            show_engagement = st.checkbox("Show engagement metrics", value=True)
        
        with card_col1:
            # Pagination
            total_posts = len(df_filtered)
            total_pages = (total_posts + posts_per_page - 1) // posts_per_page
            
            if total_pages > 1:
                page = st.selectbox(f"Page (1-{total_pages}):", range(1, total_pages + 1)) - 1
                start_idx = page * posts_per_page
                end_idx = min(start_idx + posts_per_page, total_posts)
                df_page = df_filtered.slice(start_idx, posts_per_page)
            else:
                df_page = df_filtered
            
            # Display posts
            for i, row in enumerate(df_page.to_pandas().itertuples()):
                with st.container():
                    # Author and timestamp
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        author = getattr(row, 'author', 'Unknown Author')
                        avatar_url = get_avatar_url(row)
                        post_type = get_post_type(row)
                        
                        # Display avatar and author name side by side without nested columns
                        if avatar_url:
                            st.image(avatar_url, width=30)
                            st.markdown(f"**{author}**")
                        else:
                            st.markdown(f"**👤 {author}**")
                    with col2:
                        timestamp = get_post_timestamp(row)
                        if timestamp:
                            st.caption(f"📅 {timestamp}")
                    
                    # Content
                    content = getattr(row, 'content', 'No content')
                    st.write(content)
                    
                    # LinkedIn Link
                    url = getattr(row, 'url', '')
                    if url:
                        st.markdown(f"🔗 **[View on LinkedIn]({url})**")
                    
                    # Post Type
                    post_type = get_post_type(row)
                    if post_type:
                        st.markdown(f"**Post Type:** {post_type}")
                    
                    # Engagement bar
                    if show_engagement:
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            likes = get_engagement_value(row, 'likes', 0)
                            st.write(f"👍 {likes} likes")
                        with col2:
                            comments = get_engagement_value(row, 'comments', 0)
                            st.write(f"💬 {comments} comments")
                        with col3:
                            shares = get_engagement_value(row, 'shares', 0)
                            st.write(f"🔗 {shares} shares")
                    
                    # Add some spacing between posts
                    st.markdown("---")
    
    with tab4:
        st.header("📈 Analytics")
        
        # Top performing posts
        st.markdown("### 🏆 Top Performing Posts")
        
        try:
            # Calculate engagement scores
            if "engagement" in df.columns:
                # New format
                df_with_scores = df.with_columns([
                    (pl.col("engagement").struct.field("likes") + 
                     pl.col("engagement").struct.field("comments")).alias("engagement_score")
                ])
            elif "likes" in df.columns and "comments" in df.columns:
                # Old format
                df_with_scores = df.with_columns([
                    (pl.col("likes") + pl.col("comments")).alias("engagement_score")
                ])
            else:
                df_with_scores = df.with_columns(pl.lit(0).alias("engagement_score"))
            
            # Get top posts
            top_posts = df_with_scores.sort("engagement_score", descending=True).head(5)
            
            for i, row in enumerate(top_posts.to_pandas().itertuples()):
                author = getattr(row, 'author', 'Unknown')
                score = getattr(row, 'engagement_score', 0)
                avatar_url = get_avatar_url(row)
                post_type = get_post_type(row)
                
                with st.expander(f"#{i+1} - {author} (Score: {score})"):
                    # Author info with avatar
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        if avatar_url:
                            st.image(avatar_url, width=50)
                        else:
                            st.markdown("👤")
                    with col2:
                        st.markdown(f"**{author}**")
                        st.markdown(f"**Engagement Score: {score}**")
                    
                    content = getattr(row, 'content', 'No content')
                    st.write(content[:300] + "..." if len(content) > 300 else content)
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        likes = get_engagement_value(row, 'likes', 0)
                        st.write(f"👍 {likes} likes")
                    with col2:
                        comments = get_engagement_value(row, 'comments', 0)
                        st.write(f"💬 {comments} comments")
                    with col3:
                        shares = get_engagement_value(row, 'shares', 0)
                        st.write(f"🔗 {shares} shares")
                    if post_type:
                        st.markdown(f"**Post Type:** {post_type}")
        
        except Exception as e:
            st.error(f"Failed to calculate analytics: {e}")
    
    with tab5:
        st.header("🔍 RAG Search - AI-Powered Question Answering")
        
        # RAG configuration
        rag_col1, rag_col2 = st.columns([2, 1])
        
        with rag_col2:
            st.markdown("### ⚙️ Configuration")
            
            # LLM provider selection
            provider = st.selectbox(
                "LLM Provider",
                ["ollama", "azure"],
                help="Choose between local Ollama or Azure OpenAI"
            )
            
            if provider == "ollama":
                model = st.text_input("Ollama Model", value="mistral-nemo:12b", help="Ollama model name")
            else:
                model = st.text_input("Azure Model", value="gpt-4", help="Azure OpenAI model name")
            
            temperature = st.slider("Temperature", 0.0, 1.0, 0.1, 0.1)
            max_results = st.slider("Max Results", 5, 20, 10)
            
            # Update configuration
            if st.button("🔄 Update Config"):
                with st.spinner("Updating configuration..."):
                    result = asyncio.run(
                        st.session_state.rag_client.update_config(
                            provider, model, temperature, 2048
                        )
                    )
                    if "error" in result:
                        st.error(f"Failed to update config: {result['error']}")
                    else:
                        st.success("✅ Configuration updated successfully!")
            
            # Index management
            st.markdown("### 📚 Vector Index")
            
            if st.button("🔄 Rebuild Index"):
                with st.spinner("Indexing documents..."):
                    result = asyncio.run(
                        index_data_in_rag(str(selected_dir), f"linkedin_posts_{selected_dir_name}")
                    )
                    if "error" in result:
                        st.error(f"Failed to rebuild index: {result['error']}")
                    else:
                        st.success("✅ Index rebuilt successfully!")
        
        with rag_col1:
            st.markdown("### 🤖 Ask Questions")
            
            # Query input
            query = st.text_area(
                "Ask a question about your LinkedIn posts:",
                placeholder="e.g., What are the most discussed topics? Who are the most engaging authors?",
                height=100
            )
            
            # Search button
            if st.button("🔍 Search", type="primary"):
                if query.strip():
                    with st.spinner("Searching with AI..."):
                        result = asyncio.run(
                            query_rag_system(query, f"linkedin_posts_{selected_dir_name}", max_results)
                        )
                        
                        if "error" in result:
                            st.error(f"Search failed: {result['error']}")
                        else:
                            # Display answer
                            st.markdown('<div class="rag-response">', unsafe_allow_html=True)
                            st.markdown("### 🤖 AI Answer")
                            st.write(result.get("answer", "No answer generated"))
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            # Display sources
                            sources = result.get("sources", [])
                            if sources:
                                st.markdown("### 📚 Sources")
                                for i, source in enumerate(sources[:5]):  # Show top 5 sources
                                    st.markdown('<div class="rag-source">', unsafe_allow_html=True)
                                    st.markdown(f"**Source {i+1}:**")
                                    st.write(source.get("content", "")[:200] + "...")
                                    if source.get("metadata"):
                                        metadata = source["metadata"]
                                        st.caption(f"Author: {metadata.get('author', 'Unknown')} | Likes: {metadata.get('likes', 0)}")
                                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.warning("Please enter a question to search.")

if __name__ == "__main__":
    main() 