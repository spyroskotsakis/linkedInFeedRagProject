"""
LinkedIn authentication and session management.

Handles login flow, session validation, and integration with cookie management
for maintaining persistent authentication state.
"""

import time
from dataclasses import dataclass
from typing import Optional, Tuple

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from linkedin_feed_capture.auth.cookies import CookieManager, CookieStore, CookieExpiredError
from linkedin_feed_capture.browser.stealth import (
    simulate_human_scroll, 
    simulate_mouse_movement,
    add_human_delay,
    is_likely_detected
)
from linkedin_feed_capture.utils.logger import get_logger, LoggerMixin
from linkedin_feed_capture.utils.backoff import with_retries, RetryConfig, AntiDetectionError

logger = get_logger(__name__)


class AuthenticationError(Exception):
    """Base exception for authentication errors."""
    pass


class LoginFailedError(AuthenticationError):
    """Error for failed login attempts."""
    pass


class CaptchaRequiredError(AuthenticationError):
    """Error when CAPTCHA challenge is required."""
    pass


class TwoFactorRequiredError(AuthenticationError):
    """Error when two-factor authentication is required."""
    pass


@dataclass
class AuthConfig:
    """Configuration for LinkedIn authentication."""
    
    email: str
    password: str
    cookie_path: str
    encryption_key: Optional[str] = None
    login_timeout: int = 30
    max_login_attempts: int = 3
    enable_2fa_handling: bool = False
    manual_captcha_solving: bool = True
    session_validation_url: str = "https://www.linkedin.com/feed/"
    login_url: str = "https://www.linkedin.com/login"


class LinkedInAuthenticator(LoggerMixin):
    """Handles LinkedIn authentication and session management."""
    
    def __init__(self, config: AuthConfig):
        """
        Initialize the authenticator.
        
        Args:
            config: Authentication configuration
        """
        self.config = config
        self.cookie_manager = CookieManager(
            storage_path=config.cookie_path,
            encryption_key=config.encryption_key,
        )
    
    def authenticate(self, driver: webdriver.Chrome) -> bool:
        """
        Authenticate with LinkedIn using cookies or credentials.
        
        Args:
            driver: Chrome WebDriver instance
            
        Returns:
            True if authentication successful, False otherwise
            
        Raises:
            AuthenticationError: If authentication fails
        """
        self.logger.info("Starting LinkedIn authentication")
        
        # Try cookie-based authentication first
        if self._try_cookie_authentication(driver):
            self.logger.info("Cookie-based authentication successful")
            return True
        
        # Fall back to credential-based login
        self.logger.info("Cookie authentication failed, attempting credential login")
        return self._perform_credential_login(driver)
    
    def _try_cookie_authentication(self, driver: webdriver.Chrome) -> bool:
        """
        Attempt authentication using stored cookies.
        
        Args:
            driver: Chrome WebDriver instance
            
        Returns:
            True if cookie authentication successful, False otherwise
        """
        try:
            self.logger.info("Attempting cookie-based authentication")
            
            # Load cookies
            cookie_store = self.cookie_manager.load_cookies()
            if not cookie_store:
                self.logger.info("No valid cookies found")
                return False
            
            # Apply cookies to driver
            self.cookie_manager.apply_cookies_to_driver(driver, cookie_store)
            
            # Validate session
            if self._validate_session(driver):
                # Save updated cookies after successful validation
                self.cookie_manager.save_cookies(driver, session_id="cookie_auth")
                return True
            else:
                self.logger.warning("Cookie authentication failed session validation")
                return False
                
        except CookieExpiredError:
            self.logger.warning("Stored cookies have expired")
            return False
        except Exception as e:
            self.logger.warning(
                "Cookie authentication failed",
                error=str(e),
                error_type=type(e).__name__,
            )
            return False
    
    @with_retries(RetryConfig(max_retries=3, base_delay=2.0))
    def _perform_credential_login(self, driver: webdriver.Chrome) -> bool:
        """
        Perform credential-based login to LinkedIn.
        
        Args:
            driver: Chrome WebDriver instance
            
        Returns:
            True if login successful, False otherwise
            
        Raises:
            LoginFailedError: If login fails after all attempts
        """
        try:
            self.logger.info("Starting credential-based login")
            
            # Navigate to login page
            driver.get(self.config.login_url)
            add_human_delay(2.0)
            
            # Check for detection
            if is_likely_detected(driver):
                raise AntiDetectionError("Bot detection detected on login page")
            
            # Fill email
            email_field = self._wait_for_element(
                driver, 
                (By.ID, "username"),
                "email input field"
            )
            self._human_type(email_field, self.config.email)
            add_human_delay(1.0)
            
            # Fill password
            password_field = self._wait_for_element(
                driver,
                (By.ID, "password"), 
                "password input field"
            )
            self._human_type(password_field, self.config.password)
            add_human_delay(1.0)
            
            # Submit form
            login_button = self._wait_for_element(
                driver,
                (By.XPATH, "//button[@type='submit']"),
                "login button"
            )
            
            # Simulate mouse movement to button before clicking
            simulate_mouse_movement(driver, login_button)
            add_human_delay(0.5)
            login_button.click()
            
            # Wait for page load and check result
            self._handle_post_login_flow(driver)
            
            # Validate successful login
            if self._validate_session(driver):
                self.logger.info("Credential login successful")
                
                # Save cookies for future use
                self.cookie_manager.save_cookies(
                    driver, 
                    session_id="credential_login"
                )
                return True
            else:
                raise LoginFailedError("Login appeared to succeed but session validation failed")
                
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(
                "Login failed due to element not found",
                error=str(e),
                current_url=driver.current_url,
            )
            raise LoginFailedError(f"Login UI elements not found: {e}") from e
        except AntiDetectionError:
            raise
        except Exception as e:
            self.logger.error(
                "Unexpected error during login",
                error=str(e),
                error_type=type(e).__name__,
                current_url=driver.current_url,
            )
            raise LoginFailedError(f"Login failed: {e}") from e
    
    def _handle_post_login_flow(self, driver: webdriver.Chrome) -> None:
        """
        Handle various post-login scenarios like 2FA, CAPTCHA, etc.
        
        Args:
            driver: Chrome WebDriver instance
            
        Raises:
            CaptchaRequiredError: If CAPTCHA is required
            TwoFactorRequiredError: If 2FA is required
        """
        # Wait for page to load
        add_human_delay(3.0)
        
        current_url = driver.current_url.lower()
        page_source = driver.page_source.lower()
        
        # Check for CAPTCHA
        if "captcha" in page_source or "challenge" in current_url:
            self.logger.warning("CAPTCHA challenge detected")
            
            if self.config.manual_captcha_solving:
                self._handle_manual_captcha(driver)
            else:
                raise CaptchaRequiredError("CAPTCHA required but manual solving disabled")
        
        # Check for 2FA
        if any(keyword in page_source for keyword in ["verification", "two-factor", "2fa"]):
            self.logger.warning("Two-factor authentication required")
            
            if self.config.enable_2fa_handling:
                self._handle_2fa(driver)
            else:
                raise TwoFactorRequiredError("2FA required but handling disabled")
        
        # Check for other security challenges
        if any(keyword in page_source for keyword in ["security check", "verify", "unusual activity"]):
            self.logger.warning("Security challenge detected")
            add_human_delay(5.0)  # Give more time for manual intervention
    
    def _handle_manual_captcha(self, driver: webdriver.Chrome) -> None:
        """
        Handle CAPTCHA with manual solving.
        
        Args:
            driver: Chrome WebDriver instance
        """
        self.logger.warning(
            "CAPTCHA detected - manual intervention required",
            current_url=driver.current_url,
        )
        
        # Wait for manual solving (up to 5 minutes)
        max_wait_time = 300  # 5 minutes
        start_time = time.time()
        
        while time.time() - start_time < max_wait_time:
            if "captcha" not in driver.page_source.lower():
                self.logger.info("CAPTCHA appears to be solved")
                return
            
            time.sleep(5)  # Check every 5 seconds
        
        raise CaptchaRequiredError("CAPTCHA not solved within time limit")
    
    def _handle_2fa(self, driver: webdriver.Chrome) -> None:
        """
        Handle two-factor authentication.
        
        Args:
            driver: Chrome WebDriver instance
        """
        self.logger.warning(
            "2FA detected - manual intervention may be required",
            current_url=driver.current_url,
        )
        
        # For now, just wait for manual intervention
        # In future versions, could integrate with SMS/email APIs
        max_wait_time = 300  # 5 minutes
        start_time = time.time()
        
        while time.time() - start_time < max_wait_time:
            current_url = driver.current_url.lower()
            if "feed" in current_url or "home" in current_url:
                self.logger.info("2FA appears to be completed")
                return
            
            time.sleep(5)
        
        raise TwoFactorRequiredError("2FA not completed within time limit")
    
    def _validate_session(self, driver: webdriver.Chrome) -> bool:
        """
        Validate that the current session is authenticated.
        
        Args:
            driver: Chrome WebDriver instance
            
        Returns:
            True if session is valid, False otherwise
        """
        try:
            self.logger.info("Validating LinkedIn session")
            
            # Navigate to feed page
            driver.get(self.config.session_validation_url)
            add_human_delay(3.0)
            
            # Check if we're redirected to login
            current_url = driver.current_url.lower()
            if "login" in current_url or "authwall" in current_url:
                self.logger.warning("Session validation failed - redirected to login")
                return False
            
            # Look for feed indicators
            try:
                # Wait for feed elements to appear
                WebDriverWait(driver, 10).until(
                    EC.any_of(
                        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')),
                        EC.presence_of_element_located((By.CLASS_NAME, "feed-shared-update-v2")),
                        EC.presence_of_element_located((By.CLASS_NAME, "artdeco-button--primary")),
                    )
                )
                
                self.logger.info("Session validation successful - feed elements found")
                return True
                
            except TimeoutException:
                self.logger.warning("Session validation failed - no feed elements found")
                return False
                
        except Exception as e:
            self.logger.error(
                "Session validation error",
                error=str(e),
                error_type=type(e).__name__,
                current_url=driver.current_url,
            )
            return False
    
    def _wait_for_element(
        self,
        driver: webdriver.Chrome,
        locator: Tuple[str, str],
        description: str,
        timeout: int = None,
    ):
        """
        Wait for element to be present and return it.
        
        Args:
            driver: Chrome WebDriver instance
            locator: Element locator tuple (By.*, value)
            description: Human-readable description for logging
            timeout: Timeout in seconds
            
        Returns:
            WebElement
            
        Raises:
            TimeoutException: If element not found within timeout
        """
        timeout = timeout or self.config.login_timeout
        
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            self.logger.debug(f"Found {description}", locator=locator)
            return element
        except TimeoutException:
            self.logger.error(
                f"Timeout waiting for {description}",
                locator=locator,
                timeout=timeout,
                current_url=driver.current_url,
            )
            raise
    
    def _human_type(self, element, text: str) -> None:
        """
        Type text in a human-like manner.
        
        Args:
            element: WebElement to type into
            text: Text to type
        """
        element.clear()
        
        for char in text:
            element.send_keys(char)
            # Random delay between keystrokes
            delay = 0.05 + (0.1 * hash(char) % 10 / 100)  # 0.05-0.15 seconds
            time.sleep(delay)
    
    def logout(self, driver: webdriver.Chrome) -> None:
        """
        Logout from LinkedIn and clear session.
        
        Args:
            driver: Chrome WebDriver instance
        """
        try:
            self.logger.info("Logging out from LinkedIn")
            
            # Clear browser cookies
            driver.delete_all_cookies()
            
            # Delete stored cookies
            self.cookie_manager.delete_cookies()
            
            self.logger.info("Logout completed successfully")
            
        except Exception as e:
            self.logger.error(
                "Error during logout",
                error=str(e),
                error_type=type(e).__name__,
            )
    
    def get_session_info(self, driver: webdriver.Chrome) -> dict:
        """
        Get information about the current session.
        
        Args:
            driver: Chrome WebDriver instance
            
        Returns:
            Dictionary with session information
        """
        try:
            # Get cookie info
            cookie_info = self.cookie_manager.get_cookie_info()
            
            # Get current status
            is_authenticated = self._validate_session(driver)
            
            return {
                "authenticated": is_authenticated,
                "current_url": driver.current_url,
                "cookies": cookie_info,
                "session_validation_url": self.config.session_validation_url,
                "timestamp": time.time(),
            }
        except Exception as e:
            return {
                "authenticated": False,
                "error": str(e),
                "error_type": type(e).__name__,
                "timestamp": time.time(),
            } 