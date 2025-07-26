# 🔧 Scripts & Tools Reference

**Complete documentation for all scripts, tools, and utilities in the LinkedIn Feed RAG Project**

## 📋 **Table of Contents**

1. [Setup & Configuration Scripts](#-setup--configuration-scripts)
2. [Testing & Debugging Scripts](#-testing--debugging-scripts)
3. [Development Scripts](#-development-scripts)
4. [Production Scripts](#-production-scripts)
5. [Utility Scripts](#-utility-scripts)
6. [Command Reference](#-command-reference)

---

## 🛠️ **Setup & Configuration Scripts**

### **`setup_env.py` - Environment Configuration**

**Purpose**: Interactive environment setup for the RAG system

**Usage**:
```bash
python setup_env.py
```

**What it does**:
- Prompts for LLM provider preference (Ollama/Azure)
- Configures model settings and parameters
- Sets up API endpoints and URLs
- Creates `.env` file with all required variables
- Validates configuration completeness

**Interactive Prompts**:
```
🤖 LLM Provider Configuration
Choose LLM provider (ollama/azure) [ollama]: 
Ollama model name [mistral-nemo:12b]: 
Temperature for LLM (0.0-1.0) [0.1]: 
Max tokens for responses [2048]: 
```

**Output**:
- Creates `.env` file with complete configuration
- Validates all required variables are present
- Provides setup confirmation

**Example Output**:
```
✅ Environment file created successfully!
📋 Configuration Summary:
   • LLM Provider: ollama
   • Model: mistral-nemo:12b
   • Temperature: 0.1
   • Max Tokens: 2048
   • API URL: http://localhost:8000

🚀 Next Steps:
   1. Start Ollama: ollama serve
   2. Pull model: ollama pull mistral-nemo:12b
   3. Verify setup: python verify_rag_env.py
```

---

### **`verify_rag_env.py` - Environment Verification**

**Purpose**: Comprehensive verification of RAG system environment

**Usage**:
```bash
python verify_rag_env.py
```

**What it checks**:
- `.env` file existence and content
- Required environment variables
- Docker files availability
- RAG components presence
- Data directory structure
- Ollama connection status

**Verification Categories**:

#### **Environment File Check**
```bash
✅ .env file found
✅ Loaded 33 environment variables
```

#### **Required Variables Check**
```bash
✅ RAG_API_URL: http://localhost:8000
✅ RAG_LLM_PROVIDER: ollama
✅ RAG_EMBEDDING_MODEL: all-MiniLM-L6-v2
✅ RAG_VECTOR_STORE_PATH: /app/vector_store
✅ RAG_LLM_TEMPERATURE: 0.1
✅ RAG_LLM_MAX_TOKENS: 2048
```

#### **LLM Configuration Check**
```bash
🤖 Ollama Configuration:
   ✅ OLLAMA_BASE_URL: http://host.docker.internal:11434
   ✅ OLLAMA_MODEL: mistral-nemo:12b
```

#### **Docker Configuration Check**
```bash
🐳 Docker Configuration:
   ✅ Docker Compose configuration
   ✅ RAG API Dockerfile
   ✅ Streamlit UI Dockerfile
```

#### **RAG Components Check**
```bash
🔧 RAG Components:
   ✅ RAG API main file
   ✅ RAG package init
   ✅ RAG core package
   ✅ RAG configuration
   ✅ RAG manager
   ✅ Health API
```

#### **Data Directory Check**
```bash
📁 Data Directory:
   ✅ Data directory exists: data
   ✅ Found 1 data export directories
      • posts_37_fast_fast_2025-07-25_22-45
```

#### **Ollama Connection Check**
```bash
🔗 Ollama Connection:
   ✅ Ollama is running
   ✅ Available models: mistral-nemo:latest, codellama:34b, ...
```

**Example Complete Output**:
```
============================================================
🔍 RAG Environment Verification
============================================================

✅ .env file found
✅ Loaded 33 environment variables

📋 Required Environment Variables:
✅ RAG_API_URL: http://localhost:8000
✅ RAG_LLM_PROVIDER: ollama
✅ RAG_EMBEDDING_MODEL: all-MiniLM-L6-v2
✅ RAG_VECTOR_STORE_PATH: /app/vector_store
✅ RAG_LLM_TEMPERATURE: 0.1
✅ RAG_LLM_MAX_TOKENS: 2048

🤖 Ollama Configuration:
   ✅ OLLAMA_BASE_URL: http://host.docker.internal:11434
   ✅ OLLAMA_MODEL: mistral-nemo:12b

🐳 Docker Configuration:
   ✅ Docker Compose configuration
   ✅ RAG API Dockerfile
   ✅ Streamlit UI Dockerfile

🔧 RAG Components:
   ✅ RAG API main file
   ✅ RAG package init
   ✅ RAG core package
   ✅ RAG configuration
   ✅ RAG manager
   ✅ Health API

📁 Data Directory:
   ✅ Data directory exists: data
   ✅ Found 1 data export directories
      • posts_37_fast_fast_2025-07-25_22-45

🔗 Ollama Connection:
   ✅ Ollama is running
   ✅ Available models: mistral-nemo:latest, codellama:34b, ...

============================================================
📊 Verification Summary:
============================================================
   ✅ PASS Environment File
   ✅ PASS Required Variables
   ✅ PASS LLM Configuration
   ✅ PASS Docker Files
   ✅ PASS RAG Components
   ✅ PASS Data Directory
   ✅ PASS Ollama Connection

🎉 All checks passed! Your RAG environment is ready.

🚀 Next Steps:
   1. Start the system: ./start_production.sh
   2. Access the UI: http://localhost:8501
   3. Access the API: http://localhost:8000
```

---

## 🧪 **Testing & Debugging Scripts**

### **`debug_rag_system.py` - RAG System Testing**

**Purpose**: Comprehensive testing of RAG system components

**Usage**:
```bash
python debug_rag_system.py
```

**What it tests**:
- API health endpoints
- Data loading from files
- Vector indexing process
- RAG query functionality
- Collection management
- System performance

**Test Categories**:

#### **1. API Health Test**
```bash
🔍 Testing RAG API Health...
✅ Health Check: {
  "status": "healthy",
  "components": {
    "rag_manager": {"status": "healthy", "details": {...}},
    "system_ready": {"status": "healthy", "ready": true}
  },
  "timestamp": "2025-07-26T07:10:29.640900"
}
```

#### **2. API Ready Test**
```bash
🔍 Testing RAG API Ready...
✅ Ready Check: {"status": "ready"}
```

#### **3. Data Loading Test**
```bash
🔍 Testing Data Loading...
📁 Using data directory: data/posts_37_fast_fast_2025-07-25_22-45
📄 Using JSON file: data/posts_37_fast_fast_2025-07-25_22-45/linkedin_feed_fast_fast_20250725_224507.json
✅ Loaded 37 posts from JSON

📊 Content samples (first 10 posts):
  1. 🔴 🎉 sourcelair mafia on #mikrikouventa 🎉 🎥
  2. download our free ebook to discover how agentic ai can transform...
  3. damnn… openai, google & anthropic just dropped their internal ai playbooks...
  ...

🎯 Found 4 posts mentioning OpenAI:
  Post 3: damnn… openai, google & anthropic just dropped their internal ai playbooks...
  Post 6: testing chatgpt vs photoshop for photo editing led to some surprising results...
  Post 8: how to build an ai agent using n8n...
  Post 10: this is the best video i've seen about llms in 2025...
```

#### **4. Collections Test**
```bash
🔍 Testing Collections...
✅ Collections: {"collections": ["linkedin_posts"]}
```

#### **5. Data Indexing Test**
```bash
🔍 Testing Data Indexing...
📤 Sending indexing request: {
  "data_path": "data/posts_37_fast_fast_2025-07-25_22-45",
  "collection_name": "test_collection"
}
✅ Indexing Response: {
  "message": "Indexing started",
  "data_path": "data/posts_37_fast_fast_2025-07-25_22-45",
  "collection": "test_collection"
}
```

#### **6. Collection Stats Test**
```bash
🔍 Testing Collection Stats for 'test_collection'...
✅ Collection Stats: {
  "collection": "test_collection",
  "stats": {
    "collection_name": "test_collection",
    "document_count": 100,
    "embedding_dimension": 384,
    "index_type": "hnsw"
  }
}
```

#### **7. RAG Query Test**
```bash
🔍 Testing RAG Query: 'find me posts about openAI'
📤 Sending query request: {
  "query": "find me posts about openAI",
  "collection_name": "test_collection",
  "max_results": 5
}
✅ Query Response: {
  "query": "find me posts about openAI",
  "answer": "Based on the provided context, here's what I found: ...",
  "sources": [
    {
      "content": "Check out & follow the new official LinkedIn page for OpenAI...",
      "metadata": {...},
      "similarity_score": 0.5439465641975403
    },
    ...
  ],
  "metadata": {...}
}
```

**Complete Test Summary**:
```
============================================================
📊 TEST SUMMARY
============================================================
✅ API Health: PASSED
✅ API Ready: PASSED
✅ Data Loading: PASSED
✅ Collections: PASSED
✅ Data Indexing: PASSED
✅ Collection Stats: PASSED
✅ RAG Query: PASSED

🔍 Query Analysis for 'find me posts about openAI':
📝 Answer: Based on the provided context, here's what I found: ...
📚 Sources: 5 found
  Source 1: Check out & follow the new official LinkedIn page for OpenAI...
  Source 2: damnn… OpenAI, Google & Anthropic just dropped their internal AI playbooks...
  Source 3: How to build an AI agent using n8n...
  ...
```

---

### **`simple_linkedin_test.py` - LinkedIn Connection Test**

**Purpose**: Basic LinkedIn connectivity and credential testing

**Usage**:
```bash
python simple_linkedin_test.py
```

**What it tests**:
- Credential validity
- Network connectivity
- Login success
- Basic scraping capability

**Test Process**:
```bash
🔍 Testing LinkedIn Connection...
📋 Loading credentials from .env file
🌐 Testing network connectivity
🔐 Attempting LinkedIn login
✅ Login successful
📊 Testing basic scraping capability
✅ Scraping test successful
```

**Example Output**:
```
============================================================
🔍 LinkedIn Connection Test
============================================================

📋 Credentials loaded successfully
🌐 Network connectivity: OK
🔐 LinkedIn login: SUCCESS
📊 Basic scraping test: PASSED

✅ All tests passed! LinkedIn connection is working.
```

---

### **`test_linkedin_connection.py` - Advanced Connection Test**

**Purpose**: Comprehensive LinkedIn connection and scraping testing

**Usage**:
```bash
python test_linkedin_connection.py
```

**What it tests**:
- Authentication flow
- Session management
- Rate limiting
- Error handling
- Advanced scraping features

**Advanced Test Features**:
```bash
🔍 Advanced LinkedIn Connection Test
============================================================

📋 Authentication Flow Test:
✅ Credential validation
✅ Login process
✅ Session creation
✅ Cookie management

🌐 Network & Session Test:
✅ Connection stability
✅ Session persistence
✅ Rate limit detection
✅ Error recovery

📊 Scraping Capability Test:
✅ Basic post extraction
✅ Engagement data parsing
✅ Author information
✅ Timestamp handling

🔧 Error Handling Test:
✅ Network timeout handling
✅ Authentication failure recovery
✅ Rate limit handling
✅ Invalid data handling
```

---

## 🔧 **Development Scripts**

### **`setup_credentials.py` - Credential Setup**

**Purpose**: Secure LinkedIn credential configuration

**Usage**:
```bash
python setup_credentials.py
```

**Interactive Setup**:
```bash
============================================================
🔐 LinkedIn Credential Setup
============================================================

📧 LinkedIn Email: your-email@example.com
🔑 LinkedIn Password: ********
✅ Credentials saved securely

🚀 Next Steps:
   1. Test connection: python simple_linkedin_test.py
   2. Start scraping: python complete_linkedin_scraper.py
```

**Security Features**:
- Encrypted credential storage
- Environment variable configuration
- Secure file permissions
- Validation and testing

---

### **`setup_conda_env.sh` - Conda Environment Setup**

**Purpose**: Complete development environment setup

**Usage**:
```bash
./setup_conda_env.sh
```

**What it creates**:
- Conda environment: `linkedin-feed-capture`
- Installs all dependencies
- Configures Python path
- Sets up development tools

**Setup Process**:
```bash
🚀 Setting up Conda Environment...
📦 Creating environment: linkedin-feed-capture
🔧 Installing dependencies...
✅ Environment setup complete

🎯 Next Steps:
   1. Activate environment: conda activate linkedin-feed-capture
   2. Verify installation: python verify_env.py
   3. Start development: python complete_linkedin_scraper.py
```

---

## 🚀 **Production Scripts**

### **`start_production.sh` - Automated Production Startup**

**Purpose**: Complete production system initialization

**Usage**:
```bash
./start_production.sh
```

**What it does**:
- Checks Docker and Docker Compose
- Verifies Ollama installation and models
- Creates data directory if needed
- Sets up environment file
- Builds and starts Docker services
- Performs health checks
- Shows access information

**Complete Process**:
```bash
🚀 LinkedIn Feed Explorer - Production Start Script
==================================================

[INFO] Checking Docker...
[SUCCESS] Docker is running

[INFO] Checking Docker Compose...
[SUCCESS] Docker Compose is available

[INFO] Checking Ollama...
[SUCCESS] Ollama is running

[INFO] Checking Ollama model...
[SUCCESS] Model mistral-nemo:12b is available

[INFO] Checking data directory...
[SUCCESS] Data directory exists

[INFO] Checking environment configuration...
[SUCCESS] Environment file exists

[INFO] Building and starting services...
[INFO] Building Docker images...
[INFO] Starting services...
[INFO] Waiting for services to be ready...
[INFO] Checking service health...
[SUCCESS] RAG API is healthy
[SUCCESS] Streamlit UI is healthy

🎉 LinkedIn Feed Explorer is now running!

📱 Access Points:
   • Streamlit UI: http://localhost:8501
   • RAG API: http://localhost:8000
   • API Documentation: http://localhost:8000/docs

🔧 Management Commands:
   • View logs: docker-compose logs -f
   • Stop services: docker-compose down
   • Restart services: docker-compose restart
   • Check status: docker-compose ps

📚 Documentation:
   • Production Guide: PRODUCTION_DEPLOYMENT.md
```

---

## 🛠️ **Utility Scripts**

### **`verify_env.py` - Environment Verification**

**Purpose**: Basic environment verification for development

**Usage**:
```bash
python verify_env.py
```

**What it checks**:
- Python environment
- Required packages
- Basic configuration
- Development tools

---

### **`demo.py` - Demo Application**

**Purpose**: Demonstration of core functionality

**Usage**:
```bash
python demo.py
```

**Features**:
- Basic scraping demonstration
- Data processing examples
- Export functionality
- Performance metrics

---

### **`example.py` - Code Examples**

**Purpose**: Example code snippets and usage patterns

**Usage**:
```bash
python example.py
```

**Examples**:
- Basic scraping setup
- Data processing patterns
- API integration
- Custom configurations

---

## 📋 **Command Reference**

### **Quick Commands**

#### **Setup Commands**
```bash
# Environment setup
python setup_env.py                    # Interactive environment setup
python verify_rag_env.py               # Verify RAG environment
./setup_conda_env.sh                   # Setup conda environment
python setup_credentials.py            # Setup LinkedIn credentials
```

#### **Testing Commands**
```bash
# System testing
python debug_rag_system.py             # Comprehensive RAG testing
python simple_linkedin_test.py         # LinkedIn connection test
python test_linkedin_connection.py     # Advanced LinkedIn testing
python verify_env.py                   # Basic environment verification
```

#### **Production Commands**
```bash
# Production management
./start_production.sh                  # Start production system
docker-compose up -d                   # Start services
docker-compose down                    # Stop services
docker-compose logs -f                 # View logs
docker-compose ps                      # Check status
```

#### **Scraping Commands**
```bash
# LinkedIn scraping
python complete_linkedin_scraper_enhanced_fast.py --posts 100
python complete_linkedin_scraper.py --posts 50
python complete_linkedin_scraper.py --posts 5 --no-headless --verbose
```

### **Advanced Commands**

#### **Development Commands**
```bash
# Development setup
conda activate linkedin-feed-capture
pip install -r requirements.txt
pip install -e .

# Code quality
ruff check .
ruff format .
mypy .
pytest tests/ -v
```

#### **Debugging Commands**
```bash
# Service debugging
docker-compose logs rag-api
docker-compose logs streamlit-ui
docker-compose restart rag-api

# System debugging
curl http://localhost:8000/health
curl http://localhost:8501/_stcore/health
ollama list
```

#### **Data Management Commands**
```bash
# Data operations
ls -la data/
chmod -R 755 data/
python debug_rag_system.py

# API operations
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "test query", "collection_name": "linkedin_posts"}'
```

### **Troubleshooting Commands**

#### **Common Issues**
```bash
# Port conflicts
lsof -i :8000
lsof -i :8501
kill -9 <PID>

# Permission issues
sudo chown -R $USER:$USER ./data
chmod +x *.sh

# Service issues
docker-compose down
docker-compose up --build
```

#### **Health Checks**
```bash
# Quick health check
curl http://localhost:8000/health
curl http://localhost:8000/ready
curl http://localhost:8501/_stcore/health

# Comprehensive health check
python verify_rag_env.py
python debug_rag_system.py
```

---

## 📊 **Script Output Examples**

### **Successful Setup Output**
```
============================================================
🚀 LinkedIn Feed Explorer - Environment Setup
============================================================

📋 Let's configure your RAG system environment...

🤖 LLM Provider Configuration
Choose LLM provider (ollama/azure) [ollama]: ollama
Ollama model name [mistral-nemo:12b]: mistral-nemo:12b
Temperature for LLM (0.0-1.0) [0.1]: 0.1
Max tokens for responses [2048]: 2048

✅ Environment file created successfully!
📋 Configuration Summary:
   • LLM Provider: ollama
   • Model: mistral-nemo:12b
   • Temperature: 0.1
   • Max Tokens: 2048
   • API URL: http://localhost:8000

🚀 Next Steps:
   1. Start Ollama: ollama serve
   2. Pull model: ollama pull mistral-nemo:12b
   3. Verify setup: python verify_rag_env.py
```

### **Successful Testing Output**
```
🚀 Starting Comprehensive RAG System Debug Test
============================================================

1️⃣ Testing API Health...
✅ Health Check: {"status": "healthy", ...}

2️⃣ Testing API Ready...
✅ Ready Check: {"status": "ready"}

3️⃣ Testing Data Loading...
✅ Loaded 37 posts from JSON

4️⃣ Testing Collections...
✅ Collections: {"collections": ["linkedin_posts"]}

5️⃣ Testing Data Indexing...
✅ Indexing Response: {"message": "Indexing started", ...}

6️⃣ Testing Collection Stats...
✅ Collection Stats: {"collection": "test_collection", ...}

7️⃣ Testing RAG Query...
✅ Query Response: {"query": "find me posts about openAI", ...}

============================================================
📊 TEST SUMMARY
============================================================
✅ Passed: 7/7
❌ Failed: 0/7

🎉 ALL TESTS PASSED! RAG system is working correctly.
```

---

## 🎯 **Best Practices**

### **Script Usage Guidelines**

1. **Always verify environment first**:
   ```bash
   python verify_rag_env.py
   ```

2. **Test before production**:
   ```bash
   python debug_rag_system.py
   ```

3. **Use automated startup**:
   ```bash
   ./start_production.sh
   ```

4. **Monitor logs regularly**:
   ```bash
   docker-compose logs -f
   ```

5. **Check health endpoints**:
   ```bash
   curl http://localhost:8000/health
   ```

### **Troubleshooting Workflow**

1. **Check environment**: `python verify_rag_env.py`
2. **Test RAG system**: `python debug_rag_system.py`
3. **Check services**: `docker-compose ps`
4. **View logs**: `docker-compose logs -f`
5. **Restart if needed**: `docker-compose restart`

### **Development Workflow**

1. **Setup environment**: `./setup_conda_env.sh`
2. **Configure credentials**: `python setup_credentials.py`
3. **Test connection**: `python simple_linkedin_test.py`
4. **Start development**: `python complete_linkedin_scraper.py`

---

**All scripts are documented and ready for use!** 🚀📊🔧 