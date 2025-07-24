"""
Post data models for LinkedIn feed content.

Defines the structure and validation for LinkedIn post data using Pydantic
for type safety and validation.
"""

from datetime import datetime, timezone
from typing import Optional
from urllib.parse import urlparse

from pydantic import BaseModel, Field, field_validator, ConfigDict


class PostMetrics(BaseModel):
    """Metrics for a LinkedIn post."""
    
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra="forbid"
    )
    
    likes: int = Field(
        default=0, 
        ge=0, 
        description="Number of likes/reactions on the post"
    )
    comments: int = Field(
        default=0, 
        ge=0, 
        description="Number of comments on the post"
    )
    shares: int = Field(
        default=0, 
        ge=0, 
        description="Number of shares/reposts"
    )
    views: Optional[int] = Field(
        default=None, 
        ge=0, 
        description="Number of views (if available)"
    )


class Post(BaseModel):
    """
    Represents a LinkedIn post with all extracted data.
    
    This model ensures data consistency and validates all extracted fields
    from LinkedIn feed posts. All fields are validated for type safety and
    business logic constraints.
    """
    
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra="forbid",
        json_encoders={
            datetime: lambda v: v.isoformat()
        }
    )
    
    urn: str = Field(
        ..., 
        min_length=1,
        description="LinkedIn URN identifier for the post"
    )
    author: str = Field(
        ..., 
        min_length=1,
        max_length=200,
        description="Name of the post author"
    )
    author_profile_url: Optional[str] = Field(
        default=None,
        description="URL to the author's LinkedIn profile"
    )
    content: str = Field(
        ..., 
        description="Full text content of the post"
    )
    posted_at: datetime = Field(
        ..., 
        description="When the post was published"
    )
    url: str = Field(
        ..., 
        description="Direct URL to the LinkedIn post"
    )
    metrics: PostMetrics = Field(
        default_factory=PostMetrics,
        description="Engagement metrics for the post"
    )
    company_name: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Company name if author is posting as company"
    )
    job_title: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Author's job title"
    )
    media_urls: list[str] = Field(
        default_factory=list,
        description="URLs of any attached media (images, videos)"
    )
    hashtags: list[str] = Field(
        default_factory=list,
        description="Hashtags mentioned in the post"
    )
    mentions: list[str] = Field(
        default_factory=list,
        description="Users mentioned in the post"
    )
    post_type: str = Field(
        default="text",
        description="Type of post (text, image, video, article, etc.)"
    )
    language: Optional[str] = Field(
        default=None,
        max_length=10,
        description="Detected language code (e.g., 'en', 'es')"
    )
    scraped_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="When this post was scraped"
    )
    
    @field_validator('urn')
    @classmethod
    def validate_urn(cls, v: str) -> str:
        """Validate LinkedIn URN format."""
        if not v.startswith('urn:li:'):
            raise ValueError("URN must start with 'urn:li:'")
        return v
    
    @field_validator('url', 'author_profile_url')
    @classmethod
    def validate_url(cls, v: Optional[str]) -> Optional[str]:
        """Validate URL format."""
        if v is None:
            return v
        
        try:
            parsed = urlparse(v)
            if not all([parsed.scheme, parsed.netloc]):
                raise ValueError("Invalid URL format")
            return v
        except Exception as e:
            raise ValueError(f"Invalid URL: {e}") from e
    
    @field_validator('media_urls')
    @classmethod
    def validate_media_urls(cls, v: list[str]) -> list[str]:
        """Validate all media URLs."""
        for url in v:
            try:
                parsed = urlparse(url)
                if not all([parsed.scheme, parsed.netloc]):
                    raise ValueError(f"Invalid media URL: {url}")
            except Exception as e:
                raise ValueError(f"Invalid media URL {url}: {e}") from e
        return v
    
    @field_validator('hashtags')
    @classmethod
    def validate_hashtags(cls, v: list[str]) -> list[str]:
        """Validate and normalize hashtags."""
        normalized = []
        for tag in v:
            # Remove # if present and normalize
            clean_tag = tag.lstrip('#').strip().lower()
            if clean_tag and clean_tag not in normalized:
                normalized.append(clean_tag)
        return normalized
    
    @field_validator('posted_at', 'scraped_at')
    @classmethod
    def validate_datetime(cls, v: datetime) -> datetime:
        """Validate datetime is not in the future."""
        if v > datetime.now(timezone.utc).replace(tzinfo=None):
            raise ValueError("Datetime cannot be in the future")
        return v
    
    def to_json_dict(self) -> dict:
        """Convert to JSON-serializable dictionary."""
        return self.model_dump(mode='json')
    
    def get_engagement_rate(self) -> float:
        """Calculate engagement rate if views are available."""
        if self.metrics.views and self.metrics.views > 0:
            total_engagement = (
                self.metrics.likes + 
                self.metrics.comments + 
                self.metrics.shares
            )
            return total_engagement / self.metrics.views
        return 0.0
    
    def is_company_post(self) -> bool:
        """Check if this is a company post."""
        return self.company_name is not None
    
    def has_media(self) -> bool:
        """Check if post contains media."""
        return len(self.media_urls) > 0
    
    def __str__(self) -> str:
        """Human-readable string representation."""
        content_preview = (
            self.content[:100] + "..." 
            if len(self.content) > 100 
            else self.content
        )
        return f"Post by {self.author}: {content_preview}" 