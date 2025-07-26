# 🚀 Production Deployment Guide

## Overview

This guide covers deploying the LinkedIn Feed Explorer with RAG capabilities using Docker Compose. The system consists of:

- **RAG API Service**: FastAPI-based service for AI-powered search
- **Streamlit UI**: Web interface for data exploration and RAG queries
- **Ollama Integration**: Local LLM support (host-based)
- **Azure OpenAI**: Cloud LLM alternative

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit UI  │    │   RAG API       │    │   Ollama        │
│   (Port 8501)   │◄──►│   (Port 8000)   │◄──►│   (Host:11434)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Volume   │    │ Vector Store    │    │ Azure OpenAI    │
│   (./data)      │    │ (Docker Volume) │    │ (Optional)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📋 Prerequisites

### 1. Docker & Docker Compose
```bash
# Install Docker Desktop or Docker Engine
# Ensure Docker Compose is available
docker --version
docker-compose --version
```

### 2. Ollama (for local LLM)
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the model
ollama pull mistral-nemo:12b

# Start Ollama service
ollama serve
```

### 3. Data Preparation
```bash
# Ensure your LinkedIn data is in the ./data directory
ls -la ./data/
# Should show: posts_20241201_120000/, posts_20241202_140000/, etc.
```

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <your-repo>
cd linkedInFeedRagProject

# Copy environment template
cp env.example .env

# Edit configuration
nano .env
```

### 2. Configure Environment
```bash
# Edit .env file with your settings
RAG_API_URL=http://localhost:8000
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral-nemo:12b
RAG_LLM_PROVIDER=ollama  # or azure
```

### 3. Start Services
```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

### 4. Access Applications
- **Streamlit UI**: http://localhost:8501
- **RAG API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🔧 Configuration Options

### LLM Provider Selection

#### Option 1: Ollama (Local)
```bash
# In .env file
RAG_LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral-nemo:12b
```

#### Option 2: Azure OpenAI
```bash
# In .env file
RAG_LLM_PROVIDER=azure
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
```

### RAG Configuration
```bash
# Embedding model
RAG_EMBEDDING_MODEL=all-MiniLM-L6-v2

# Vector store location
RAG_VECTOR_STORE_PATH=./vector_store

# Generation parameters
RAG_LLM_TEMPERATURE=0.1
RAG_LLM_MAX_TOKENS=2048
```

## 🐳 Docker Compose Services

### RAG API Service
- **Port**: 8000
- **Health Check**: `/health` endpoint
- **Dependencies**: Ollama or Azure OpenAI
- **Volumes**: Vector store, data directory

### Streamlit UI Service
- **Port**: 8501
- **Health Check**: Streamlit health endpoint
- **Dependencies**: RAG API service
- **Volumes**: Data directory (read-only)

## 🔍 Health Monitoring

### Check Service Health
```bash
# Overall health
docker-compose ps

# Individual service health
curl http://localhost:8000/health
curl http://localhost:8501/_stcore/health

# View logs
docker-compose logs rag-api
docker-compose logs streamlit-ui
```

### Health Check Endpoints
- **RAG API**: `GET /health` - Returns system status
- **RAG API**: `GET /ready` - Returns readiness status
- **Streamlit**: Built-in health monitoring

## 🔄 Operations

### Restart Services
```bash
# Restart all services
docker-compose restart

# Restart specific service
docker-compose restart rag-api
docker-compose restart streamlit-ui
```

### Update Configuration
```bash
# Update .env file
nano .env

# Restart services to apply changes
docker-compose restart
```

### Rebuild Services
```bash
# Rebuild after code changes
docker-compose build

# Rebuild specific service
docker-compose build rag-api
docker-compose build streamlit-ui
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f rag-api
docker-compose logs -f streamlit-ui

# Last 100 lines
docker-compose logs --tail=100 rag-api
```

## 🗄️ Data Management

### Indexing Data
1. **Via UI**: Use "Rebuild Index" button in Streamlit
2. **Via API**: `POST /index` endpoint
3. **Automatic**: Triggered when data is loaded

### Vector Store Location
- **Docker Volume**: `rag_vector_store`
- **Persistent**: Survives container restarts
- **Backup**: Volume can be backed up separately

### Data Directory
- **Location**: `./data/`
- **Format**: Auto-discovered export directories
- **Access**: Read-only in containers

## 🔒 Security Considerations

### Network Security
- Services communicate via Docker network
- Ollama runs on host (not in container)
- External access only via exposed ports

### Environment Variables
- Sensitive data in `.env` file
- Never commit `.env` to version control
- Use secrets management in production

### API Security
- CORS configured for development
- Add authentication for production
- Rate limiting recommended

## 🚨 Troubleshooting

### Common Issues

#### 1. Ollama Connection Failed
```bash
# Check Ollama is running
curl http://localhost:11434/api/tags

# Check model is available
ollama list

# Pull model if missing
ollama pull mistral-nemo:12b
```

#### 2. RAG API Not Starting
```bash
# Check logs
docker-compose logs rag-api

# Check environment variables
docker-compose exec rag-api env | grep RAG

# Restart service
docker-compose restart rag-api
```

#### 3. Streamlit UI Issues
```bash
# Check logs
docker-compose logs streamlit-ui

# Check RAG API connection
curl http://rag-api:8000/health

# Restart service
docker-compose restart streamlit-ui
```

#### 4. Data Not Loading
```bash
# Check data directory
ls -la ./data/

# Check volume mounts
docker-compose exec streamlit-ui ls -la /app/data/

# Verify file permissions
chmod -R 755 ./data/
```

### Performance Issues

#### 1. Slow Indexing
- Check available memory
- Reduce batch size in configuration
- Use SSD storage for vector store

#### 2. Slow Queries
- Check Ollama model performance
- Optimize embedding model
- Increase vector store resources

#### 3. UI Responsiveness
- Check browser performance
- Reduce data grid page size
- Enable pagination

## 📊 Monitoring & Metrics

### Available Metrics
- **RAG API**: `GET /metrics` - Performance metrics
- **Health Status**: Real-time health monitoring
- **Logs**: Structured logging for analysis

### Recommended Monitoring
- Service health checks
- Response time monitoring
- Error rate tracking
- Resource usage (CPU, memory, disk)

## 🔄 Backup & Recovery

### Backup Strategy
```bash
# Backup vector store
docker run --rm -v linkedin-rag_vector_store:/data -v $(pwd):/backup alpine tar czf /backup/vector_store_backup.tar.gz -C /data .

# Backup data directory
tar czf data_backup.tar.gz ./data/

# Backup configuration
cp .env .env.backup
```

### Recovery Process
```bash
# Restore vector store
docker run --rm -v linkedin-rag_vector_store:/data -v $(pwd):/backup alpine tar xzf /backup/vector_store_backup.tar.gz -C /data

# Restore data
tar xzf data_backup.tar.gz

# Restore configuration
cp .env.backup .env
```

## 🚀 Production Deployment

### Production Checklist
- [ ] Environment variables configured
- [ ] SSL/TLS certificates installed
- [ ] Authentication implemented
- [ ] Monitoring configured
- [ ] Backup strategy in place
- [ ] Log aggregation setup
- [ ] Resource limits configured
- [ ] Security scanning completed

### Scaling Considerations
- **Horizontal**: Multiple RAG API instances
- **Vertical**: Increase container resources
- **Caching**: Redis for query caching
- **Load Balancing**: Nginx or similar

## 📚 API Reference

### RAG API Endpoints
- `GET /` - Service information
- `GET /health` - Health check
- `GET /ready` - Readiness check
- `POST /query` - RAG query
- `POST /index` - Index data
- `GET /collections` - List collections
- `GET /collections/{name}/stats` - Collection stats
- `DELETE /collections/{name}` - Delete collection
- `POST /config` - Update configuration
- `GET /metrics` - Performance metrics

### Example API Usage
```bash
# Query RAG system
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the most discussed topics?", "max_results": 10}'

# Check health
curl http://localhost:8000/health

# List collections
curl http://localhost:8000/collections
```

## 🎯 Success Metrics

### Performance Targets
- **API Response Time**: < 5 seconds for RAG queries
- **UI Load Time**: < 3 seconds for initial load
- **Indexing Speed**: > 1000 documents/minute
- **Uptime**: > 99.9%

### Quality Metrics
- **Query Relevance**: > 80% user satisfaction
- **Answer Accuracy**: > 90% factual correctness
- **System Reliability**: < 1% error rate

---

**Ready for production deployment!** 🚀 