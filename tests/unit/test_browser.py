"""
Unit tests for browser module.

Tests driver factory, configuration, and stealth measures.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from linkedin_feed_capture.browser.driver import DriverFactory, DriverConfig
from linkedin_feed_capture.browser.stealth import (
    StealthConfig, 
    apply_stealth_measures,
    simulate_human_scroll,
    simulate_mouse_movement,
    simulate_reading_pause,
    add_human_delay,
    is_likely_detected
)


class TestDriverConfig:
    """Test cases for DriverConfig."""
    
    def test_default_config(self):
        """Test default driver configuration."""
        config = DriverConfig()
        
        assert config.headless is True
        assert config.window_size == (1920, 1080)
        assert config.user_agent is None
        assert config.proxy is None
        assert config.page_load_timeout == 30
        assert config.implicit_wait == 10
        assert config.download_dir is None
        assert config.disable_images is True
        assert config.disable_css is False
        assert config.disable_javascript is False
        assert config.disable_extensions is True
        assert config.disable_dev_shm is True
        assert config.no_sandbox is True
        assert config.disable_gpu is True
        assert config.disable_notifications is True
        assert config.disable_popup_blocking is False
        assert config.incognito is True
        assert config.disable_logging is True

    def test_custom_config(self):
        """Test custom driver configuration."""
        config = DriverConfig(
            headless=False,
            window_size=(1366, 768),
            user_agent="custom-agent",
            proxy="http://proxy:8080",
            page_load_timeout=60
        )
        
        assert config.headless is False
        assert config.window_size == (1366, 768)
        assert config.user_agent == "custom-agent"
        assert config.proxy == "http://proxy:8080"
        assert config.page_load_timeout == 60


class TestDriverFactory:
    """Test cases for DriverFactory."""
    
    @patch('linkedin_feed_capture.browser.driver.webdriver.Chrome')
    @patch('linkedin_feed_capture.browser.driver.Service')
    def test_create_driver_default(self, mock_service, mock_chrome):
        """Test creating driver with default configuration."""
        mock_driver = Mock()
        mock_chrome.return_value = mock_driver
        
        factory = DriverFactory()
        driver = factory.create_driver()
        
        assert driver == mock_driver
        mock_chrome.assert_called_once()
        mock_driver.implicitly_wait.assert_called_once_with(10)
        mock_driver.set_page_load_timeout.assert_called_once_with(30)
    
    @patch('linkedin_feed_capture.browser.driver.webdriver.Chrome')
    @patch('linkedin_feed_capture.browser.driver.Service')
    def test_create_driver_custom_config(self, mock_service, mock_chrome):
        """Test creating driver with custom configuration."""
        mock_driver = Mock()
        mock_chrome.return_value = mock_driver
        
        config = DriverConfig(
            headless=False,
            page_load_timeout=60,
            implicit_wait=15
        )
        factory = DriverFactory()
        driver = factory.create_driver(config)
        
        assert driver == mock_driver
        mock_driver.implicitly_wait.assert_called_once_with(15)
        mock_driver.set_page_load_timeout.assert_called_once_with(60)
    
    @patch('linkedin_feed_capture.browser.driver.webdriver.Chrome')
    @patch('linkedin_feed_capture.browser.driver.Service')
    def test_create_driver_with_proxy(self, mock_service, mock_chrome):
        """Test creating driver with proxy configuration."""
        mock_driver = Mock()
        mock_chrome.return_value = mock_driver
        
        config = DriverConfig(proxy="http://proxy:8080")
        factory = DriverFactory()
        driver = factory.create_driver(config)
        
        # Verify Chrome was called with options containing proxy
        args, kwargs = mock_chrome.call_args
        options = kwargs.get('options') or args[1] if len(args) > 1 else args[0]
        assert any('--proxy-server=http://proxy:8080' in arg for arg in options.arguments)
    
    @patch('linkedin_feed_capture.browser.driver.webdriver.Chrome')
    @patch('linkedin_feed_capture.browser.driver.Service')
    def test_create_default_driver(self, mock_service, mock_chrome):
        """Test create_default_driver convenience method."""
        mock_driver = Mock()
        mock_chrome.return_value = mock_driver
        
        driver = DriverFactory.create_default_driver()
        
        assert driver == mock_driver
        mock_chrome.assert_called_once()
    
    @patch('linkedin_feed_capture.browser.driver.webdriver.Chrome')
    @patch('linkedin_feed_capture.browser.driver.Service')
    def test_get_driver_info(self, mock_service, mock_chrome):
        """Test getting driver info."""
        mock_driver = Mock()
        mock_driver.capabilities = {
            'browserName': 'chrome',
            'browserVersion': '120.0.0.0',
            'chrome': {'chromedriverVersion': '120.0.0.0'}
        }
        mock_chrome.return_value = mock_driver
        
        factory = DriverFactory()
        driver = factory.create_driver()
        info = factory.get_driver_info(driver)
        
        assert 'browser_name' in info
        assert 'browser_version' in info
        assert 'driver_version' in info


class TestStealthConfig:
    """Test cases for StealthConfig."""
    
    def test_default_config(self):
        """Test default stealth configuration."""
        config = StealthConfig()
        
        assert config.randomize_viewport is True
        assert config.inject_stealth_scripts is True
        assert config.human_delays is True
        assert config.mouse_movements is True
        assert config.scroll_behavior is True
        assert config.reading_pauses is True
        assert config.min_delay == 0.5
        assert config.max_delay == 2.0
        assert config.scroll_pause_min == 1.0
        assert config.scroll_pause_max == 3.0
        assert config.reading_pause_min == 2.0
        assert config.reading_pause_max == 5.0

    def test_custom_config(self):
        """Test custom stealth configuration."""
        config = StealthConfig(
            randomize_viewport=False,
            human_delays=False,
            min_delay=1.0,
            max_delay=5.0
        )
        
        assert config.randomize_viewport is False
        assert config.human_delays is False
        assert config.min_delay == 1.0
        assert config.max_delay == 5.0


class TestStealthMeasures:
    """Test cases for stealth measures."""
    
    def test_apply_stealth_measures_default(self):
        """Test applying stealth measures with default config."""
        mock_driver = Mock()
        
        apply_stealth_measures(mock_driver)
        
        # Verify execute_script was called (for stealth scripts)
        assert mock_driver.execute_script.called
    
    def test_apply_stealth_measures_custom_config(self):
        """Test applying stealth measures with custom config."""
        mock_driver = Mock()
        config = StealthConfig(inject_stealth_scripts=False)
        
        apply_stealth_measures(mock_driver, config)
        
        # Should still be called for viewport randomization
        assert mock_driver.execute_script.called
    
    @patch('linkedin_feed_capture.browser.stealth.time.sleep')
    def test_simulate_human_scroll(self, mock_sleep):
        """Test human-like scrolling simulation."""
        mock_driver = Mock()
        
        simulate_human_scroll(mock_driver, scroll_count=3)
        
        # Verify execute_script was called for scrolling
        assert mock_driver.execute_script.call_count >= 3
        assert mock_sleep.called
    
    @patch('linkedin_feed_capture.browser.stealth.ActionChains')
    def test_simulate_mouse_movement(self, mock_action_chains):
        """Test mouse movement simulation."""
        mock_driver = Mock()
        mock_driver.get_window_size.return_value = {'width': 1920, 'height': 1080}
        mock_actions = Mock()
        mock_action_chains.return_value = mock_actions
        
        simulate_mouse_movement(mock_driver)
        
        mock_action_chains.assert_called_once_with(mock_driver)
        mock_actions.move_by_offset.assert_called()
        mock_actions.perform.assert_called_once()
    
    @patch('linkedin_feed_capture.browser.stealth.time.sleep')
    def test_simulate_reading_pause(self, mock_sleep):
        """Test reading pause simulation."""
        simulate_reading_pause(min_pause=1.0, max_pause=2.0)
        
        mock_sleep.assert_called_once()
        call_args = mock_sleep.call_args[0]
        assert 1.0 <= call_args[0] <= 2.0
    
    @patch('linkedin_feed_capture.browser.stealth.time.sleep')
    def test_add_human_delay(self, mock_sleep):
        """Test human delay addition."""
        add_human_delay(min_delay=0.5, max_delay=1.5)
        
        mock_sleep.assert_called_once()
        call_args = mock_sleep.call_args[0]
        assert 0.5 <= call_args[0] <= 1.5
    
    def test_is_likely_detected_no_detection(self):
        """Test detection check when not detected."""
        mock_driver = Mock()
        mock_driver.current_url = "https://linkedin.com/feed"
        mock_driver.title = "LinkedIn Feed"
        mock_driver.find_elements.return_value = []
        
        result = is_likely_detected(mock_driver)
        
        assert result is False
    
    def test_is_likely_detected_captcha(self):
        """Test detection check when CAPTCHA is present."""
        mock_driver = Mock()
        mock_driver.current_url = "https://linkedin.com/challenge"
        mock_driver.title = "Security Challenge"
        mock_driver.find_elements.return_value = [Mock()]  # CAPTCHA element found
        
        result = is_likely_detected(mock_driver)
        
        assert result is True
    
    def test_is_likely_detected_blocked_url(self):
        """Test detection check with blocked URL."""
        mock_driver = Mock()
        mock_driver.current_url = "https://linkedin.com/checkpoint/lg/sign-in-another-way"
        mock_driver.title = "LinkedIn"
        mock_driver.find_elements.return_value = []
        
        result = is_likely_detected(mock_driver)
        
        assert result is True


class TestStealthIntegration:
    """Integration tests for stealth measures."""
    
    def test_stealth_measures_do_not_break_driver(self):
        """Test that stealth measures don't break normal driver operations."""
        mock_driver = Mock()
        mock_driver.get_window_size.return_value = {'width': 1920, 'height': 1080}
        
        # Apply stealth measures
        apply_stealth_measures(mock_driver)
        
        # Verify driver is still functional
        mock_driver.get.assert_not_called()  # Shouldn't navigate anywhere
        assert mock_driver.execute_script.called  # Should execute stealth scripts
    
    @patch('linkedin_feed_capture.browser.stealth.ActionChains')
    @patch('linkedin_feed_capture.browser.stealth.time.sleep')
    def test_human_behavior_simulation_sequence(self, mock_sleep, mock_action_chains):
        """Test a sequence of human behavior simulations."""
        mock_driver = Mock()
        mock_driver.get_window_size.return_value = {'width': 1920, 'height': 1080}
        mock_actions = Mock()
        mock_action_chains.return_value = mock_actions
        
        # Simulate a sequence of human behaviors
        simulate_mouse_movement(mock_driver)
        simulate_reading_pause()
        simulate_human_scroll(mock_driver, scroll_count=2)
        add_human_delay()
        
        # Verify all behaviors were executed
        mock_action_chains.assert_called()
        assert mock_sleep.call_count >= 3  # At least 3 sleep calls
        assert mock_driver.execute_script.call_count >= 2  # At least 2 scroll scripts 