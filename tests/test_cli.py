"""Tests for the CLI module."""

# Import built-in modules
from unittest import mock

# Import local modules
from your_project_name.cli import main


def test_main_returns_zero():
    """Test that the main function returns zero."""
    result = main(["--help"])
    assert result == 0


def test_version_flag():
    """Test that the version flag works."""
    with mock.patch("sys.stdout") as mock_stdout:
        with mock.patch("sys.exit") as mock_exit:
            main(["--version"])
            mock_exit.assert_called_once()


def test_config_flag():
    """Test that the config flag works."""
    with mock.patch("builtins.print") as mock_print:
        main(["--config", "test_config.json"])
        mock_print.assert_any_call("Using configuration file: test_config.json")
