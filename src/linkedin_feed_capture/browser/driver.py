"""
WebDriver factory and configuration for LinkedIn feed scraping.

Provides a standardized way to create and configure Chrome WebDriver instances
with anti-detection measures and optimal settings for scraping.
"""

import os
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from linkedin_feed_capture.browser.stealth import apply_stealth_measures
from linkedin_feed_capture.utils.logger import get_logger, LoggerMixin

logger = get_logger(__name__)


@dataclass
class DriverConfig:
    """Configuration for WebDriver instances."""
    
    headless: bool = True
    window_width: int = 1280
    window_height: int = 900
    user_agent: Optional[str] = None
    chrome_binary_path: Optional[str] = None
    chromedriver_path: Optional[str] = None
    profile_directory: Optional[str] = None
    disable_images: bool = False
    disable_javascript: bool = False
    disable_plugins: bool = True
    disable_extensions: bool = True
    disable_dev_shm_usage: bool = True
    no_sandbox: bool = False
    enable_stealth: bool = True
    page_load_timeout: int = 30
    implicit_wait_timeout: int = 10
    script_timeout: int = 30
    proxy_server: Optional[str] = None
    proxy_username: Optional[str] = None
    proxy_password: Optional[str] = None
    download_directory: Optional[str] = None
    extra_arguments: List[str] = field(default_factory=list)
    extra_experimental_options: Dict[str, any] = field(default_factory=dict)
    extra_prefs: Dict[str, any] = field(default_factory=dict)


class DriverFactory(LoggerMixin):
    """Factory for creating configured WebDriver instances."""
    
    def __init__(self, config: Optional[DriverConfig] = None):
        """
        Initialize the driver factory.
        
        Args:
            config: Driver configuration options
        """
        self.config = config or DriverConfig()
        self._temp_dirs: List[str] = []
        
    def create_driver(self) -> webdriver.Chrome:
        """
        Create a configured Chrome WebDriver instance.
        
        Returns:
            Configured Chrome WebDriver instance
            
        Raises:
            RuntimeError: If driver creation fails
        """
        try:
            self.logger.info(
                "Creating Chrome WebDriver instance",
                headless=self.config.headless,
                stealth_enabled=self.config.enable_stealth,
                window_size=f"{self.config.window_width}x{self.config.window_height}",
            )
            
            options = self._build_chrome_options()
            service = self._build_chrome_service()
            
            # Create driver
            driver = webdriver.Chrome(
                service=service,
                options=options,
            )
            
            # Configure timeouts
            driver.set_page_load_timeout(self.config.page_load_timeout)
            driver.implicitly_wait(self.config.implicit_wait_timeout)
            driver.set_script_timeout(self.config.script_timeout)
            
            # Set window size
            driver.set_window_size(self.config.window_width, self.config.window_height)
            
            # Apply stealth measures
            if self.config.enable_stealth:
                apply_stealth_measures(driver)
            
            self.logger.info(
                "Chrome WebDriver created successfully",
                browser_version=driver.capabilities.get("browserVersion"),
                driver_version=driver.capabilities.get("chrome", {}).get("chromedriverVersion"),
            )
            
            return driver
            
        except Exception as e:
            self.logger.error(
                "Failed to create Chrome WebDriver",
                error=str(e),
                error_type=type(e).__name__,
            )
            raise RuntimeError(f"Failed to create WebDriver: {e}") from e
    
    def _build_chrome_options(self) -> Options:
        """Build Chrome options with anti-detection measures."""
        options = Options()
        
        # Basic options
        if self.config.headless:
            options.add_argument("--headless=new")
        
        options.add_argument(f"--window-size={self.config.window_width},{self.config.window_height}")
        
        # Anti-detection arguments
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-automation")
        options.add_argument("--disable-extensions-file-access-check")
        options.add_argument("--disable-extensions-http-throttling") 
        options.add_argument("--disable-features=VizDisplayCompositor")
        options.add_argument("--disable-ipc-flooding-protection")
        options.add_argument("--no-first-run")
        options.add_argument("--no-service-autorun")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--password-store=basic")
        options.add_argument("--use-mock-keychain")
        options.add_argument("--lang=en-US,en;q=0.9")
        
        # User agent
        if self.config.user_agent:
            options.add_argument(f"--user-agent={self.config.user_agent}")
        else:
            # Use a realistic user agent
            default_ua = (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
            options.add_argument(f"--user-agent={default_ua}")
        
        # Binary path
        if self.config.chrome_binary_path:
            options.binary_location = self.config.chrome_binary_path
        
        # Profile directory
        if self.config.profile_directory:
            options.add_argument(f"--user-data-dir={self.config.profile_directory}")
        else:
            # Create temporary profile directory
            temp_dir = tempfile.mkdtemp(prefix="linkedin_scraper_profile_")
            self._temp_dirs.append(temp_dir)
            options.add_argument(f"--user-data-dir={temp_dir}")
        
        # Performance optimizations
        if self.config.disable_images:
            options.add_argument("--disable-images")
            
        if self.config.disable_javascript:
            options.add_argument("--disable-javascript")
            
        if self.config.disable_plugins:
            options.add_argument("--disable-plugins")
            
        if self.config.disable_extensions:
            options.add_argument("--disable-extensions")
            
        if self.config.disable_dev_shm_usage:
            options.add_argument("--disable-dev-shm-usage")
            
        if self.config.no_sandbox:
            options.add_argument("--no-sandbox")
        
        # Memory and performance
        options.add_argument("--memory-pressure-off")
        options.add_argument("--max_old_space_size=4096")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-backgrounding-occluded-windows")
        
        # Proxy configuration
        if self.config.proxy_server:
            options.add_argument(f"--proxy-server={self.config.proxy_server}")
            
        # Download directory
        if self.config.download_directory:
            Path(self.config.download_directory).mkdir(parents=True, exist_ok=True)
            
        # Extra arguments
        for arg in self.config.extra_arguments:
            options.add_argument(arg)
        
        # Experimental options
        experimental_options = {
            "excludeSwitches": ["enable-automation", "enable-logging"],
            "useAutomationExtension": False,
            "detach": True,
        }
        experimental_options.update(self.config.extra_experimental_options)
        
        for key, value in experimental_options.items():
            options.add_experimental_option(key, value)
        
        # Preferences
        prefs = {
            "profile.default_content_setting_values": {
                "notifications": 2,  # Block notifications
                "geolocation": 2,    # Block location sharing
                "media_stream": 2,   # Block camera/microphone
            },
            "profile.managed_default_content_settings": {
                "images": 1 if not self.config.disable_images else 2,
            },
            "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,
        }
        
        if self.config.download_directory:
            prefs["download.default_directory"] = str(Path(self.config.download_directory).absolute())
            prefs["download.prompt_for_download"] = False
            prefs["download.directory_upgrade"] = True
            prefs["safebrowsing.enabled"] = True
        
        # Proxy authentication
        if self.config.proxy_username and self.config.proxy_password:
            prefs["profile.http_auth.enabled"] = True
        
        prefs.update(self.config.extra_prefs)
        options.add_experimental_option("prefs", prefs)
        
        return options
    
    def _build_chrome_service(self) -> Service:
        """Build Chrome service configuration."""
        service_args = [
            "--disable-build-check",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--log-level=3",  # Suppress INFO messages
        ]
        
        service = Service(
            executable_path=self.config.chromedriver_path,
            service_args=service_args,
        )
        
        return service
    
    def cleanup(self) -> None:
        """Clean up temporary directories and resources."""
        import shutil
        
        for temp_dir in self._temp_dirs:
            try:
                shutil.rmtree(temp_dir, ignore_errors=True)
                self.logger.debug("Cleaned up temporary directory", path=temp_dir)
            except Exception as e:
                self.logger.warning(
                    "Failed to clean up temporary directory",
                    path=temp_dir,
                    error=str(e),
                )
        
        self._temp_dirs.clear()
    
    def __del__(self):
        """Cleanup when factory is destroyed."""
        self.cleanup()


def create_default_driver(
    headless: bool = True,
    enable_stealth: bool = True,
    window_size: tuple[int, int] = (1280, 900),
) -> webdriver.Chrome:
    """
    Create a Chrome driver with sensible defaults for LinkedIn scraping.
    
    Args:
        headless: Whether to run in headless mode
        enable_stealth: Whether to apply stealth measures
        window_size: Browser window size as (width, height)
        
    Returns:
        Configured Chrome WebDriver instance
    """
    config = DriverConfig(
        headless=headless,
        enable_stealth=enable_stealth,
        window_width=window_size[0],
        window_height=window_size[1],
        disable_images=False,  # Keep images for better detection evasion
        disable_plugins=True,
        disable_extensions=True,
        no_sandbox=os.getenv("DOCKER_ENVIRONMENT") == "true",  # Enable in Docker
    )
    
    factory = DriverFactory(config)
    return factory.create_driver()


def get_driver_info(driver: webdriver.Chrome) -> Dict[str, any]:
    """
    Get information about the WebDriver instance.
    
    Args:
        driver: Chrome WebDriver instance
        
    Returns:
        Dictionary with driver information
    """
    try:
        capabilities = driver.capabilities
        return {
            "browser_name": capabilities.get("browserName"),
            "browser_version": capabilities.get("browserVersion"),
            "driver_version": capabilities.get("chrome", {}).get("chromedriverVersion"),
            "platform": capabilities.get("platformName"),
            "headless": "--headless" in driver.service.service_args,
            "window_size": driver.get_window_size(),
            "user_agent": driver.execute_script("return navigator.userAgent;"),
        }
    except Exception as e:
        logger.warning("Failed to get driver info", error=str(e))
        return {} 