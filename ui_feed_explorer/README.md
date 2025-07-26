# 🖥️ LinkedIn Feed Explorer - Production UI

**Interactive Data Visualization & RAG Search for LinkedIn Posts**

A modern Streamlit-based web application that provides interactive visualization, analysis, and AI-powered search of your scraped LinkedIn data.

## 🚀 **Quick Start (Production)**

```bash
# Start the production system
./start_production.sh

# Access the application at: http://localhost:8501
```

## 📊 **Features**

### 📊 **Overview Tab**
- **Key Metrics Dashboard** - Total posts, unique authors, engagement totals
- **Sample Posts Preview** - Quick preview of extracted content
- **Data Quality Indicators** - Validation status and completeness metrics

### 📄 **Data Grid Tab**
- **Interactive Table** - Sort, filter, and search through all posts
- **Advanced Filtering** - Filter by author, engagement, date, content
- **Export Functionality** - Download filtered data as CSV
- **Real-time Statistics** - Live metrics as you filter

### 🖼️ **Card View Tab**
- **Social Media Style Display** - Beautiful card-based post layout
- **Pagination Controls** - Navigate through large datasets
- **Author Filtering** - Focus on specific authors
- **Engagement Metrics** - Visual display of likes, comments, shares

### 📈 **Analytics Tab**
- **Top Performing Posts** - Posts with highest engagement
- **Author Analytics** - Most active authors and their statistics
- **Engagement Distribution** - Analysis of interaction patterns
- **Content Insights** - Trends and patterns in your data

### 🤖 **RAG Search Tab**
- **AI-Powered Search** - Natural language queries about your data
- **Intelligent Answers** - AI-generated responses with citations
- **Source Tracking** - Links to original LinkedIn posts
- **LLM Configuration** - Switch between Ollama and Azure OpenAI

## 🔧 **Technical Features**

- **High Performance** - Built with Polars for fast data processing
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Auto Data Discovery** - Automatically finds all your LinkedIn exports
- **Data Validation** - Ensures data quality and completeness
- **Export Capabilities** - Download filtered results for further analysis
- **Format Compatibility** - Works with both old and new data formats
- **RAG Integration** - Seamless connection to AI-powered search

## 📁 **Data Requirements**

The UI Explorer automatically discovers and loads data from:
- **Location**: `../data/` (relative to ui_feed_explorer directory)
- **Format**: JSON, CSV, or Parquet files
- **Structure**: LinkedIn post exports from the scraper

### **Supported Data Formats**

#### **New Enhanced Format (Recommended)**
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
  "timestamp": "2024-01-24T10:30:00Z",
  "url": "https://linkedin.com/posts/..."
}
```

#### **Legacy Format (Also Supported)**
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

## 🎯 **Use Cases**

- **Content Analysis** - Identify trending topics and themes
- **Author Research** - Find influential contributors in your network
- **Engagement Insights** - Understand what content performs best
- **Data Export** - Prepare filtered datasets for external analysis
- **Quick Exploration** - Rapidly explore large datasets without coding
- **AI-Powered Search** - Ask natural language questions about your data

## 🛠️ **Installation & Setup**

### **Production Deployment (Recommended)**
```bash
# Start the complete production system
./start_production.sh

# Access the UI at: http://localhost:8501
```

### **Development Setup**
```bash
# Ensure you're in the conda environment
source activate_env.sh

# Navigate to UI directory
cd ui_feed_explorer

# Install dependencies
pip install -r requirements.txt

# Run the production app
streamlit run streamlit_app_production.py
```

## 🔍 **RAG Search Setup**

### **1. Load Your Data**
- Select your LinkedIn export from the sidebar
- System automatically validates and loads data
- View overview statistics and sample posts

### **2. Index Data for RAG**
- Click "Index Data" button in the RAG Search tab
- System builds vector embeddings for semantic search
- Progress is shown with real-time updates

### **3. Configure LLM Provider**
- **Ollama (Local)**: Select for local AI processing
- **Azure OpenAI**: Select for cloud-based AI
- Adjust temperature and other parameters as needed

### **4. Ask Questions**
- Use natural language queries
- Get AI-generated answers with citations
- View source posts with direct links

## 🔍 **Troubleshooting**

### **No data found:**
- Ensure you've run the LinkedIn scraper first
- Check that data is in the `../data/` directory
- Verify file permissions and accessibility

### **App won't start:**
- Confirm you're in the conda environment: `conda info --envs`
- Check Streamlit installation: `streamlit --version`
- Verify Python path: `which python`

### **Performance issues:**
- For large datasets (>10k posts), use pagination in Card View
- Use Data Grid filters to focus on specific data subsets
- Consider exporting filtered data for external analysis

### **RAG search not working:**
- Check RAG API status in the sidebar
- Verify Ollama is running: `ollama list`
- Check API logs: `docker-compose logs rag-api`

## 📋 **Prerequisites**

1. **LinkedIn Scraper Data** - Must have run the main scraper first
2. **Docker & Docker Compose** - For production deployment
3. **Ollama** - For local LLM processing (optional)
4. **Azure OpenAI** - For cloud LLM processing (optional)

## 🎉 **Success Metrics**

- ✅ **Fast Loading** - Handles 10k+ posts efficiently
- ✅ **Responsive UI** - Smooth interactions and real-time updates
- ✅ **Data Integrity** - Maintains data quality and validation
- ✅ **Export Functionality** - Reliable data export capabilities
- ✅ **Cross-platform** - Works on Windows, macOS, and Linux
- ✅ **Format Compatibility** - Works with both old and new data structures
- ✅ **RAG Integration** - Seamless AI-powered search experience

## 🚀 **Getting Started**

1. **Run the Scraper**:
   ```bash
   python complete_linkedin_scraper_enhanced_fast.py --posts 50 --speed fast
   ```

2. **Start the Production System**:
   ```bash
   ./start_production.sh
   ```

3. **Explore Your Data**:
   - Select your data export from the sidebar
   - Browse through Overview, Data Grid, Card View, and Analytics tabs
   - Use RAG Search for AI-powered queries
   - Export filtered data as needed

## 🔧 **Configuration**

### **Environment Variables**
```bash
# RAG API Configuration
RAG_API_URL=http://rag-api:8000

# Streamlit Configuration
STREAMLIT_PORT=8501
STREAMLIT_SERVER_PORT=8501
```

### **Docker Configuration**
The UI is containerized with:
- **Base Image**: Python 3.11-slim
- **Dependencies**: Streamlit, Polars, httpx, streamlit-aggrid
- **Port**: 8501
- **Health Check**: Automatic monitoring

## 📊 **Performance**

### **Optimizations**
- **Lazy Loading**: Data loaded on-demand
- **Caching**: Streamlit caching for repeated operations
- **Pagination**: Efficient handling of large datasets
- **Background Processing**: Non-blocking operations

### **Scalability**
- **Horizontal Scaling**: Multiple UI instances possible
- **Load Balancing**: Ready for production load balancers
- **Resource Management**: Efficient memory and CPU usage

---

**Ready for production data exploration!** 🚀📊🤖
