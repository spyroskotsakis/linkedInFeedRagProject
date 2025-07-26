# 🖥️ LinkedIn Feed Explorer

**Interactive Data Visualization & Analysis for LinkedIn Posts**

A powerful Streamlit-based web application that provides interactive visualization and analysis of your scraped LinkedIn data.

## 🚀 Quick Start

```bash
# Navigate to UI directory
cd ui_feed_explorer

# Run the Streamlit app (make sure you're in the conda environment)
source activate_env.sh
streamlit run streamlit_app_simple.py
```

**Access the app at:** `http://localhost:8501`

## 📊 Features

### 📊 Overview Tab
- **Key Metrics Dashboard** - Total posts, unique authors, engagement totals
- **Sample Posts Preview** - Quick preview of extracted content
- **Data Quality Indicators** - Validation status and completeness metrics

### 📄 Data Grid Tab
- **Interactive Table** - Sort, filter, and search through all posts
- **Advanced Filtering** - Filter by author, engagement, date, content
- **Export Functionality** - Download filtered data as CSV
- **Real-time Statistics** - Live metrics as you filter

### 🖼️ Card View Tab
- **Social Media Style Display** - Beautiful card-based post layout
- **Pagination Controls** - Navigate through large datasets
- **Author Filtering** - Focus on specific authors
- **Engagement Metrics** - Visual display of likes, comments, shares

### 📈 Analytics Tab
- **Top Performing Posts** - Posts with highest engagement
- **Author Analytics** - Most active authors and their statistics
- **Engagement Distribution** - Analysis of interaction patterns
- **Content Insights** - Trends and patterns in your data

## 🔧 Technical Features

- **High Performance** - Built with Polars for fast data processing
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Auto Data Discovery** - Automatically finds all your LinkedIn exports
- **Data Validation** - Ensures data quality and completeness
- **Export Capabilities** - Download filtered results for further analysis
- **Format Compatibility** - Works with both old and new data formats

## 📁 Data Requirements

The UI Explorer automatically discovers and loads data from:
- **Location**: `../data/` (relative to ui_feed_explorer directory)
- **Format**: JSON, CSV, or Parquet files
- **Structure**: LinkedIn post exports from the scraper

### Supported Data Formats

#### New Enhanced Format (Recommended)
```json
{
  "urn": "urn:li:activity:1234567890",
  "author": "John Doe",
  "content": "Post content...",
  "engagement": {
    "likes": 42,
    "comments": 8,
    "shares": 3
  },
  "timestamp": "2024-01-24T10:30:00Z"
}
```

#### Legacy Format (Also Supported)
```json
{
  "urn": "urn:li:activity:1234567890",
  "author": "John Doe",
  "content": "Post content...",
  "likes": 42,
  "comments": 8,
  "shares": 3,
  "posted_at": "2024-01-24T10:30:00Z"
}
```

## 🎯 Use Cases

- **Content Analysis** - Identify trending topics and themes
- **Author Research** - Find influential contributors in your network
- **Engagement Insights** - Understand what content performs best
- **Data Export** - Prepare filtered datasets for external analysis
- **Quick Exploration** - Rapidly explore large datasets without coding

## 🛠️ Installation & Setup

The UI Explorer uses the same conda environment as the scraper:

```bash
# Ensure you're in the conda environment
source activate_env.sh

# Navigate to UI directory
cd ui_feed_explorer

# Run the simple version (recommended)
streamlit run streamlit_app_simple.py

# Or run the full version with RAG (if dependencies are available)
streamlit run streamlit_app.py
```

## 🔍 Troubleshooting

### No data found:
- Ensure you've run the LinkedIn scraper first
- Check that data is in the `../data/` directory
- Verify file permissions and accessibility

### App won't start:
- Confirm you're in the conda environment: `conda info --envs`
- Check Streamlit installation: `streamlit --version`
- Verify Python path: `which python`

### Performance issues:
- For large datasets (>10k posts), use pagination in Card View
- Use Data Grid filters to focus on specific data subsets
- Consider exporting filtered data for external analysis

### RAG functionality issues:
- Use `streamlit_app_simple.py` for core features without RAG
- RAG requires additional dependencies that may have compatibility issues
- Core visualization features work without RAG dependencies

## 📋 Prerequisites

1. **LinkedIn Scraper Data** - Must have run the main scraper first
2. **Conda Environment** - Use the same environment as the scraper
3. **Streamlit** - Automatically installed with the environment
4. **Polars** - For high-performance data processing

## 🎉 Success Metrics

- ✅ **Fast Loading** - Handles 10k+ posts efficiently
- ✅ **Responsive UI** - Smooth interactions and real-time updates
- ✅ **Data Integrity** - Maintains data quality and validation
- ✅ **Export Functionality** - Reliable data export capabilities
- ✅ **Cross-platform** - Works on Windows, macOS, and Linux
- ✅ **Format Compatibility** - Works with both old and new data structures

## 🔄 Version Information

### Simple Version (`streamlit_app_simple.py`) - **RECOMMENDED**
- ✅ **Core Features**: Overview, Data Grid, Card View, Analytics
- ✅ **No Dependencies**: Works without RAG or additional packages
- ✅ **Stable**: No compatibility issues with pyarrow or other libraries
- ✅ **Fast**: Optimized for performance and reliability

### Full Version (`streamlit_app.py`)
- ✅ **All Features**: Includes RAG search functionality
- ⚠️ **Dependencies**: Requires additional packages (may have compatibility issues)
- ⚠️ **Complexity**: More features but potential for import errors

## 🚀 Getting Started

1. **Run the Scraper**:
   ```bash
   python complete_linkedin_scraper_enhanced_fast.py --posts 50 --speed fast
   ```

2. **Start the UI**:
   ```bash
   cd ui_feed_explorer
   source activate_env.sh
   streamlit run streamlit_app_simple.py
   ```

3. **Explore Your Data**:
   - Select your data export from the sidebar
   - Browse through Overview, Data Grid, Card View, and Analytics tabs
   - Export filtered data as needed

---

**Ready for data exploration!** 🚀📊
