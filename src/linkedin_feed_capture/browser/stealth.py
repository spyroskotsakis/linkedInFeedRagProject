"""
Stealth measures and anti-detection techniques for web scraping.

Implements various techniques to make the browser appear more human-like
and avoid detection by anti-bot systems.
"""

import random
import time
from dataclasses import dataclass
from typing import Optional

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from linkedin_feed_capture.utils.logger import get_logger

logger = get_logger(__name__)


@dataclass
class StealthConfig:
    """Configuration for stealth measures."""
    
    randomize_viewport: bool = True
    viewport_variations: list[tuple[int, int]] = None
    inject_webdriver_fixes: bool = True
    randomize_user_agent: bool = False
    user_agent_pool: list[str] = None
    simulate_human_behavior: bool = True
    mouse_movement_frequency: float = 0.3  # Probability of mouse movement
    random_delays: bool = True
    delay_range: tuple[float, float] = (0.5, 2.0)
    
    def __post_init__(self):
        if self.viewport_variations is None:
            self.viewport_variations = [
                (1280, 900), (1366, 768), (1920, 1080),
                (1440, 900), (1536, 864), (1600, 900),
            ]
        
        if self.user_agent_pool is None:
            self.user_agent_pool = [
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            ]


def apply_stealth_measures(
    driver: webdriver.Chrome,
    config: Optional[StealthConfig] = None,
) -> None:
    """
    Apply comprehensive stealth measures to the WebDriver.
    
    Args:
        driver: Chrome WebDriver instance
        config: Stealth configuration
    """
    if config is None:
        config = StealthConfig()
    
    logger.info("Applying stealth measures to WebDriver")
    
    # Randomize viewport if enabled
    if config.randomize_viewport:
        _randomize_viewport(driver, config.viewport_variations)
    
    # Inject JavaScript fixes for WebDriver detection
    if config.inject_webdriver_fixes:
        _inject_webdriver_fixes(driver)
    
    # Inject additional stealth scripts
    _inject_stealth_scripts(driver)
    
    logger.info("Stealth measures applied successfully")


def _randomize_viewport(
    driver: webdriver.Chrome,
    viewport_variations: list[tuple[int, int]],
) -> None:
    """Randomize the browser viewport size."""
    width, height = random.choice(viewport_variations)
    driver.set_window_size(width, height)
    
    logger.debug(
        "Randomized viewport size",
        width=width,
        height=height,
    )


def _inject_webdriver_fixes(driver: webdriver.Chrome) -> None:
    """Inject JavaScript to fix WebDriver detection vectors."""
    
    # Remove webdriver property
    script = """
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined,
    });
    """
    driver.execute_script(script)
    
    # Fix chrome runtime
    script = """
    window.chrome = {
        runtime: {},
        loadTimes: function() {},
        csi: function() {},
        app: {}
    };
    """
    driver.execute_script(script)
    
    # Fix permissions
    script = """
    const originalQuery = window.navigator.permissions.query;
    return window.navigator.permissions.query = (parameters) => (
        parameters.name === 'notifications' ?
            Promise.resolve({ state: Notification.permission }) :
            originalQuery(parameters)
    );
    """
    driver.execute_script(script)
    
    # Fix plugins
    script = """
    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3, 4, 5],
    });
    """
    driver.execute_script(script)
    
    # Fix languages
    script = """
    Object.defineProperty(navigator, 'languages', {
        get: () => ['en-US', 'en'],
    });
    """
    driver.execute_script(script)


def _inject_stealth_scripts(driver: webdriver.Chrome) -> None:
    """Inject additional stealth scripts."""
    
    # Override Date.getTimezoneOffset for consistency
    script = """
    Date.prototype.getTimezoneOffset = function() {
        return 0; // UTC
    };
    """
    driver.execute_script(script)
    
    # Mock battery API
    script = """
    Object.defineProperty(navigator, 'getBattery', {
        get: () => () => Promise.resolve({
            charging: true,
            chargingTime: 0,
            dischargingTime: Infinity,
            level: 1,
            addEventListener: () => {},
            removeEventListener: () => {},
        }),
    });
    """
    driver.execute_script(script)
    
    # Mock geolocation
    script = """
    Object.defineProperty(navigator.geolocation, 'getCurrentPosition', {
        get: () => (success, error) => {
            if (error) {
                error({ code: 1, message: 'User denied geolocation' });
            }
        },
    });
    """
    driver.execute_script(script)


def simulate_human_scroll(
    driver: webdriver.Chrome,
    scroll_pause_range: tuple[float, float] = (1.0, 3.0),
    scroll_pixels_range: tuple[int, int] = (300, 800),
    smooth_scroll: bool = True,
) -> None:
    """
    Simulate human-like scrolling behavior.
    
    Args:
        driver: Chrome WebDriver instance
        scroll_pause_range: Range for pause between scrolls (min, max) in seconds
        scroll_pixels_range: Range for scroll distance (min, max) in pixels
        smooth_scroll: Whether to use smooth scrolling
    """
    scroll_pixels = random.randint(*scroll_pixels_range)
    
    if smooth_scroll:
        # Smooth scroll in smaller increments
        increments = random.randint(5, 15)
        pixels_per_increment = scroll_pixels // increments
        
        for _ in range(increments):
            driver.execute_script(f"window.scrollBy(0, {pixels_per_increment});")
            time.sleep(random.uniform(0.05, 0.15))
    else:
        # Single scroll
        driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")
    
    # Pause after scrolling
    pause_time = random.uniform(*scroll_pause_range)
    time.sleep(pause_time)
    
    logger.debug(
        "Simulated human scroll",
        scroll_pixels=scroll_pixels,
        pause_time=round(pause_time, 2),
        smooth=smooth_scroll,
    )


def simulate_mouse_movement(
    driver: webdriver.Chrome,
    target_element=None,
    randomize: bool = True,
) -> None:
    """
    Simulate random mouse movements to appear more human.
    
    Args:
        driver: Chrome WebDriver instance
        target_element: Element to move towards (optional)
        randomize: Whether to randomize the movement
    """
    actions = ActionChains(driver)
    
    if target_element:
        # Move towards the target element with some randomization
        if randomize:
            offset_x = random.randint(-50, 50)
            offset_y = random.randint(-20, 20)
            actions.move_to_element_with_offset(target_element, offset_x, offset_y)
        else:
            actions.move_to_element(target_element)
    else:
        # Random movement within viewport
        viewport_size = driver.get_window_size()
        x = random.randint(100, viewport_size['width'] - 100)
        y = random.randint(100, viewport_size['height'] - 100)
        
        # Get current viewport position to calculate absolute coordinates
        body_element = driver.find_element(By.TAG_NAME, "body")
        actions.move_to_element_with_offset(body_element, x, y)
    
    # Execute the movement
    actions.perform()
    
    logger.debug("Simulated mouse movement")


def simulate_reading_pause(
    content_length: int = 100,
    base_time: float = 2.0,
    reading_speed_wpm: int = 200,
) -> None:
    """
    Simulate a realistic reading pause based on content length.
    
    Args:
        content_length: Number of characters in content
        base_time: Base pause time in seconds
        reading_speed_wpm: Reading speed in words per minute
    """
    # Estimate reading time (assuming 5 characters per word)
    estimated_words = content_length / 5
    reading_time = (estimated_words / reading_speed_wpm) * 60
    
    # Add base time and some randomization
    total_pause = base_time + reading_time + random.uniform(0.5, 2.0)
    
    # Cap the maximum pause
    total_pause = min(total_pause, 10.0)
    
    time.sleep(total_pause)
    
    logger.debug(
        "Simulated reading pause",
        content_length=content_length,
        pause_duration=round(total_pause, 2),
    )


def add_human_delay(
    base_delay: float = 1.0,
    jitter_range: tuple[float, float] = (0.5, 1.5),
) -> None:
    """
    Add a human-like delay with jitter.
    
    Args:
        base_delay: Base delay in seconds
        jitter_range: Range for jitter multiplier (min, max)
    """
    jitter = random.uniform(*jitter_range)
    total_delay = base_delay * jitter
    time.sleep(total_delay)
    
    logger.debug(
        "Added human delay",
        base_delay=base_delay,
        jitter_multiplier=round(jitter, 2),
        total_delay=round(total_delay, 2),
    )


def is_likely_detected(driver: webdriver.Chrome) -> bool:
    """
    Check if the browser is likely detected as a bot.
    
    Args:
        driver: Chrome WebDriver instance
        
    Returns:
        True if detection is likely, False otherwise
    """
    try:
        # Check for common detection indicators
        page_source = driver.page_source.lower()
        
        detection_indicators = [
            "captcha",
            "please verify",
            "unusual traffic",
            "automated requests",
            "bot detected",
            "access denied",
            "security check",
            "prove you're human",
        ]
        
        for indicator in detection_indicators:
            if indicator in page_source:
                logger.warning(
                    "Potential bot detection",
                    indicator=indicator,
                    current_url=driver.current_url,
                )
                return True
        
        # Check for specific LinkedIn detection patterns
        linkedin_detection_patterns = [
            "authwall",
            "challenge",
            "verification",
            "blocked",
        ]
        
        for pattern in linkedin_detection_patterns:
            if pattern in page_source:
                logger.warning(
                    "LinkedIn-specific detection pattern found",
                    pattern=pattern,
                    current_url=driver.current_url,
                )
                return True
        
        # Check current URL for redirects to challenge pages
        current_url = driver.current_url.lower()
        if any(pattern in current_url for pattern in ["challenge", "verify", "captcha"]):
            logger.warning(
                "Redirected to challenge page",
                current_url=driver.current_url,
            )
            return True
        
        return False
        
    except Exception as e:
        logger.error(
            "Error checking for detection",
            error=str(e),
            error_type=type(e).__name__,
        )
        return False 