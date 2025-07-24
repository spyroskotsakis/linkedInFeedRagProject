"""
LinkedIn Feed Capture - Production-ready scraper for RAG applications.

A modular, testable, and production-ready LinkedIn feed scraper designed for
Retrieval-Augmented Generation (RAG) applications. Features anti-detection
measures, cookie persistence, and comprehensive error handling.
"""

__version__ = "0.1.0"
__author__ = "LinkedIn Feed Capture Team"
__email__ = "contact@example.com"

from linkedin_feed_capture.models.post import Post, PostMetrics

__all__ = ["Post", "PostMetrics"] 