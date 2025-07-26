
import streamlit as st
import polars as pl
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

def flatten_engagement_data(df: pl.DataFrame) -> pl.DataFrame:
    """
    Flatten engagement data from nested structure for grid display.
    
    Args:
        df: Polars DataFrame with potentially nested engagement data
        
    Returns:
        DataFrame with flattened engagement columns
    """
    try:
        if "engagement" in df.columns:
            # Extract engagement fields from struct
            df_flattened = df.with_columns([
                pl.col("engagement").struct.field("likes").alias("likes"),
                pl.col("engagement").struct.field("comments").alias("comments"),
                pl.col("engagement").struct.field("shares").alias("shares")
            ])
            return df_flattened
        else:
            # Already flattened or old format
            return df
    except Exception as e:
        logger.warning(f"Could not flatten engagement data: {e}")
        return df

def render_grid(df: pl.DataFrame, height: int = 500, enable_enterprise_modules: bool = False) -> Dict[str, Any]:
    """
    Render ag-Grid with server-side pagination and optimized performance.
    
    Args:
        df: Polars DataFrame to display
        height: Grid height in pixels
        enable_enterprise_modules: Enable enterprise features
        
    Returns:
        Dictionary with grid response data
    """
    if df.is_empty():
        st.warning("No data to display")
        return {}
    
    try:
        # Flatten engagement data for display
        df_display = flatten_engagement_data(df)
        
        # Convert to pandas for ag-grid compatibility
        df_pandas = df_display.to_pandas()
        
        # Build grid options
        gb = GridOptionsBuilder.from_dataframe(df_pandas)
        
        # Configure pagination
        gb.configure_pagination(
            enabled=True,
            paginationAutoPageSize=False,
            paginationPageSize=100
        )
        
        # Enable server-side model for large datasets
        if len(df_pandas) > 1000:
            gb.configure_grid_options(
                rowModelType='serverSide',
                serverSideStoreType='partial',
                cacheBlockSize=100,
                maxBlocksInCache=10
            )
        
        # Configure columns
        gb.configure_default_column(
            filterable=True,
            sortable=True,
            resizable=True,
            width=150
        )
        
        # Custom column configurations
        if "content" in df_display.columns:
            gb.configure_column(
                "content",
                wrapText=True,
                autoHeight=True,
                width=300,
                cellRenderer=JsCode("""
                    function(params) {
                        if (params.value && params.value.length > 100) {
                            return params.value.substring(0, 100) + '...';
                        }
                        return params.value;
                    }
                """)
            )
        
        if "author" in df_display.columns:
            gb.configure_column("author", width=150, pinned="left")
        
        if "urn" in df_display.columns:
            gb.configure_column("urn", hide=True)  # Hide URN by default
        
        # URL column configuration
        if "url" in df_display.columns:
            gb.configure_column(
                "url",
                headerName="LinkedIn Link",
                cellRenderer=JsCode("""
                    function(params) {
                        if (params.value) {
                            return '<a href="' + params.value + '" target="_blank">🔗 View</a>';
                        }
                        return '';
                    }
                """),
                width=120,
                cellStyle={"textAlign": "center"}
            )
        
        # Engagement columns styling
        engagement_cols = ["likes", "comments", "shares"]
        for col in engagement_cols:
            if col in df_display.columns:
                gb.configure_column(
                    col,
                    type=["numericColumn"],
                    width=100,
                    cellStyle={"textAlign": "center"}
                )
        
        # Date column formatting
        date_cols = ["posted_at", "extracted_at", "timestamp"]
        for col in date_cols:
            if col in df_display.columns:
                gb.configure_column(
                    col,
                    type=["dateColumnFilter"],
                    width=180
                )
        
        # Selection and update modes
        gb.configure_selection(
            selection_mode="multiple",
            use_checkbox=True,
            groupSelectsChildren=True,
            groupSelectsFiltered=True
        )
        
        # Build grid options
        grid_options = gb.build()
        
        # Add theme and styling
        custom_css = {
            ".ag-theme-streamlit": {
                "transform": "scale(0.8)",
                "transform-origin": "0 0"
            }
        }
        
        # Display grid info
        st.caption(f"📊 Displaying {len(df_pandas):,} posts with server-side optimization")
        
        # Render the grid
        grid_response = AgGrid(
            df_pandas,
            gridOptions=grid_options,
            height=height,
            width='100%',
            data_return_mode='FILTERED_AND_SORTED',
            update_mode=GridUpdateMode.SELECTION_CHANGED,
            fit_columns_on_grid_load=False,
            allow_unsafe_jscode=True,
            enable_enterprise_modules=enable_enterprise_modules,
            custom_css=custom_css,
            theme='streamlit'
        )
        
        return grid_response
        
    except Exception as e:
        logger.error(f"Error rendering grid: {e}")
        st.error(f"Failed to render data grid: {str(e)}")
        
        # Fallback to simple dataframe display
        st.dataframe(df.to_pandas(), height=height)
        return {}

def show_grid_stats(df: pl.DataFrame, grid_response: Optional[Dict[str, Any]] = None) -> None:
    """
    Show statistics about the current grid data.
    
    Args:
        df: Original DataFrame
        grid_response: Optional grid response for filtered stats
    """
    try:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Posts", f"{len(df):,}")
        
        with col2:
            if grid_response and 'data' in grid_response:
                visible_count = len(grid_response['data'])
                st.metric("Visible Posts", f"{visible_count:,}")
            else:
                st.metric("Visible Posts", f"{len(df):,}")
        
        with col3:
            if "author" in df.columns:
                unique_authors = df.select(pl.col("author").n_unique()).item()
                st.metric("Unique Authors", f"{unique_authors:,}")
        
        with col4:
            if "likes" in df.columns:
                total_likes = df.select(pl.col("likes").sum()).item()
                st.metric("Total Likes", f"{total_likes:,}")
                
    except Exception as e:
        logger.error(f"Error showing grid stats: {e}")

def export_filtered_data(grid_response: Dict[str, Any], filename: str = "filtered_data.csv") -> None:
    """
    Export filtered/selected data from grid.
    
    Args:
        grid_response: Response from AgGrid component
        filename: Export filename
    """
    try:
        if not grid_response or 'data' not in grid_response:
            st.warning("No data to export")
            return
        
        data = grid_response['data']
        
        if len(data) == 0:
            st.warning("No rows selected for export")
            return
        
        # Convert to CSV
        df = pl.DataFrame(data)
        csv_data = df.write_csv()
        
        st.download_button(
            label="📥 Download Filtered Data",
            data=csv_data,
            file_name=filename,
            mime="text/csv",
            help="Download the currently filtered/selected data as CSV"
        )
        
    except Exception as e:
        logger.error(f"Error exporting data: {e}")
        st.error(f"Failed to export data: {str(e)}")

def optimize_dataframe_for_display(df: pl.DataFrame, max_rows: int = 10000) -> pl.DataFrame:
    """
    Optimize DataFrame for display performance.
    
    Args:
        df: Input DataFrame
        max_rows: Maximum rows to keep for performance
        
    Returns:
        Optimized DataFrame
    """
    try:
        # Limit rows if too large
        if len(df) > max_rows:
            st.warning(f"Dataset has {len(df):,} rows. Showing first {max_rows:,} for performance.")
            df = df.head(max_rows)
        
        # Optimize string columns (simplified)
        return df
        
    except Exception as e:
        logger.error(f"Error optimizing DataFrame: {e}")
        return df
