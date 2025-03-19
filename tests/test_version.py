"""Test version information."""

# Import local modules
from your_project_name import __version__


def test_version():
    """Test that version is a string."""
    assert isinstance(__version__, str)
