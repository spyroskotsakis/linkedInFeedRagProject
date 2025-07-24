# LinkedIn Feed Capture for RAG Applications

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Selenium](https://img.shields.io/badge/selenium-4.15+-orange.svg)

A production-ready LinkedIn feed scraper designed specifically for RAG (Retrieval-Augmented Generation) applications. Extract posts, engagement metrics, author information, and media content with comprehensive anti-detection measures.

## 🚀 Quick Start

### 1. Clone and Install
```bash
git clone <your-repo-url>
cd linkedInFeedRagProject
pip install -e .
```

### 2. Configure Credentials
```bash
python setup_credentials.py
# Edit the .env file with your LinkedIn credentials
```

### 3. Test Connection
```bash
python simple_linkedin_test.py
```

### 4. Start Scraping
```bash
# Interactive mode
python complete_linkedin_scraper.py

# Command line mode
python complete_linkedin_scraper.py --posts 50 --verbose
```

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [CLI Reference](#cli-reference)
- [Output Formats](#output-formats)
- [Data Schema](#data-schema)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)
- [Legal Considerations](#legal-considerations)

## ✨ Features

### Core Functionality
- **🔐 Automated Authentication** - Secure login with cookie persistence
- **🛡️ Anti-Detection Stealth Mode** - Bypass LinkedIn's bot detection
- **📊 Comprehensive Data Extraction** - Posts, engagement, authors, media
- **⚡ Scalable Processing** - From 10 to 1000+ posts
- **🎯 RAG-Optimized Output** - JSON format ready for AI/ML pipelines

### Advanced Features
- **📈 Real-time Progress Tracking** - Monitor extraction progress
- **🔄 Quality Filtering** - Auto-filter high-value content
- **📁 Multiple Output Formats** - JSON, CSV, analytics reports
- **🖥️ Flexible CLI Options** - Command line and interactive modes
- **📱 Cross-platform Support** - Windows, macOS, Linux

### Data Extracted
- Author information and profile links
- Complete post content (up to 3000+ characters)
- Engagement metrics (likes, comments, shares)
- Timestamps and post URLs
- Hashtags and mentions
- Media detection (images, videos)
- Company/organization affiliations

## 🛠️ Installation

### Prerequisites
- Python 3.11 or higher
- Google Chrome browser
- Internet connection

### Automatic Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd linkedInFeedRagProject

# Install with all dependencies
pip install -e .

# Verify installation
python -c "import linkedin_feed_capture; print('✅ Installation successful')"
```

### Manual Dependencies (if needed)
```bash
pip install selenium>=4.15.0 webdriver-manager>=4.0.0 python-dotenv>=1.0.0
pip install beautifulsoup4>=4.12.0 pandas>=2.0.0 requests>=2.31.0
```

## ⚙️ Configuration

### 1. Environment Setup
Run the setup script to create your configuration:
```bash
python setup_credentials.py
```

### 2. Configure LinkedIn Credentials
Edit the `.env` file:
```bash
# LinkedIn Authentication (REQUIRED)
LINKEDIN_EMAIL=your.email@example.com
LINKEDIN_PASSWORD=your_secure_password

# Optional Configuration
COOKIE_PATH=./data/cookies.pkl
COOKIE_ENCRYPTION_KEY=your_encryption_key_here
LOG_LEVEL=INFO
LOG_FILE=./logs/linkedin_scraper.log
```

### 3. Verify Configuration
```bash
# Test your credentials
python simple_linkedin_test.py

# Check CLI options
python complete_linkedin_scraper.py --help
```

## 🚀 Usage

### Interactive Mode (Easiest)
```bash
python complete_linkedin_scraper.py
# Prompts for number of posts to extract
```

### Command Line Mode (Recommended for Automation)
```bash
# Basic usage
python complete_linkedin_scraper.py --posts 25

# Advanced usage with all options
python complete_linkedin_scraper.py \
  --posts 100 \
  --output data/my_feed.json \
  --verbose \
  --no-headless \
  --scroll-delay 3
```

### Use the Built-in CLI Tool
```bash
# After installation, you can also use:
python -m linkedin_feed_capture.cli.main capture --posts 50
```

## 📖 CLI Reference

### `complete_linkedin_scraper.py` (Main Tool)

#### Basic Options
| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--posts` | `-n` | Number of posts to extract | Interactive prompt |
| `--output` | `-o` | Output file path | Auto-generated |
| `--verbose` | `-v` | Enable detailed output | False |
| `--help` | `-h` | Show help message | - |

#### Browser Control
| Option | Description | Default |
|--------|-------------|---------|
| `--headless` | Run browser invisibly | False |
| `--no-headless` | Run browser visibly (for debugging) | True |
| `--scroll-delay` | Seconds between scrolls | 2.0 |
| `--max-scrolls` | Maximum scroll attempts | 50 |

#### Output Formatting
| Option | Description | Default |
|--------|-------------|---------|
| `--pretty` | Format JSON with indentation | True |
| `--no-pretty` | Compact JSON output | False |

### Examples

#### Quick Extractions
```bash
# Extract 10 posts (default)
python complete_linkedin_scraper.py

# Extract 50 posts with verbose output
python complete_linkedin_scraper.py --posts 50 --verbose

# Extract 25 posts to specific file
python complete_linkedin_scraper.py -n 25 -o "my_linkedin_data.json"
```

#### Production Usage
```bash
# Large scale extraction (headless mode)
python complete_linkedin_scraper.py \
  --posts 200 \
  --headless \
  --output "data/feed_$(date +%Y%m%d).json" \
  --scroll-delay 3

# Debug mode (visible browser)
python complete_linkedin_scraper.py \
  --posts 10 \
  --no-headless \
  --verbose
```

#### Scheduled Automation
```bash
# Daily extraction (add to crontab)
0 9 * * * cd /path/to/project && python complete_linkedin_scraper.py --posts 100 --headless

# Weekly large extraction
0 9 * * 1 cd /path/to/project && python complete_linkedin_scraper.py --posts 500 --headless
```

### Additional Tools

#### Setup and Testing
```bash
# Configure credentials
python setup_credentials.py

# Test connection
python simple_linkedin_test.py

# Check configuration status
python setup_credentials.py  # Shows current status
```

#### Built-in CLI (Alternative)
```bash
# Main CLI tool (more features, complex setup)
python -m linkedin_feed_capture.cli.main capture [OPTIONS]

# Test connection
python -m linkedin_feed_capture.cli.main test-connection

# Show auth info  
python -m linkedin_feed_capture.cli.main auth-info
```

## 📄 Output Formats

### Organized Data Structure
Each extraction creates a dedicated subfolder with comprehensive data organization:

```
data/
├── posts_5/                          # 5 posts extraction
│   ├── linkedin_feed_20240115_143022.json
│   ├── analytics_20240115_143022.json
│   ├── posts_analysis_20240115_143022.csv
│   ├── quality_posts_20240115_143022.json
│   └── extraction_summary_20240115_143022.txt
├── posts_25/                         # 25 posts extraction
│   ├── linkedin_feed_20240115_150030.json
│   ├── analytics_20240115_150030.json
│   ├── posts_analysis_20240115_150030.csv
│   ├── quality_posts_20240115_150030.json
│   └── extraction_summary_20240115_150030.txt
└── posts_100/                        # 100 posts extraction
    ├── linkedin_feed_20240115_160045.json
    ├── analytics_20240115_160045.json
    ├── posts_analysis_20240115_160045.csv
    ├── quality_posts_20240115_160045.json
    └── extraction_summary_20240115_160045.txt
```

### File Types Generated

#### 1. Main Data File: `linkedin_feed_TIMESTAMP.json`
Primary extraction data with complete post information:

```json
[
  {
    "urn": "urn:li:activity:7354048940184367105",
    "author": "John Doe",
    "author_url": "https://linkedin.com/in/johndoe",
    "author_headline": "Senior Data Scientist at TechCorp",
    "content": "Just built an amazing RAG system...",
    "posted_at": "2024-01-15T10:30:00Z",
    "engagement": {
      "likes": 42,
      "comments": 8,
      "shares": 3
    },
    "hashtags": ["AI", "MachineLearning", "RAG"],
    "media": {
      "has_image": true,
      "has_video": false,
      "urls": ["https://media.licdn.com/..."]
    },
    "extracted_at": "2024-01-15T14:22:33.123456",
    "post_url": "https://www.linkedin.com/posts/..."
  }
]
```

#### 2. Analytics File: `analytics_TIMESTAMP.json`
Comprehensive extraction statistics and insights:

```json
{
  "extraction_info": {
    "timestamp": "2024-01-15T14:22:33Z",
    "total_posts": 25,
    "extraction_duration": "45s"
  },
  "engagement_metrics": {
    "total_likes": 1250,
    "total_comments": 245,
    "total_shares": 67,
    "average_likes": 50.0,
    "high_engagement_posts": 5
  },
  "content_analysis": {
    "posts_with_substantial_content": 18,
    "posts_with_media": 12,
    "average_content_length": 340,
    "hashtag_count": 45
  },
  "top_posts": [...]
}
```

#### 3. CSV Export: `posts_analysis_TIMESTAMP.csv`
Spreadsheet-friendly format for analysis and filtering:

```csv
urn,author,author_headline,content_length,content_preview,likes,comments,shares,has_media,hashtag_count,extracted_at
urn:li:activity:123,John Doe,Senior Engineer,1200,"Amazing AI breakthrough...",42,8,3,true,3,2024-01-15T14:22:33
```

#### 4. Quality Posts: `quality_posts_TIMESTAMP.json`
Filtered dataset containing only high-value posts (>200 characters OR >10 likes):

```json
[
  {
    "urn": "...",
    "content": "Substantial post with detailed insights...",
    "engagement": {"likes": 125, "comments": 23}
  }
]
```

#### 5. Extraction Summary: `extraction_summary_TIMESTAMP.txt`
Human-readable summary report:

```
LinkedIn Feed Extraction Summary
==================================================
Extraction Date: 2024-01-15 14:22:33
Target Posts: 25
Actual Posts Extracted: 25
Success Rate: 100.0%

Engagement Overview:
- Total Likes: 1,250
- Total Comments: 245
- Posts with Media: 12
- Posts with Substantial Content (>200 chars): 18

Top Performing Posts:
------------------------------
1. 125 likes - Tech Expert
   "Revolutionary AI breakthrough in natural language processing..."

Files Generated:
- linkedin_feed_TIMESTAMP.json (main data)
- analytics_TIMESTAMP.json (detailed analytics)
- posts_analysis_TIMESTAMP.csv (spreadsheet format)
- quality_posts_TIMESTAMP.json (filtered high-value posts)
- extraction_summary_TIMESTAMP.txt (this file)
```

### Folder Organization Benefits

- **Easy Organization**: Each extraction is self-contained
- **No File Conflicts**: Timestamp-based naming prevents overwrites
- **Quick Access**: Find extractions by post count
- **Complete Context**: All related files in one location
- **Production Ready**: Structured for automated processing

## 📊 Data Schema

### Post Object Structure
```typescript
interface Post {
  urn: string;                    // Unique LinkedIn identifier
  author: string;                 // Author display name
  author_url?: string;            // LinkedIn profile URL
  author_headline?: string;       // Professional title/description
  content: string;                // Full post content
  posted_at?: string;             // ISO timestamp or relative time
  engagement: {
    likes: number;                // Reaction count
    comments: number;             // Comment count  
    shares: number;               // Share/repost count
  };
  hashtags: string[];             // Extracted hashtags
  media: {
    has_image: boolean;           // Contains images
    has_video: boolean;           // Contains videos
    urls: string[];               // Media URLs
  };
  extracted_at: string;           // Extraction timestamp (ISO)
  post_url?: string;              // Direct post URL
}
```

### Quality Metrics
Posts are automatically scored based on:
- **Content Length** (200+ characters preferred)
- **Engagement Rate** (likes, comments, shares)
- **Media Presence** (images, videos)
- **Author Information** (complete profiles)
- **Professional Relevance** (industry keywords)

## 🔧 Troubleshooting

### Common Issues

#### Authentication Problems
```bash
# Problem: Login fails or security challenge
# Solution: 
python simple_linkedin_test.py  # Test credentials
# Complete any security challenges manually
# Update .env with correct credentials
```

#### Browser/Driver Issues
```bash
# Problem: ChromeDriver version mismatch
# Solution: The scraper auto-manages drivers, but if issues persist:
pip install --upgrade webdriver-manager
# or manually update Chrome browser
```

#### No Posts Found
```bash
# Problem: Extraction finds 0 posts
# Likely causes:
# 1. Empty LinkedIn feed (new account)
# 2. Privacy settings blocking content
# 3. Rate limiting/temporary blocks

# Solutions:
python complete_linkedin_scraper.py --no-headless --verbose  # Debug mode
# Reduce post count: --posts 5
# Increase scroll delay: --scroll-delay 5
```

#### Rate Limiting/HTTP 999 Errors
```bash
# Problem: LinkedIn detects automation
# Solutions:
# 1. Reduce frequency (daily instead of hourly)
# 2. Lower post counts (50 instead of 500)  
# 3. Increase delays: --scroll-delay 5
# 4. Use --no-headless for less detection
# 5. Wait 24 hours before retrying
```

### Debug Mode
Run in visible browser mode for troubleshooting:
```bash
python complete_linkedin_scraper.py --no-headless --verbose --posts 5
```

### Log Analysis
Check logs for detailed error information:
```bash
# View recent logs
tail -f logs/linkedin_scraper.log

# Search for specific errors
grep "ERROR" logs/linkedin_scraper.log
```

## 🎯 Best Practices

### Extraction Guidelines
- **Start Small**: Begin with 10-25 posts to test your setup
- **Gradual Scaling**: Increase to 50-100 posts once stable
- **Rate Limiting**: Don't exceed 200 posts per session
- **Timing**: Space extractions 24+ hours apart
- **Monitoring**: Use `--verbose` to track progress

### Data Quality Optimization
- **Content Filtering**: Focus on posts with >200 characters
- **Engagement Filtering**: Prioritize posts with >10 likes
- **Author Diversity**: Capture from various industries/roles
- **Temporal Distribution**: Mix recent and older posts

### Security and Ethics
- **Credential Security**: Never commit `.env` files
- **Respect Rate Limits**: Don't overwhelm LinkedIn's servers
- **Content Attribution**: Preserve author information
- **Data Retention**: Follow data protection guidelines
- **Terms Compliance**: Review LinkedIn's User Agreement

### Production Deployment
```bash
# 1. Environment Setup
python -m venv linkedin_scraper
source linkedin_scraper/bin/activate
pip install -r requirements.txt

# 2. Automated Scheduling (crontab example)
# Daily extraction at 9 AM
0 9 * * * cd /path/to/project && python complete_linkedin_scraper.py --posts 50 --headless

# 3. Monitoring and Alerting
# Add error handling and notifications
# Monitor success/failure rates
# Set up log rotation
```

### RAG Integration
```python
# Example: Loading data for RAG applications
import json
from pathlib import Path

def load_linkedin_data(data_dir="./data"):
    """Load all LinkedIn posts for RAG processing"""
    posts = []
    for json_file in Path(data_dir).glob("linkedin_feed_*.json"):
        with open(json_file) as f:
            posts.extend(json.load(f))
    
    # Filter high-quality content
    quality_posts = [
        post for post in posts 
        if len(post['content']) > 200 and post['engagement']['likes'] > 5
    ]
    
    return quality_posts

# Usage in your RAG pipeline
posts = load_linkedin_data()
for post in posts:
    # Create embeddings from post['content']
    # Use post['author_headline'] for context
    # Weight by post['engagement']['likes']
    pass
```

## ⚖️ Legal Considerations

### Important Disclaimers
- **User Agreement**: LinkedIn's ToS prohibits automated data collection
- **Public Data**: Focus on publicly visible content only
- **Personal Use**: Intended for research and personal RAG applications
- **Commercial Use**: Requires careful legal review
- **Data Protection**: Comply with GDPR, CCPA, and local privacy laws

### Compliance Guidelines
1. **Respect robots.txt** (though LinkedIn may not honor it)
2. **Rate Limiting** to avoid overwhelming servers
3. **Data Minimization** - collect only what you need
4. **Purpose Limitation** - use data only for stated purposes
5. **Access Control** - secure storage and limited access
6. **Retention Policies** - delete data when no longer needed

### Risk Mitigation
- Use on accounts you control
- Keep extraction volumes reasonable
- Implement proper error handling
- Monitor for IP blocks or rate limits
- Have legal review for commercial use

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

### Development Setup
```bash
git clone <your-fork>
cd linkedInFeedRagProject
pip install -e ".[dev]"
pre-commit install
```

### Running Tests
```bash
pytest tests/
python -m pytest tests/ -v
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Support

- **Documentation**: Check this README first
- **Issues**: Open GitHub issues for bugs
- **Features**: Submit feature requests via GitHub
- **Security**: Email security issues privately

## 🔄 Version History

- **v0.1.0**: Initial release with basic extraction
- **v0.2.0**: Added CLI options and quality filtering
- **v0.3.0**: Enhanced anti-detection and analytics

---

**⚠️ Disclaimer**: This tool is for educational and research purposes. Users are responsible for complying with LinkedIn's Terms of Service and applicable laws. 

## 🧪 Testing & Quality Assurance

### Test Structure

The project includes comprehensive testing at multiple levels:

```
tests/
├── unit/                              # Unit tests for individual components
│   ├── test_auth.py                   # Authentication testing
│   ├── test_browser.py                # Browser driver testing
│   ├── test_cli.py                    # CLI functionality testing
│   ├── test_models.py                 # Data model validation
│   ├── test_scraper.py                # Scraping logic testing
│   └── test_utils.py                  # Utility functions testing
├── integration/                       # Integration tests
│   ├── test_integration.py            # End-to-end workflow testing
│   └── test_data_pipeline.py          # Data processing pipeline
├── e2e/                              # End-to-end tests
│   ├── test_full_extraction.py        # Complete extraction scenarios
│   └── test_cli_scenarios.py          # CLI usage scenarios
└── fixtures/                         # Test data and fixtures
    ├── mock_posts.json               # Sample post data
    ├── test_credentials.env          # Test environment config
    └── sample_html.html              # Mock LinkedIn pages
```

### Unit Testing

#### Running Unit Tests
```bash
# Run all unit tests
pytest tests/unit/ -v

# Run specific test file
pytest tests/unit/test_scraper.py -v

# Run with coverage
pytest tests/unit/ --cov=src/linkedin_feed_capture --cov-report=html

# Run specific test function
pytest tests/unit/test_cli.py::test_cli_post_count_argument -v
```

#### Test Categories

**1. Authentication Tests (`test_auth.py`)**
```python
def test_cookie_encryption()           # Cookie security
def test_session_persistence()        # Session management
def test_login_validation()           # Credential validation
def test_auth_failure_handling()      # Error scenarios
```

**2. Browser Tests (`test_browser.py`)**
```python
def test_driver_creation()            # WebDriver initialization
def test_stealth_measures()           # Anti-detection features
def test_browser_cleanup()            # Resource management
def test_headless_mode()              # Headless functionality
```

**3. CLI Tests (`test_cli.py`)**
```python
def test_argument_parsing()           # Command line arguments
def test_post_count_validation()      # Input validation
def test_output_file_creation()       # File handling
def test_verbose_mode()               # Output formatting
def test_error_handling()             # Error scenarios
```

**4. Scraper Tests (`test_scraper.py`)**
```python
def test_post_extraction()            # Data extraction logic
def test_scroll_behavior()            # Scrolling mechanisms
def test_element_parsing()            # DOM parsing
def test_quality_filtering()          # Content filtering
def test_rate_limiting()              # Timing controls
```

**5. Model Tests (`test_models.py`)**
```python
def test_post_validation()            # Data structure validation
def test_json_serialization()         # JSON conversion
def test_engagement_metrics()         # Metrics calculation
def test_data_consistency()           # Data integrity
```

### Integration Testing

#### End-to-End Workflow Tests
```bash
# Run integration tests
pytest tests/integration/ -v

# Test complete data pipeline
pytest tests/integration/test_data_pipeline.py -v

# Test CLI integration
pytest tests/integration/test_cli_integration.py -v
```

#### Integration Test Examples
```python
def test_complete_extraction_workflow():
    """Test full extraction from login to data export"""
    # Test complete workflow with real LinkedIn interaction
    
def test_folder_organization():
    """Test that data is organized in correct subfolders"""
    # Verify posts_X folder structure is created
    
def test_multiple_file_generation():
    """Test that all 5 file types are generated correctly"""
    # Verify JSON, CSV, analytics, quality, and summary files
    
def test_concurrent_extractions():
    """Test multiple extractions don't conflict"""
    # Ensure timestamp-based naming prevents conflicts
```

### End-to-End Testing

#### Full System Tests
```bash
# Run complete E2E tests (requires LinkedIn credentials)
pytest tests/e2e/ -v --slow

# Test specific extraction scenarios
pytest tests/e2e/test_full_extraction.py::test_5_post_extraction -v

# Test CLI scenarios
pytest tests/e2e/test_cli_scenarios.py -v
```

#### E2E Test Scenarios
```python
def test_5_post_extraction():
    """Test extraction of 5 posts with all CLI options"""
    
def test_25_post_extraction():
    """Test medium-scale extraction"""
    
def test_100_post_extraction():
    """Test large-scale extraction"""
    
def test_custom_output_paths():
    """Test custom output file handling"""
    
def test_verbose_and_headless_modes():
    """Test different operational modes"""
```

### Test Configuration

#### Test Environment Setup
```bash
# 1. Install test dependencies
pip install -e ".[test]"

# 2. Set up test environment
cp tests/fixtures/test_credentials.env .env.test

# 3. Configure test database/storage
mkdir -p tests/temp_data

# 4. Run test suite
pytest tests/ -v
```

#### Test Dependencies
```bash
# Core testing framework
pytest>=7.4.0
pytest-cov>=4.1.0           # Coverage reporting
pytest-mock>=3.12.0         # Mocking framework
pytest-asyncio>=0.21.0      # Async testing
pytest-xdist>=3.5.0         # Parallel test execution

# Additional testing tools
factory-boy>=3.3.0          # Test data generation
responses>=0.24.0            # HTTP request mocking
freezegun>=1.2.0            # Time/date mocking
```

### Continuous Integration

#### GitHub Actions Workflow
```yaml
# .github/workflows/test.yml
name: Test Suite
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.11, 3.12]
    
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        pip install -e ".[test]"
    
    - name: Run unit tests
      run: |
        pytest tests/unit/ -v --cov=src --cov-report=xml
    
    - name: Run integration tests
      run: |
        pytest tests/integration/ -v
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
```

### Test Data Management

#### Mock Data Creation
```python
# tests/fixtures/mock_data.py
def create_mock_post(likes=10, content_length=200):
    """Create mock post data for testing"""
    return {
        "urn": f"urn:li:activity:{random.randint(1000000, 9999999)}",
        "author": "Test Author",
        "content": "A" * content_length,
        "engagement": {"likes": likes, "comments": 5, "shares": 2},
        # ... rest of post structure
    }

def create_mock_extraction(post_count=5):
    """Create complete mock extraction for testing"""
    return [create_mock_post() for _ in range(post_count)]
```

#### Test Environment Isolation
```python
# tests/conftest.py
@pytest.fixture
def temp_data_dir():
    """Create temporary data directory for tests"""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)

@pytest.fixture
def mock_linkedin_session():
    """Mock LinkedIn session for testing"""
    with responses.RequestsMock() as rsps:
        # Set up mock LinkedIn responses
        yield rsps
```

### Performance Testing

#### Load Testing
```bash
# Test extraction performance
pytest tests/performance/ -v --benchmark-only

# Memory usage testing
pytest tests/unit/ --memray

# Concurrent extraction testing
pytest tests/e2e/test_concurrent.py -v
```

#### Performance Benchmarks
```python
def test_extraction_speed(benchmark):
    """Benchmark extraction speed"""
    result = benchmark(extract_posts, post_count=10)
    assert len(result) == 10

def test_memory_usage():
    """Test memory consumption during extraction"""
    # Monitor memory usage during large extractions
    
def test_concurrent_safety():
    """Test thread safety of extraction process"""
    # Run multiple extractions simultaneously
```

### Quality Assurance

#### Code Quality Checks
```bash
# Linting
ruff check src tests --fix

# Type checking
mypy src --strict

# Security scanning
bandit -r src

# Dependency checking
safety check

# Code formatting
black src tests
```

#### Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
      - id: black
  
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.8
    hooks:
      - id: ruff
        args: [--fix]
  
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]
```

### Test Coverage Requirements

#### Coverage Targets
- **Unit Tests**: 90%+ coverage
- **Integration Tests**: 80%+ coverage  
- **Critical Paths**: 100% coverage
- **CLI Functions**: 95%+ coverage
- **Data Models**: 100% coverage

#### Coverage Reporting
```bash
# Generate coverage report
pytest tests/ --cov=src --cov-report=html --cov-report=term

# View detailed coverage
open htmlcov/index.html

# Coverage requirements check
pytest tests/ --cov=src --cov-fail-under=85
```

### Testing Best Practices

#### Test Writing Guidelines
1. **Arrange-Act-Assert**: Structure tests clearly
2. **Single Responsibility**: One assertion per test
3. **Descriptive Names**: Test names explain the scenario
4. **Independent Tests**: No dependencies between tests
5. **Mock External Services**: Isolate unit tests
6. **Test Edge Cases**: Include error scenarios
7. **Performance Awareness**: Monitor test execution time

#### Production Testing
```bash
# Pre-deployment testing
pytest tests/e2e/ --env=staging -v

# Smoke tests for production
pytest tests/smoke/ --env=production -v

# Health check tests
pytest tests/health/ -v
``` 