#!/usr/bin/env python
"""Basic usage example for your-project-name."""

# Import built-in modules
import sys
import os

# Add the parent directory to sys.path to import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the package
from your_project_name import __version__


def main():
    """Main function to demonstrate basic usage."""
    print(f"Using your-project-name version {__version__}")
    
    # Add your example code here
    print("This is a basic usage example.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
