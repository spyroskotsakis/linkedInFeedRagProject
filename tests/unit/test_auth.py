"""
Unit tests for authentication module.

Tests cookie management, authentication flows, and session handling.
"""

import pytest
import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta
from cryptography.fernet import Fernet

from linkedin_feed_capture.auth.cookies import (
    CookieManager,
    CookieStore,
    CookieData,
    CookieError,
    CookieEncryptionError,
    CookieExpiredError
)
from linkedin_feed_capture.auth.authenticator import (
    LinkedInAuthenticator,
    AuthConfig,
    AuthenticationError,
    LoginFailedError,
    CaptchaRequiredError,
    TwoFactorRequiredError
)


class TestCookieData:
    """Test cases for CookieData dataclass."""
    
    def test_cookie_data_creation(self):
        """Test creating cookie data."""
        cookie_data = CookieData(
            cookies=[{'name': 'session', 'value': 'abc123'}],
            timestamp=datetime.now(),
            user_agent="test-agent"
        )
        
        assert len(cookie_data.cookies) == 1
        assert cookie_data.cookies[0]['name'] == 'session'
        assert cookie_data.user_agent == "test-agent"
        assert isinstance(cookie_data.timestamp, datetime)
    
    def test_cookie_data_expiry_check(self):
        """Test cookie data expiry check."""
        # Fresh cookie
        fresh_cookie = CookieData(
            cookies=[],
            timestamp=datetime.now(),
            user_agent="test"
        )
        assert fresh_cookie.is_expired() is False
        
        # Expired cookie
        expired_cookie = CookieData(
            cookies=[],
            timestamp=datetime.now() - timedelta(days=8),
            user_agent="test"
        )
        assert expired_cookie.is_expired() is True


class TestCookieStore:
    """Test cases for CookieStore dataclass."""
    
    def test_cookie_store_creation(self):
        """Test creating cookie store."""
        cookie_data = CookieData(
            cookies=[],
            timestamp=datetime.now(),
            user_agent="test"
        )
        
        store = CookieStore(
            data=cookie_data,
            checksum="abc123"
        )
        
        assert store.data == cookie_data
        assert store.checksum == "abc123"


class TestCookieManager:
    """Test cases for CookieManager."""
    
    def test_init_with_custom_key(self):
        """Test initialization with custom encryption key."""
        key = Fernet.generate_key()
        manager = CookieManager(encryption_key=key)
        
        assert manager.encryption_key == key
        assert isinstance(manager.fernet, Fernet)
    
    def test_init_generates_key_if_none(self):
        """Test that key is generated if none provided."""
        manager = CookieManager()
        
        assert manager.encryption_key is not None
        assert isinstance(manager.fernet, Fernet)
    
    @patch('builtins.open', create=True)
    @patch('pathlib.Path.exists')
    def test_save_cookies_success(self, mock_exists, mock_open):
        """Test successful cookie saving."""
        mock_exists.return_value = True
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        
        manager = CookieManager()
        cookies = [{'name': 'test', 'value': 'value'}]
        
        result = manager.save_cookies(cookies, "test-agent")
        
        assert result is True
        mock_open.assert_called_once()
        mock_file.write.assert_called_once()
    
    @patch('builtins.open', create=True)
    @patch('pathlib.Path.exists')
    def test_save_cookies_file_error(self, mock_exists, mock_open):
        """Test cookie saving with file error."""
        mock_exists.return_value = True
        mock_open.side_effect = IOError("File write error")
        
        manager = CookieManager()
        cookies = [{'name': 'test', 'value': 'value'}]
        
        result = manager.save_cookies(cookies, "test-agent")
        
        assert result is False
    
    @patch('builtins.open', create=True)
    @patch('pathlib.Path.exists')
    def test_load_cookies_success(self, mock_exists, mock_open):
        """Test successful cookie loading."""
        # Create test data
        manager = CookieManager()
        cookie_data = CookieData(
            cookies=[{'name': 'test', 'value': 'value'}],
            timestamp=datetime.now(),
            user_agent="test-agent"
        )
        store = CookieStore(data=cookie_data, checksum="test")
        encrypted_data = manager.fernet.encrypt(json.dumps(store.__dict__, default=str).encode())
        
        mock_exists.return_value = True
        mock_file = MagicMock()
        mock_file.read.return_value = encrypted_data
        mock_open.return_value.__enter__.return_value = mock_file
        
        result = manager.load_cookies()
        
        assert result is not None
        assert len(result) == 1
        assert result[0]['name'] == 'test'
    
    @patch('pathlib.Path.exists')
    def test_load_cookies_file_not_exists(self, mock_exists):
        """Test loading cookies when file doesn't exist."""
        mock_exists.return_value = False
        
        manager = CookieManager()
        result = manager.load_cookies()
        
        assert result is None
    
    @patch('builtins.open', create=True)
    @patch('pathlib.Path.exists')
    def test_load_cookies_expired(self, mock_exists, mock_open):
        """Test loading expired cookies."""
        # Create expired test data
        manager = CookieManager()
        cookie_data = CookieData(
            cookies=[{'name': 'test', 'value': 'value'}],
            timestamp=datetime.now() - timedelta(days=8),
            user_agent="test-agent"
        )
        store = CookieStore(data=cookie_data, checksum="test")
        encrypted_data = manager.fernet.encrypt(json.dumps(store.__dict__, default=str).encode())
        
        mock_exists.return_value = True
        mock_file = MagicMock()
        mock_file.read.return_value = encrypted_data
        mock_open.return_value.__enter__.return_value = mock_file
        
        with pytest.raises(CookieExpiredError):
            manager.load_cookies()
    
    def test_apply_cookies_to_driver(self):
        """Test applying cookies to WebDriver."""
        mock_driver = Mock()
        mock_driver.current_url = "https://linkedin.com"
        
        manager = CookieManager()
        cookies = [
            {'name': 'session', 'value': 'abc123', 'domain': '.linkedin.com'},
            {'name': 'csrf', 'value': 'xyz789', 'domain': '.linkedin.com'}
        ]
        
        manager.apply_cookies_to_driver(mock_driver, cookies)
        
        # Should be called twice for two cookies
        assert mock_driver.add_cookie.call_count == 2
    
    def test_apply_cookies_different_domain(self):
        """Test applying cookies with domain mismatch."""
        mock_driver = Mock()
        mock_driver.current_url = "https://example.com"
        
        manager = CookieManager()
        cookies = [{'name': 'test', 'value': 'value', 'domain': '.linkedin.com'}]
        
        # Should not raise error but skip cookie
        manager.apply_cookies_to_driver(mock_driver, cookies)
        
        mock_driver.add_cookie.assert_not_called()
    
    @patch('pathlib.Path.unlink')
    @patch('pathlib.Path.exists')
    def test_delete_cookies(self, mock_exists, mock_unlink):
        """Test cookie deletion."""
        mock_exists.return_value = True
        
        manager = CookieManager()
        result = manager.delete_cookies()
        
        assert result is True
        mock_unlink.assert_called_once()
    
    @patch('pathlib.Path.exists')
    def test_delete_cookies_not_exists(self, mock_exists):
        """Test deleting non-existent cookies."""
        mock_exists.return_value = False
        
        manager = CookieManager()
        result = manager.delete_cookies()
        
        assert result is True  # Should succeed even if file doesn't exist


class TestAuthConfig:
    """Test cases for AuthConfig."""
    
    def test_default_config(self):
        """Test default authentication configuration."""
        config = AuthConfig(
            username="test@example.com",
            password="password123"
        )
        
        assert config.username == "test@example.com"
        assert config.password == "password123"
        assert config.cookie_file == "linkedin_cookies.enc"
        assert config.login_timeout == 30
        assert config.max_login_attempts == 3
        assert config.enable_2fa is False
        assert config.headless is True
        assert config.user_agent is None

    def test_custom_config(self):
        """Test custom authentication configuration."""
        config = AuthConfig(
            username="user@test.com",
            password="pass",
            cookie_file="custom_cookies.enc",
            login_timeout=60,
            max_login_attempts=5,
            enable_2fa=True,
            headless=False,
            user_agent="custom-agent"
        )
        
        assert config.username == "user@test.com"
        assert config.cookie_file == "custom_cookies.enc"
        assert config.login_timeout == 60
        assert config.max_login_attempts == 5
        assert config.enable_2fa is True
        assert config.headless is False
        assert config.user_agent == "custom-agent"


class TestLinkedInAuthenticator:
    """Test cases for LinkedInAuthenticator."""
    
    def test_init(self):
        """Test authenticator initialization."""
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        assert auth.config == config
        assert auth.cookie_manager is not None
        assert auth.logger is not None
    
    @patch('linkedin_feed_capture.auth.authenticator.CookieManager')
    def test_authenticate_with_cookies_success(self, mock_cookie_manager):
        """Test successful authentication using saved cookies."""
        # Setup
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        mock_driver.current_url = "https://linkedin.com/feed"
        
        mock_cookies = [{'name': 'session', 'value': 'valid'}]
        auth.cookie_manager.load_cookies.return_value = mock_cookies
        
        # Test
        result = auth.authenticate(mock_driver)
        
        # Verify
        assert result is True
        auth.cookie_manager.apply_cookies_to_driver.assert_called_once()
    
    @patch('linkedin_feed_capture.auth.authenticator.CookieManager')
    def test_authenticate_with_invalid_cookies(self, mock_cookie_manager):
        """Test authentication with invalid cookies falls back to login."""
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        mock_driver.current_url = "https://linkedin.com/login"
        
        # Setup cookie loading to return cookies but session validation to fail
        mock_cookies = [{'name': 'session', 'value': 'invalid'}]
        auth.cookie_manager.load_cookies.return_value = mock_cookies
        
        with patch.object(auth, '_try_credential_login', return_value=True):
            result = auth.authenticate(mock_driver)
        
        assert result is True
    
    @patch('linkedin_feed_capture.auth.authenticator.CookieManager')
    def test_authenticate_no_cookies(self, mock_cookie_manager):
        """Test authentication when no cookies available."""
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        auth.cookie_manager.load_cookies.return_value = None
        
        with patch.object(auth, '_try_credential_login', return_value=True):
            result = auth.authenticate(mock_driver)
        
        assert result is True
    
    def test_is_session_valid_success(self):
        """Test session validation when logged in."""
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        mock_driver.current_url = "https://linkedin.com/feed"
        mock_driver.find_elements.return_value = [Mock()]  # Profile element found
        
        result = auth._is_session_valid(mock_driver)
        
        assert result is True
    
    def test_is_session_valid_failure(self):
        """Test session validation when not logged in."""
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        mock_driver.current_url = "https://linkedin.com/login"
        mock_driver.find_elements.return_value = []  # No profile element
        
        result = auth._is_session_valid(mock_driver)
        
        assert result is False
    
    @patch('linkedin_feed_capture.auth.authenticator.WebDriverWait')
    def test_try_credential_login_success(self, mock_wait):
        """Test successful credential login."""
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        mock_driver.get_cookies.return_value = [{'name': 'session', 'value': 'new'}]
        
        # Mock form elements
        mock_username_field = Mock()
        mock_password_field = Mock()
        mock_submit_button = Mock()
        
        mock_driver.find_element.side_effect = [
            mock_username_field,
            mock_password_field,
            mock_submit_button
        ]
        
        # Mock successful login
        with patch.object(auth, '_is_session_valid', return_value=True):
            result = auth._try_credential_login(mock_driver)
        
        assert result is True
        mock_username_field.send_keys.assert_called_once_with("test")
        mock_password_field.send_keys.assert_called_once_with("pass")
        mock_submit_button.click.assert_called_once()
    
    def test_try_credential_login_captcha_detected(self):
        """Test login with CAPTCHA detection."""
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        mock_driver.find_elements.return_value = [Mock()]  # CAPTCHA element found
        
        with pytest.raises(CaptchaRequiredError):
            auth._try_credential_login(mock_driver)
    
    def test_try_credential_login_2fa_detected(self):
        """Test login with 2FA detection."""
        config = AuthConfig(username="test", password="pass", enable_2fa=True)
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        mock_driver.find_elements.side_effect = [
            [],  # No CAPTCHA
            [Mock()]  # 2FA element found
        ]
        
        with pytest.raises(TwoFactorRequiredError):
            auth._try_credential_login(mock_driver)
    
    def test_handle_2fa_timeout(self):
        """Test 2FA handling with timeout."""
        config = AuthConfig(username="test", password="pass", enable_2fa=True)
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        
        with patch('linkedin_feed_capture.auth.authenticator.time.time', side_effect=[0, 61]):
            result = auth._handle_2fa(mock_driver, timeout=60)
        
        assert result is False
    
    def test_cleanup_session(self):
        """Test session cleanup."""
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        
        auth.cleanup_session(mock_driver)
        
        # Should call driver quit
        mock_driver.quit.assert_called_once()


class TestAuthenticationIntegration:
    """Integration tests for authentication flow."""
    
    @patch('linkedin_feed_capture.auth.authenticator.CookieManager')
    def test_full_authentication_flow_with_cookies(self, mock_cookie_manager):
        """Test complete authentication flow using saved cookies."""
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        mock_driver.current_url = "https://linkedin.com/feed"
        
        # Setup successful cookie authentication
        mock_cookies = [{'name': 'session', 'value': 'valid'}]
        auth.cookie_manager.load_cookies.return_value = mock_cookies
        
        with patch.object(auth, '_is_session_valid', return_value=True):
            result = auth.authenticate(mock_driver)
        
        assert result is True
        auth.cookie_manager.apply_cookies_to_driver.assert_called_once()
    
    @patch('linkedin_feed_capture.auth.authenticator.CookieManager')
    def test_full_authentication_flow_with_login(self, mock_cookie_manager):
        """Test complete authentication flow with credential login."""
        config = AuthConfig(username="test", password="pass")
        auth = LinkedInAuthenticator(config)
        
        mock_driver = Mock()
        mock_driver.get_cookies.return_value = [{'name': 'new_session', 'value': 'abc'}]
        
        # No saved cookies available
        auth.cookie_manager.load_cookies.return_value = None
        
        with patch.object(auth, '_try_credential_login', return_value=True):
            result = auth.authenticate(mock_driver)
        
        assert result is True
        auth.cookie_manager.save_cookies.assert_called_once() 