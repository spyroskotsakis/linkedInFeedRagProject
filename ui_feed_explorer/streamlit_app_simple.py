#!/usr/bin/env python3
"""
LinkedIn Feed Explorer - Simple Version (No RAG)
"""

import streamlit as st
import polars as pl
from pathlib import Path
import sys
import logging

# Add current directory to path for imports
current_dir = Path(__file__).parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from utils.data_loader import get_export_dirs, load_export, get_export_metadata, validate_dataframe
from utils.grid import render_grid, show_grid_stats, export_filtered_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="LinkedIn Feed Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
.metric-container {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

def get_engagement_value(row, field, default=0):
    """
    Safely extract engagement values from both old and new data formats.
    
    Args:
        row: DataFrame row
        field: Field name ('likes', 'comments', 'shares')
        default: Default value if not found
        
    Returns:
        Engagement value
    """
    try:
        # Try new format first: engagement.likes, engagement.comments, etc.
        if hasattr(row, 'engagement') and row.engagement:
            if isinstance(row.engagement, dict) and field in row.engagement:
                return row.engagement[field] or default
            elif hasattr(row.engagement, field):
                return getattr(row.engagement, field) or default
        
        # Try old format: direct columns
        if hasattr(row, field):
            return getattr(row, field) or default
            
        return default
    except:
        return default

def get_post_timestamp(row):
    """
    Safely extract timestamp from both old and new data formats.
    """
    try:
        # Try new format: timestamp field
        if hasattr(row, 'timestamp') and row.timestamp:
            return row.timestamp
        
        # Try old format: posted_at field
        if hasattr(row, 'posted_at') and row.posted_at:
            return row.posted_at
            
        return ""
    except:
        return ""

def main():
    st.title("🔍 LinkedIn Feed Explorer")
    st.markdown("*Explore LinkedIn posts with interactive visualizations and analytics*")

    # --- Sidebar for Export Selection ---
    with st.sidebar:
        st.header("📁 Data Export Selection")

        export_dirs = get_export_dirs()
        dir_names = [d.name for d in export_dirs]

        if not dir_names:
            st.warning("No data exports found in the 'data/' directory.")
            st.info("Please run the LinkedIn scraper first to generate some data.")
            st.markdown("""
            **Quick Start:**
            ```bash
            python complete_linkedin_scraper_enhanced_fast.py --posts 50 --speed fast
            ```
            """)
            st.stop()

        # Export selection
        selected_dir_name = st.selectbox(
            "Select an export to analyze:",
            options=dir_names,
            help="Choose a dataset to explore. The most recent is selected by default."
        )

        selected_dir_path = Path("../data") / selected_dir_name

        # Display export metadata
        if selected_dir_path:
            metadata = get_export_metadata(selected_dir_path)

            st.markdown("### 📊 Export Info")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Posts", metadata.get("post_count", "Unknown"))
                st.metric("Files", metadata["file_count"])
            with col2:
                st.metric("Size", f"{metadata['total_size_mb']:.1f} MB")
                st.metric("Format", "Parquet" if metadata["has_parquet"] else "CSV/JSON")

            # Feature status
            st.markdown("### 🚀 Features")
            st.info("✅ Core visualization features enabled")
            st.info("ℹ️ RAG features available in full version")

    # --- Load Data ---
    if selected_dir_path and selected_dir_path.exists():
        with st.spinner("Loading data..."):
            df = load_export(selected_dir_path)
            validation = validate_dataframe(df)

        if validation["is_valid"]:
            st.sidebar.success(f"✅ Loaded {len(df):,} posts successfully")
        else:
            st.sidebar.error("❌ Data validation failed")
            st.sidebar.write("Missing columns:", validation["missing_columns"])
    else:
        df = pl.DataFrame()
        st.sidebar.error("❌ Selected export directory not found")

    # --- Main Content Area ---
    if not df.is_empty() and validation.get("is_valid", False):

        # Main tabs
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Overview",
            "📄 Data Grid",
            "🖼️ Card View",
            "📈 Analytics"
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
                with st.expander(f"Post {i+1}: {getattr(row, 'author', 'Unknown Author')}"):
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
                posts_per_page = st.selectbox("Posts per page", [5, 10, 20, 50], index=1)
                show_engagement = st.checkbox("Show engagement metrics", True)

                if "author" in df.columns:
                    authors = df.select(pl.col("author").unique()).to_series().to_list()
                    selected_author = st.selectbox("Filter by author", ["All"] + authors)
                else:
                    selected_author = "All"

            # Filter data
            display_df = df
            if selected_author != "All":
                display_df = df.filter(pl.col("author") == selected_author)

            # Pagination
            total_posts = len(display_df)
            total_pages = (total_posts + posts_per_page - 1) // posts_per_page

            if total_pages > 1:
                page = st.selectbox("Page", range(1, total_pages + 1))
                start_idx = (page - 1) * posts_per_page
                end_idx = min(start_idx + posts_per_page, total_posts)
                page_df = display_df.slice(start_idx, posts_per_page)
            else:
                page_df = display_df.head(posts_per_page)
                page = 1

            st.write(f"Showing {len(page_df)} of {total_posts} posts (Page {page} of {total_pages})")

            # Render cards
            for i, row in enumerate(page_df.to_pandas().itertuples()):
                with st.container():
                    st.markdown("---")

                    # Header
                    header_col1, header_col2 = st.columns([3, 1])
                    with header_col1:
                        author = getattr(row, 'author', 'Unknown Author')
                        st.markdown(f"### 👤 {author}")

                        timestamp = get_post_timestamp(row)
                        if timestamp:
                            st.caption(f"📅 {timestamp}")

                    with header_col2:
                        if show_engagement:
                            likes = get_engagement_value(row, 'likes', 0)
                            comments = get_engagement_value(row, 'comments', 0)
                            shares = get_engagement_value(row, 'shares', 0)

                            st.metric("Engagement", f"{likes + comments + shares}")

                    # Content
                    content = getattr(row, 'content', 'No content available')
                    st.write(content)

                    # LinkedIn Link
                    url = getattr(row, 'url', '')
                    if url:
                        st.markdown(f"🔗 **[View on LinkedIn]({url})**")

                    # Engagement bar
                    if show_engagement:
                        eng_col1, eng_col2, eng_col3 = st.columns(3)
                        with eng_col1:
                            likes = get_engagement_value(row, 'likes', 0)
                            st.write(f"👍 {likes}")
                        with eng_col2:
                            comments = get_engagement_value(row, 'comments', 0)
                            st.write(f"💬 {comments}")
                        with eng_col3:
                            shares = get_engagement_value(row, 'shares', 0)
                            st.write(f"🔗 {shares}")

        with tab4:
            st.header("📈 Analytics & Insights")

            # Engagement analytics
            try:
                # Create engagement metrics DataFrame
                if "engagement" in df.columns:
                    # New format: extract from engagement struct
                    df_analysis = df.with_columns([
                        (pl.col("engagement").struct.field("likes") + 
                         pl.col("engagement").struct.field("comments") + 
                         pl.col("engagement").struct.field("shares")).alias("total_engagement")
                    ])
                elif "likes" in df.columns and "comments" in df.columns:
                    # Old format: direct columns
                    df_analysis = df.with_columns([
                        (pl.col("likes") + pl.col("comments") + pl.col("shares")).alias("total_engagement")
                    ])
                else:
                    df_analysis = df.with_columns([pl.lit(0).alias("total_engagement")])

                if "total_engagement" in df_analysis.columns:
                    st.subheader("📊 Engagement Distribution")

                    # Top performing posts
                    top_posts = df_analysis.sort("total_engagement", descending=True).head(5)

                    st.markdown("**🏆 Top Performing Posts**")
                    for i, row in enumerate(top_posts.to_pandas().itertuples()):
                        with st.expander(f"#{i+1}: {getattr(row, 'author', 'Unknown')} ({getattr(row, 'total_engagement', 0)} total engagement)"):
                            content = getattr(row, 'content', 'No content')
                            st.write(content[:300] + "..." if len(content) > 300 else content)

            except Exception as e:
                st.warning(f"Could not analyze engagement data: {e}")

            # Author analytics
            if "author" in df.columns:
                st.subheader("👥 Author Analytics")

                try:
                    # Calculate author statistics
                    if "engagement" in df.columns:
                        # New format: extract from engagement struct
                        author_stats = df.group_by("author").agg([
                            pl.count().alias("post_count"),
                            pl.col("engagement").struct.field("likes").sum().alias("total_likes"),
                            pl.col("engagement").struct.field("comments").sum().alias("total_comments")
                        ]).sort("post_count", descending=True)
                    elif "likes" in df.columns and "comments" in df.columns:
                        # Old format: direct columns
                        author_stats = df.group_by("author").agg([
                            pl.count().alias("post_count"),
                            pl.col("likes").sum().alias("total_likes"),
                            pl.col("comments").sum().alias("total_comments")
                        ]).sort("post_count", descending=True)
                    else:
                        # Fallback: just count posts
                        author_stats = df.group_by("author").agg([
                            pl.count().alias("post_count")
                        ]).sort("post_count", descending=True)

                    st.markdown("**📝 Most Active Authors**")
                    st.dataframe(author_stats.head(10).to_pandas(), use_container_width=True)

                except Exception as e:
                    st.warning(f"Could not analyze author statistics: {e}")

    else:
        if df.is_empty():
            st.info("🔍 Please select a valid data export from the sidebar to begin exploring.")
        else:
            st.error("❌ The selected dataset failed validation. Please check the data format.")
            if "missing_columns" in validation:
                st.write("Missing required columns:", validation["missing_columns"])

if __name__ == "__main__":
    main() 