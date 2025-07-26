#!/usr/bin/env python3
"""
Environment Setup Script

Interactive script to create .env file with all required configuration for the RAG system.
"""

import os
import sys
from pathlib import Path


def print_banner():
    """Print setup banner."""
    print("=" * 60)
    print("🚀 LinkedIn Feed Explorer - Environment Setup")
    print("=" * 60)
    print()


def get_user_input(prompt: str, default: str = "", required: bool = True) -> str:
    """Get user input with validation."""
    while True:
        if default:
            user_input = input(f"{prompt} [{default}]: ").strip()
            if not user_input:
                user_input = default
        else:
            user_input = input(f"{prompt}: ").strip()
        
        if not required or user_input:
            return user_input
        else:
            print("❌ This field is required. Please provide a value.")


def create_env_file():
    """Create .env file with user configuration."""
    print_banner()
    
    # Check if .env already exists
    env_path = Path(".env")
    if env_path.exists():
        overwrite = input("⚠️  .env file already exists. Overwrite? (y/N): ").strip().lower()
        if overwrite != 'y':
            print("❌ Setup cancelled.")
            return False
    
    print("📋 Let's configure your RAG system environment...")
    print()
    
    # LLM Provider Selection
    print("🤖 LLM Provider Configuration")
    print("-" * 30)
    provider = get_user_input(
        "Choose LLM provider (ollama/azure)",
        default="ollama",
        required=True
    ).lower()
    
    if provider not in ["ollama", "azure"]:
        print("❌ Invalid provider. Must be 'ollama' or 'azure'.")
        return False
    
    # Build environment configuration
    env_config = []
    env_config.append("# =============================================================================")
    env_config.append("# LinkedIn Feed Explorer - RAG System Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    
    # RAG API Configuration
    env_config.append("# RAG API Configuration")
    env_config.append("RAG_API_URL=http://localhost:8000")
    env_config.append("")
    
    # LLM Provider Configuration
    env_config.append("# =============================================================================")
    env_config.append("# LLM Provider Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    env_config.append(f"# Primary LLM Provider (ollama or azure)")
    env_config.append(f"RAG_LLM_PROVIDER={provider}")
    env_config.append("")
    
    if provider == "ollama":
        # Ollama Configuration
        env_config.append("# =============================================================================")
        env_config.append("# Ollama Configuration (Local LLM)")
        env_config.append("# =============================================================================")
        env_config.append("")
        env_config.append("# Ollama base URL (host-based, not containerized)")
        env_config.append("OLLAMA_BASE_URL=http://host.docker.internal:11434")
        env_config.append("")
        env_config.append("# Ollama model to use")
        ollama_model = get_user_input(
            "Ollama model name",
            default="llama3.1:8b",
            required=True
        )
        env_config.append(f"OLLAMA_MODEL={ollama_model}")
        env_config.append("")
        
        # Azure placeholder
        env_config.append("# =============================================================================")
        env_config.append("# Azure OpenAI Configuration (Alternative to Ollama)")
        env_config.append("# =============================================================================")
        env_config.append("")
        env_config.append("# Azure OpenAI endpoint (optional - only if using Azure)")
        env_config.append("AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/")
        env_config.append("")
        env_config.append("# Azure OpenAI API key (optional - only if using Azure)")
        env_config.append("AZURE_OPENAI_API_KEY=your-azure-openai-api-key")
        env_config.append("")
        env_config.append("# Azure OpenAI deployment name (optional - only if using Azure)")
        env_config.append("AZURE_OPENAI_DEPLOYMENT=your-deployment-name")
        env_config.append("")
        
    else:
        # Azure Configuration
        env_config.append("# =============================================================================")
        env_config.append("# Ollama Configuration (Local LLM)")
        env_config.append("# =============================================================================")
        env_config.append("")
        env_config.append("# Ollama base URL (host-based, not containerized)")
        env_config.append("OLLAMA_BASE_URL=http://host.docker.internal:11434")
        env_config.append("")
        env_config.append("# Ollama model to use")
        env_config.append("OLLAMA_MODEL=llama3.1:8b")
        env_config.append("")
        
        env_config.append("# =============================================================================")
        env_config.append("# Azure OpenAI Configuration (Alternative to Ollama)")
        env_config.append("# =============================================================================")
        env_config.append("")
        env_config.append("# Azure OpenAI endpoint (optional - only if using Azure)")
        azure_endpoint = get_user_input(
            "Azure OpenAI endpoint URL",
            required=True
        )
        env_config.append(f"AZURE_OPENAI_ENDPOINT={azure_endpoint}")
        env_config.append("")
        env_config.append("# Azure OpenAI API key (optional - only if using Azure)")
        azure_key = get_user_input(
            "Azure OpenAI API key",
            required=True
        )
        env_config.append(f"AZURE_OPENAI_API_KEY={azure_key}")
        env_config.append("")
        env_config.append("# Azure OpenAI deployment name (optional - only if using Azure)")
        azure_deployment = get_user_input(
            "Azure OpenAI deployment name",
            required=True
        )
        env_config.append(f"AZURE_OPENAI_DEPLOYMENT={azure_deployment}")
        env_config.append("")
    
    # RAG System Configuration
    env_config.append("# =============================================================================")
    env_config.append("# RAG System Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    env_config.append("# Embedding model for text vectorization")
    embedding_model = get_user_input(
        "Embedding model name",
        default="all-MiniLM-L6-v2",
        required=True
    )
    env_config.append(f"RAG_EMBEDDING_MODEL={embedding_model}")
    env_config.append("")
    env_config.append("# Vector store persistence path")
    env_config.append("RAG_VECTOR_STORE_PATH=/app/vector_store")
    env_config.append("")
    env_config.append("# LLM generation parameters")
    temperature = get_user_input(
        "LLM temperature (0.0-1.0)",
        default="0.1",
        required=True
    )
    env_config.append(f"RAG_LLM_TEMPERATURE={temperature}")
    max_tokens = get_user_input(
        "LLM max tokens",
        default="2048",
        required=True
    )
    env_config.append(f"RAG_LLM_MAX_TOKENS={max_tokens}")
    env_config.append("")
    
    # Streamlit Configuration
    env_config.append("# =============================================================================")
    env_config.append("# Streamlit Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    env_config.append("# Streamlit server configuration")
    env_config.append("STREAMLIT_SERVER_PORT=8501")
    env_config.append("STREAMLIT_SERVER_ADDRESS=0.0.0.0")
    env_config.append("")
    
    # Docker Configuration
    env_config.append("# =============================================================================")
    env_config.append("# Docker Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    env_config.append("# Docker network configuration")
    env_config.append("DOCKER_NETWORK_NAME=linkedin-network")
    env_config.append("")
    
    # Data Configuration
    env_config.append("# =============================================================================")
    env_config.append("# Data Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    env_config.append("# Data directory path (relative to project root)")
    env_config.append("DATA_DIRECTORY=./data")
    env_config.append("")
    
    # Performance Configuration
    env_config.append("# =============================================================================")
    env_config.append("# Performance Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    env_config.append("# Maximum number of results for RAG queries")
    max_results = get_user_input(
        "Max RAG results",
        default="10",
        required=True
    )
    env_config.append(f"RAG_MAX_RESULTS={max_results}")
    env_config.append("")
    env_config.append("# Batch size for indexing")
    batch_size = get_user_input(
        "Indexing batch size",
        default="100",
        required=True
    )
    env_config.append(f"RAG_BATCH_SIZE={batch_size}")
    env_config.append("")
    
    # Security Configuration
    env_config.append("# =============================================================================")
    env_config.append("# Security Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    env_config.append("# CORS origins (comma-separated)")
    env_config.append("CORS_ORIGINS=http://localhost:8501,http://127.0.0.1:8501")
    env_config.append("")
    
    # Logging Configuration
    env_config.append("# =============================================================================")
    env_config.append("# Logging Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    env_config.append("# Log level (DEBUG, INFO, WARNING, ERROR)")
    log_level = get_user_input(
        "Log level",
        default="INFO",
        required=True
    )
    env_config.append(f"LOG_LEVEL={log_level}")
    env_config.append("")
    
    # Health Check Configuration
    env_config.append("# =============================================================================")
    env_config.append("# Health Check Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    env_config.append("# Health check interval (seconds)")
    env_config.append("HEALTH_CHECK_INTERVAL=30")
    env_config.append("")
    env_config.append("# Health check timeout (seconds)")
    env_config.append("HEALTH_CHECK_TIMEOUT=10")
    env_config.append("")
    
    # Backup Configuration
    env_config.append("# =============================================================================")
    env_config.append("# Backup Configuration")
    env_config.append("# =============================================================================")
    env_config.append("")
    env_config.append("# Enable automatic backups")
    env_config.append("ENABLE_BACKUPS=true")
    env_config.append("")
    env_config.append("# Backup retention days")
    env_config.append("BACKUP_RETENTION_DAYS=30")
    
    # Write .env file
    try:
        with open(env_path, 'w') as f:
            f.write('\n'.join(env_config))
        
        print()
        print("✅ .env file created successfully!")
        print()
        print("📋 Configuration Summary:")
        print(f"   • LLM Provider: {provider}")
        if provider == "ollama":
            print(f"   • Ollama Model: {ollama_model}")
        else:
            print(f"   • Azure Endpoint: {azure_endpoint}")
            print(f"   • Azure Deployment: {azure_deployment}")
        print(f"   • Embedding Model: {embedding_model}")
        print(f"   • Max Results: {max_results}")
        print(f"   • Log Level: {log_level}")
        print()
        print("🚀 Next Steps:")
        print("   1. Review the .env file: cat .env")
        print("   2. Start the system: ./start_production.sh")
        print("   3. Access the UI: http://localhost:8501")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False


def main():
    """Main function."""
    try:
        success = create_env_file()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n❌ Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 