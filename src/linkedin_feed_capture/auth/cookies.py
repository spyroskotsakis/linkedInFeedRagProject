"""
Cookie management and persistence for LinkedIn authentication.

Handles secure storage, encryption, and management of authentication cookies
to maintain session state across scraping runs.
"""

import json
import pickle
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Union

from cryptography.fernet import Fernet
from selenium import webdriver

from linkedin_feed_capture.utils.logger import get_logger, LoggerMixin
from linkedin_feed_capture.utils.backoff import with_retries, RetryConfig, RetryableError

logger = get_logger(__name__)


class CookieError(Exception):
    """Base exception for cookie-related errors."""
    pass


class CookieEncryptionError(CookieError):
    """Error for cookie encryption/decryption failures."""
    pass


class CookieExpiredError(CookieError):
    """Error for expired cookies."""
    pass


@dataclass
class CookieData:
    """Represents a browser cookie with metadata."""
    
    name: str
    value: str
    domain: str
    path: str = "/"
    secure: bool = True
    http_only: bool = False
    same_site: Optional[str] = None
    expiry: Optional[int] = None
    created_at: float = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = time.time()
    
    def is_expired(self) -> bool:
        """Check if cookie is expired."""
        if self.expiry is None:
            return False
        return time.time() > self.expiry
    
    def is_linkedin_cookie(self) -> bool:
        """Check if this is a LinkedIn-related cookie."""
        linkedin_domains = [".linkedin.com", "linkedin.com", "www.linkedin.com"]
        return any(domain in self.domain for domain in linkedin_domains)
    
    def to_selenium_dict(self) -> Dict[str, Union[str, int, bool]]:
        """Convert to format expected by Selenium."""
        cookie_dict = {
            "name": self.name,
            "value": self.value,
            "domain": self.domain,
            "path": self.path,
            "secure": self.secure,
            "httpOnly": self.http_only,
        }
        
        if self.expiry is not None:
            cookie_dict["expiry"] = self.expiry
            
        if self.same_site is not None:
            cookie_dict["sameSite"] = self.same_site
            
        return cookie_dict
    
    @classmethod
    def from_selenium_dict(cls, cookie_dict: Dict[str, Union[str, int, bool]]) -> "CookieData":
        """Create from Selenium cookie dictionary."""
        return cls(
            name=cookie_dict["name"],
            value=cookie_dict["value"],
            domain=cookie_dict["domain"],
            path=cookie_dict.get("path", "/"),
            secure=cookie_dict.get("secure", True),
            http_only=cookie_dict.get("httpOnly", False),
            same_site=cookie_dict.get("sameSite"),
            expiry=cookie_dict.get("expiry"),
        )


@dataclass
class CookieStore:
    """Container for multiple cookies with metadata."""
    
    cookies: List[CookieData]
    created_at: float
    last_used: float
    user_agent: Optional[str] = None
    session_id: Optional[str] = None
    
    def __post_init__(self):
        if self.last_used is None:
            self.last_used = time.time()
    
    def get_linkedin_cookies(self) -> List[CookieData]:
        """Get only LinkedIn-related cookies."""
        return [cookie for cookie in self.cookies if cookie.is_linkedin_cookie()]
    
    def is_expired(self, max_age_days: int = 30) -> bool:
        """Check if cookie store is expired."""
        max_age_seconds = max_age_days * 24 * 60 * 60
        age = time.time() - self.created_at
        return age > max_age_seconds
    
    def has_valid_session(self) -> bool:
        """Check if store contains valid session cookies."""
        linkedin_cookies = self.get_linkedin_cookies()
        
        # Check for critical LinkedIn session cookies
        critical_cookies = ["li_at", "JSESSIONID", "bcookie"]
        found_cookies = {cookie.name for cookie in linkedin_cookies}
        
        has_critical = any(critical in found_cookies for critical in critical_cookies)
        has_unexpired = any(not cookie.is_expired() for cookie in linkedin_cookies)
        
        return has_critical and has_unexpired
    
    def remove_expired_cookies(self) -> None:
        """Remove expired cookies from the store."""
        self.cookies = [cookie for cookie in self.cookies if not cookie.is_expired()]
    
    def update_last_used(self) -> None:
        """Update the last used timestamp."""
        self.last_used = time.time()


class CookieManager(LoggerMixin):
    """Manages cookie storage, encryption, and persistence."""
    
    def __init__(
        self,
        storage_path: Union[str, Path],
        encryption_key: Optional[str] = None,
        max_age_days: int = 30,
    ):
        """
        Initialize cookie manager.
        
        Args:
            storage_path: Path to store cookie files
            encryption_key: Encryption key for securing cookies
            max_age_days: Maximum age for cookies before expiration
        """
        self.storage_path = Path(storage_path)
        self.max_age_days = max_age_days
        
        # Setup encryption
        if encryption_key:
            self.cipher = Fernet(encryption_key.encode() if isinstance(encryption_key, str) else encryption_key)
        else:
            # Generate a key and warn user
            self.cipher = Fernet(Fernet.generate_key())
            self.logger.warning(
                "No encryption key provided, generated temporary key. "
                "Cookies will not be readable across sessions."
            )
        
        # Ensure storage directory exists
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
    
    @with_retries(RetryConfig(max_retries=3, base_delay=0.5))
    def save_cookies(
        self, 
        driver: webdriver.Chrome,
        user_agent: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> None:
        """
        Save cookies from WebDriver to encrypted storage.
        
        Args:
            driver: Chrome WebDriver instance
            user_agent: User agent string
            session_id: Optional session identifier
        """
        try:
            self.logger.info("Saving cookies to storage", storage_path=str(self.storage_path))
            
            # Get all cookies from driver
            selenium_cookies = driver.get_cookies()
            
            # Convert to CookieData objects
            cookies = [
                CookieData.from_selenium_dict(cookie) 
                for cookie in selenium_cookies
            ]
            
            # Create cookie store
            cookie_store = CookieStore(
                cookies=cookies,
                created_at=time.time(),
                last_used=time.time(),
                user_agent=user_agent or driver.execute_script("return navigator.userAgent;"),
                session_id=session_id,
            )
            
            # Serialize and encrypt
            serialized_data = pickle.dumps(asdict(cookie_store))
            encrypted_data = self.cipher.encrypt(serialized_data)
            
            # Write to file
            with open(self.storage_path, "wb") as f:
                f.write(encrypted_data)
            
            linkedin_cookies = cookie_store.get_linkedin_cookies()
            self.logger.info(
                "Cookies saved successfully",
                total_cookies=len(cookies),
                linkedin_cookies=len(linkedin_cookies),
                storage_size_bytes=len(encrypted_data),
            )
            
        except Exception as e:
            self.logger.error(
                "Failed to save cookies",
                error=str(e),
                error_type=type(e).__name__,
                storage_path=str(self.storage_path),
            )
            raise CookieError(f"Failed to save cookies: {e}") from e
    
    @with_retries(RetryConfig(max_retries=3, base_delay=0.5))
    def load_cookies(self) -> Optional[CookieStore]:
        """
        Load cookies from encrypted storage.
        
        Returns:
            CookieStore if successful, None if no valid cookies found
            
        Raises:
            CookieError: If loading fails
        """
        if not self.storage_path.exists():
            self.logger.info("No cookie file found", storage_path=str(self.storage_path))
            return None
        
        try:
            self.logger.info("Loading cookies from storage", storage_path=str(self.storage_path))
            
            # Read and decrypt
            with open(self.storage_path, "rb") as f:
                encrypted_data = f.read()
            
            decrypted_data = self.cipher.decrypt(encrypted_data)
            cookie_store_dict = pickle.loads(decrypted_data)
            
            # Reconstruct CookieStore
            cookies = [
                CookieData(**cookie_data) 
                for cookie_data in cookie_store_dict["cookies"]
            ]
            
            cookie_store = CookieStore(
                cookies=cookies,
                created_at=cookie_store_dict["created_at"],
                last_used=cookie_store_dict["last_used"],
                user_agent=cookie_store_dict.get("user_agent"),
                session_id=cookie_store_dict.get("session_id"),
            )
            
            # Check if expired
            if cookie_store.is_expired(self.max_age_days):
                self.logger.warning(
                    "Cookie store is expired",
                    age_days=(time.time() - cookie_store.created_at) / (24 * 60 * 60),
                    max_age_days=self.max_age_days,
                )
                raise CookieExpiredError("Cookie store has expired")
            
            # Remove expired individual cookies
            initial_count = len(cookie_store.cookies)
            cookie_store.remove_expired_cookies()
            
            if len(cookie_store.cookies) < initial_count:
                self.logger.info(
                    "Removed expired cookies",
                    removed_count=initial_count - len(cookie_store.cookies),
                    remaining_count=len(cookie_store.cookies),
                )
            
            # Check for valid session
            if not cookie_store.has_valid_session():
                self.logger.warning("No valid LinkedIn session found in cookies")
                raise CookieExpiredError("No valid LinkedIn session cookies")
            
            linkedin_cookies = cookie_store.get_linkedin_cookies()
            self.logger.info(
                "Cookies loaded successfully",
                total_cookies=len(cookie_store.cookies),
                linkedin_cookies=len(linkedin_cookies),
                store_age_hours=(time.time() - cookie_store.created_at) / 3600,
            )
            
            # Update last used timestamp
            cookie_store.update_last_used()
            
            return cookie_store
            
        except (CookieExpiredError, CookieEncryptionError):
            raise
        except Exception as e:
            self.logger.error(
                "Failed to load cookies",
                error=str(e),
                error_type=type(e).__name__,
                storage_path=str(self.storage_path),
            )
            raise CookieError(f"Failed to load cookies: {e}") from e
    
    def apply_cookies_to_driver(
        self,
        driver: webdriver.Chrome,
        cookie_store: CookieStore,
    ) -> None:
        """
        Apply cookies from store to WebDriver.
        
        Args:
            driver: Chrome WebDriver instance
            cookie_store: Cookie store to apply
        """
        try:
            self.logger.info("Applying cookies to WebDriver")
            
            # Navigate to LinkedIn first to set domain
            driver.get("https://www.linkedin.com")
            
            # Apply LinkedIn cookies
            linkedin_cookies = cookie_store.get_linkedin_cookies()
            applied_count = 0
            
            for cookie in linkedin_cookies:
                if not cookie.is_expired():
                    try:
                        driver.add_cookie(cookie.to_selenium_dict())
                        applied_count += 1
                    except Exception as e:
                        self.logger.warning(
                            "Failed to apply individual cookie",
                            cookie_name=cookie.name,
                            error=str(e),
                        )
            
            self.logger.info(
                "Cookies applied to WebDriver",
                applied_cookies=applied_count,
                total_linkedin_cookies=len(linkedin_cookies),
            )
            
        except Exception as e:
            self.logger.error(
                "Failed to apply cookies to WebDriver",
                error=str(e),
                error_type=type(e).__name__,
            )
            raise CookieError(f"Failed to apply cookies: {e}") from e
    
    def delete_cookies(self) -> None:
        """Delete stored cookie file."""
        try:
            if self.storage_path.exists():
                self.storage_path.unlink()
                self.logger.info("Cookie file deleted", storage_path=str(self.storage_path))
            else:
                self.logger.info("No cookie file to delete", storage_path=str(self.storage_path))
        except Exception as e:
            self.logger.error(
                "Failed to delete cookie file",
                error=str(e),
                storage_path=str(self.storage_path),
            )
    
    def get_cookie_info(self) -> Dict[str, any]:
        """Get information about stored cookies."""
        if not self.storage_path.exists():
            return {"exists": False}
        
        try:
            cookie_store = self.load_cookies()
            if not cookie_store:
                return {"exists": False}
            
            linkedin_cookies = cookie_store.get_linkedin_cookies()
            return {
                "exists": True,
                "total_cookies": len(cookie_store.cookies),
                "linkedin_cookies": len(linkedin_cookies),
                "created_at": datetime.fromtimestamp(cookie_store.created_at).isoformat(),
                "last_used": datetime.fromtimestamp(cookie_store.last_used).isoformat(),
                "age_days": (time.time() - cookie_store.created_at) / (24 * 60 * 60),
                "has_valid_session": cookie_store.has_valid_session(),
                "user_agent": cookie_store.user_agent,
                "session_id": cookie_store.session_id,
            }
        except Exception as e:
            return {
                "exists": True,
                "error": str(e),
                "error_type": type(e).__name__,
            } 