"""
Unit tests for CLI module.

Tests command-line interface, argument parsing, and main execution flow.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import tempfile
import json
from typer.testing import CliRunner

from linkedin_feed_capture.cli.main import (
    app,
    main,
    capture,
    auth_info,
    test_connection
)


class TestCliApp:
    """Test cases for CLI application."""
    
    def test_app_exists(self):
        """Test that the CLI app is properly initialized."""
        assert app is not None
        assert hasattr(app, 'command')
    
    def test_cli_runner_works(self):
        """Test that the CLI runner can execute basic commands."""
        runner = CliRunner()
        result = runner.invoke(app, ["--help"])
        
        assert result.exit_code == 0
        assert "LinkedIn" in result.stdout


class TestMainFunction:
    """Test cases for main function."""
    
    @patch('linkedin_feed_capture.cli.main.app')
    def test_main_calls_app(self, mock_app):
        """Test that main function calls the Typer app."""
        main()
        mock_app.assert_called_once()


class TestCaptureCommand:
    """Test cases for capture command."""
    
    def test_capture_help(self):
        """Test capture command help."""
        runner = CliRunner()
        result = runner.invoke(app, ["capture", "--help"])
        
        assert result.exit_code == 0
        assert "capture" in result.stdout.lower()


class TestAuthInfoCommand:
    """Test cases for auth-info command."""
    
    def test_auth_info_help(self):
        """Test auth-info command help."""
        runner = CliRunner()
        result = runner.invoke(app, ["auth-info", "--help"])
        
        assert result.exit_code == 0
        assert "auth-info" in result.stdout.lower()


class TestTestConnectionCommand:
    """Test cases for test-connection command."""
    
    def test_test_connection_help(self):
        """Test test-connection command help."""
        runner = CliRunner()
        result = runner.invoke(app, ["test-connection", "--help"])
        
        assert result.exit_code == 0
        assert "test-connection" in result.stdout.lower()


class TestCliIntegration:
    """Integration tests for CLI functionality."""
    
    def test_cli_app_commands_exist(self):
        """Test that expected CLI commands are available."""
        runner = CliRunner()
        result = runner.invoke(app, ["--help"])
        
        assert result.exit_code == 0
        
        # Check that main commands are listed
        commands = ["capture", "auth-info", "test-connection"]
        
        for command in commands:
            assert command in result.stdout
    
    def test_cli_error_handling(self):
        """Test CLI error handling for invalid commands."""
        runner = CliRunner()
        result = runner.invoke(app, ["invalid-command"])
        
        assert result.exit_code != 0 