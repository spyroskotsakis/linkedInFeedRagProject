#!/bin/bash

# 🚀 LinkedIn Feed Explorer - Production Start Script

set -e

echo "🚀 Starting LinkedIn Feed Explorer Production System..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Docker is running
check_docker() {
    print_status "Checking Docker..."
    if ! docker info > /dev/null 2>&1; then
        print_error "Docker is not running. Please start Docker Desktop or Docker Engine."
        exit 1
    fi
    print_success "Docker is running"
}

# Check if Docker Compose is available
check_docker_compose() {
    print_status "Checking Docker Compose..."
    if ! docker-compose --version > /dev/null 2>&1; then
        print_error "Docker Compose is not available. Please install Docker Compose."
        exit 1
    fi
    print_success "Docker Compose is available"
}

# Check if Ollama is running
check_ollama() {
    print_status "Checking Ollama..."
    if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
        print_warning "Ollama is not running. Starting Ollama..."
        if command -v ollama > /dev/null 2>&1; then
            ollama serve &
            sleep 5
            if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
                print_success "Ollama started successfully"
            else
                print_error "Failed to start Ollama. Please start it manually: ollama serve"
                exit 1
            fi
        else
            print_error "Ollama is not installed. Please install Ollama first."
            print_status "Install with: curl -fsSL https://ollama.ai/install.sh | sh"
            exit 1
        fi
    else
        print_success "Ollama is running"
    fi
}

# Check if required model is available
check_ollama_model() {
    print_status "Checking Ollama model..."
    if ! ollama list | grep -q "mistral-nemo:12b"; then
        print_warning "Model mistral-nemo:12b not found. Pulling..."
        ollama pull mistral-nemo:12b
        print_success "Model pulled successfully"
    else
        print_success "Model mistral-nemo:12b is available"
    fi
}

# Check if data directory exists
check_data_directory() {
    print_status "Checking data directory..."
    if [ ! -d "./data" ]; then
        print_warning "Data directory not found. Creating..."
        mkdir -p ./data
        print_success "Data directory created"
    else
        print_success "Data directory exists"
    fi
}

# Check if environment file exists
check_environment() {
    print_status "Checking environment configuration..."
    if [ ! -f ".env" ]; then
        if [ -f "env.example" ]; then
            print_warning "Environment file not found. Creating from template..."
            cp env.example .env
            print_success "Environment file created from template"
            print_warning "Please edit .env file with your configuration"
        else
            print_error "Environment file not found and no template available"
            exit 1
        fi
    else
        print_success "Environment file exists"
    fi
}

# Build and start services
start_services() {
    print_status "Building and starting services..."
    
    # Stop any existing services
    docker-compose down 2>/dev/null || true
    
    # Build services
    print_status "Building Docker images..."
    docker-compose build
    
    # Start services
    print_status "Starting services..."
    docker-compose up -d
    
    # Wait for services to be ready
    print_status "Waiting for services to be ready..."
    sleep 10
    
    # Check service health
    check_service_health
}

# Check service health
check_service_health() {
    print_status "Checking service health..."
    
    # Check RAG API
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        print_success "RAG API is healthy"
    else
        print_warning "RAG API health check failed"
    fi
    
    # Check Streamlit UI
    if curl -s http://localhost:8501/_stcore/health > /dev/null 2>&1; then
        print_success "Streamlit UI is healthy"
    else
        print_warning "Streamlit UI health check failed"
    fi
}

# Display access information
show_access_info() {
    echo ""
    echo "🎉 LinkedIn Feed Explorer is now running!"
    echo ""
    echo "📱 Access Points:"
    echo "   • Streamlit UI: http://localhost:8501"
    echo "   • RAG API: http://localhost:8000"
    echo "   • API Documentation: http://localhost:8000/docs"
    echo ""
    echo "🔧 Management Commands:"
    echo "   • View logs: docker-compose logs -f"
    echo "   • Stop services: docker-compose down"
    echo "   • Restart services: docker-compose restart"
    echo "   • Check status: docker-compose ps"
    echo ""
    echo "📚 Documentation:"
    echo "   • Production Guide: PRODUCTION_DEPLOYMENT.md"
    echo ""
}

# Main execution
main() {
    echo "🚀 LinkedIn Feed Explorer - Production Start Script"
    echo "=================================================="
    echo ""
    
    # Run checks
    check_docker
    check_docker_compose
    check_ollama
    check_ollama_model
    check_data_directory
    check_environment
    
    # Start services
    start_services
    
    # Show access information
    show_access_info
}

# Run main function
main "$@" 