#!/bin/bash

# Ollama Connectivity Test Script
# Tests Ollama connectivity from within Docker containers

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
IMAGE_NAME="ollama-connectivity-test"
CONTAINER_NAME="ollama-test-container"

echo -e "${BLUE}🔍 Ollama Connectivity Test${NC}"
echo "=================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo -e "${RED}❌ Docker is not running. Please start Docker and try again.${NC}"
    exit 1
fi

# Check if Ollama is running on host
echo -e "${YELLOW}📡 Checking if Ollama is running on host...${NC}"
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo -e "${RED}❌ Ollama is not running on host. Please start Ollama and try again.${NC}"
    echo "   Run: ollama serve"
    exit 1
fi
echo -e "${GREEN}✅ Ollama is running on host${NC}"

# Build the test image
echo -e "${YELLOW}🔨 Building test image...${NC}"
docker build -f Dockerfile.ollama-test -t $IMAGE_NAME .

# Clean up any existing container
echo -e "${YELLOW}🧹 Cleaning up existing containers...${NC}"
docker rm -f $CONTAINER_NAME 2>/dev/null || true

# Run the test
echo -e "${YELLOW}🚀 Running Ollama connectivity tests...${NC}"
echo "=================================="

# Run with different network configurations to test
echo -e "${BLUE}📋 Test 1: Bridge network with host.docker.internal${NC}"
docker run --rm --name $CONTAINER_NAME \
    --network bridge \
    $IMAGE_NAME \
    python test_ollama_connectivity.py --base-url http://host.docker.internal:11434

echo -e "\n${BLUE}📋 Test 2: Host network${NC}"
docker run --rm --name $CONTAINER_NAME \
    --network host \
    $IMAGE_NAME \
    python test_ollama_connectivity.py --base-url http://localhost:11434

echo -e "\n${BLUE}📋 Test 3: Custom network with host IP${NC}"
# Get host IP
HOST_IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | head -1 | awk '{print $2}')
echo "   Using host IP: $HOST_IP"

docker run --rm --name $CONTAINER_NAME \
    --network bridge \
    $IMAGE_NAME \
    python test_ollama_connectivity.py --base-url http://$HOST_IP:11434

echo -e "\n${BLUE}📋 Test 4: Generate detailed report${NC}"
docker run --rm --name $CONTAINER_NAME \
    --network bridge \
    -v $(pwd):/app/reports \
    $IMAGE_NAME \
    python test_ollama_connectivity.py --base-url http://host.docker.internal:11434 --report

echo -e "\n${GREEN}✅ All tests completed!${NC}"
echo "=================================="

# Clean up
echo -e "${YELLOW}🧹 Cleaning up...${NC}"
docker rmi $IMAGE_NAME 2>/dev/null || true

echo -e "${GREEN}🎉 Ollama connectivity testing completed!${NC}" 