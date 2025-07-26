#!/usr/bin/env python3
"""
RAG Environment Verification Script

Check if the RAG system environment is properly configured.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple


def print_banner():
    """Print verification banner."""
    print("=" * 60)
    print("🔍 RAG Environment Verification")
    print("=" * 60)
    print()


def check_env_file() -> Tuple[bool, Dict[str, str]]:
    """Check if .env file exists and load configuration."""
    env_path = Path(".env")
    
    if not env_path.exists():
        print("❌ .env file not found!")
        print("   Run: python setup_env.py")
        return False, {}
    
    print("✅ .env file found")
    
    # Load environment variables
    env_vars = {}
    try:
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()
        
        print(f"✅ Loaded {len(env_vars)} environment variables")
        return True, env_vars
        
    except Exception as e:
        print(f"❌ Failed to load .env file: {e}")
        return False, {}


def check_required_vars(env_vars: Dict[str, str]) -> List[str]:
    """Check for required environment variables."""
    required_vars = [
        'RAG_API_URL',
        'RAG_LLM_PROVIDER',
        'RAG_EMBEDDING_MODEL',
        'RAG_VECTOR_STORE_PATH',
        'RAG_LLM_TEMPERATURE',
        'RAG_LLM_MAX_TOKENS'
    ]
    
    missing_vars = []
    for var in required_vars:
        if var not in env_vars:
            missing_vars.append(var)
        else:
            print(f"✅ {var}: {env_vars[var]}")
    
    return missing_vars


def check_llm_config(env_vars: Dict[str, str]) -> bool:
    """Check LLM provider configuration."""
    provider = env_vars.get('RAG_LLM_PROVIDER', '').lower()
    
    if provider == 'ollama':
        print("🤖 Ollama Configuration:")
        ollama_vars = ['OLLAMA_BASE_URL', 'OLLAMA_MODEL']
        for var in ollama_vars:
            if var in env_vars:
                print(f"   ✅ {var}: {env_vars[var]}")
            else:
                print(f"   ❌ {var}: Missing")
                return False
        return True
        
    elif provider == 'azure':
        print("🤖 Azure OpenAI Configuration:")
        azure_vars = ['AZURE_OPENAI_ENDPOINT', 'AZURE_OPENAI_API_KEY', 'AZURE_OPENAI_DEPLOYMENT']
        for var in azure_vars:
            if var in env_vars:
                value = env_vars[var]
                if 'your-' in value or value == '':
                    print(f"   ⚠️  {var}: Not configured (using placeholder)")
                else:
                    print(f"   ✅ {var}: Configured")
            else:
                print(f"   ❌ {var}: Missing")
                return False
        return True
        
    else:
        print(f"❌ Invalid LLM provider: {provider}")
        return False


def check_docker_files() -> bool:
    """Check if Docker files exist."""
    print("\n🐳 Docker Configuration:")
    
    docker_files = [
        ('docker-compose.yml', 'Docker Compose configuration'),
        ('rag_api/Dockerfile', 'RAG API Dockerfile'),
        ('ui_feed_explorer/Dockerfile', 'Streamlit UI Dockerfile')
    ]
    
    all_exist = True
    for file_path, description in docker_files:
        if Path(file_path).exists():
            print(f"   ✅ {description}")
        else:
            print(f"   ❌ {description}: {file_path} not found")
            all_exist = False
    
    return all_exist


def check_rag_components() -> bool:
    """Check if RAG components exist."""
    print("\n🔧 RAG Components:")
    
    rag_files = [
        ('rag_api/main.py', 'RAG API main file'),
        ('rag_api/rag/__init__.py', 'RAG package init'),
        ('rag_api/rag/core/__init__.py', 'RAG core package'),
        ('rag_api/rag/core/config.py', 'RAG configuration'),
        ('rag_api/rag/core/rag_manager.py', 'RAG manager'),
        ('rag_api/rag/api/health_api.py', 'Health API')
    ]
    
    all_exist = True
    for file_path, description in rag_files:
        if Path(file_path).exists():
            print(f"   ✅ {description}")
        else:
            print(f"   ❌ {description}: {file_path} not found")
            all_exist = False
    
    return all_exist


def check_data_directory() -> bool:
    """Check if data directory exists."""
    print("\n📁 Data Directory:")
    
    data_dir = Path("./data")
    if data_dir.exists():
        print(f"   ✅ Data directory exists: {data_dir}")
        
        # Check for data files
        data_files = list(data_dir.glob("posts_*"))
        if data_files:
            print(f"   ✅ Found {len(data_files)} data export directories")
            for data_file in data_files[:3]:  # Show first 3
                print(f"      • {data_file.name}")
            if len(data_files) > 3:
                print(f"      • ... and {len(data_files) - 3} more")
        else:
            print("   ⚠️  No data export directories found")
            print("      Run the LinkedIn scraper first to generate data")
        
        return True
    else:
        print(f"   ❌ Data directory not found: {data_dir}")
        print("      Create it with: mkdir -p ./data")
        return False


def check_ollama_connection() -> bool:
    """Check Ollama connection (if configured)."""
    import subprocess
    import json
    
    print("\n🔗 Ollama Connection:")
    
    try:
        # Check if ollama is running
        result = subprocess.run(['curl', '-s', 'http://localhost:11434/api/tags'], 
                              capture_output=True, text=True, timeout=5)
        
        if result.returncode == 0:
            try:
                models = json.loads(result.stdout)
                print("   ✅ Ollama is running")
                if 'models' in models:
                    model_names = [model.get('name', '') for model in models['models']]
                    print(f"   ✅ Available models: {', '.join(model_names)}")
                return True
            except json.JSONDecodeError:
                print("   ⚠️  Ollama is running but response format is unexpected")
                return True
        else:
            print("   ❌ Ollama is not running")
            print("      Start with: ollama serve")
            return False
            
    except subprocess.TimeoutExpired:
        print("   ❌ Ollama connection timeout")
        return False
    except FileNotFoundError:
        print("   ❌ curl not found (Ollama check skipped)")
        return True
    except Exception as e:
        print(f"   ❌ Ollama check failed: {e}")
        return False


def main():
    """Main verification function."""
    print_banner()
    
    # Check .env file
    env_exists, env_vars = check_env_file()
    if not env_exists:
        sys.exit(1)
    
    print()
    
    # Check required variables
    print("📋 Required Environment Variables:")
    missing_vars = check_required_vars(env_vars)
    if missing_vars:
        print(f"❌ Missing required variables: {', '.join(missing_vars)}")
        sys.exit(1)
    
    # Check LLM configuration
    llm_ok = check_llm_config(env_vars)
    if not llm_ok:
        print("❌ LLM configuration is incomplete")
        sys.exit(1)
    
    # Check Docker files
    docker_ok = check_docker_files()
    
    # Check RAG components
    rag_ok = check_rag_components()
    
    # Check data directory
    data_ok = check_data_directory()
    
    # Check Ollama (if using Ollama)
    ollama_ok = True
    if env_vars.get('RAG_LLM_PROVIDER', '').lower() == 'ollama':
        ollama_ok = check_ollama_connection()
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Verification Summary:")
    print("=" * 60)
    
    checks = [
        ("Environment File", env_exists),
        ("Required Variables", len(missing_vars) == 0),
        ("LLM Configuration", llm_ok),
        ("Docker Files", docker_ok),
        ("RAG Components", rag_ok),
        ("Data Directory", data_ok),
        ("Ollama Connection", ollama_ok)
    ]
    
    all_passed = True
    for check_name, passed in checks:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {status} {check_name}")
        if not passed:
            all_passed = False
    
    print()
    
    if all_passed:
        print("🎉 All checks passed! Your RAG environment is ready.")
        print("\n🚀 Next Steps:")
        print("   1. Start the system: ./start_production.sh")
        print("   2. Access the UI: http://localhost:8501")
        print("   3. Access the API: http://localhost:8000")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print("\n🔧 Common fixes:")
        print("   • Run: python setup_env.py")
        print("   • Install Ollama: curl -fsSL https://ollama.ai/install.sh | sh")
        print("   • Start Ollama: ollama serve")
        print("   • Pull model: ollama pull mistral-nemo:12b")
        sys.exit(1)


if __name__ == "__main__":
    main() 