#!/usr/bin/env python
"""Example of using the CLI functionality of your-project-name."""

# Import built-in modules
import subprocess
import sys


def main():
    """Main function to demonstrate CLI usage."""
    print("Running CLI with --help flag:")
    result = subprocess.run(
        [sys.executable, "-m", "your_project_name", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    print(result.stdout)
    
    print("\nRunning CLI with --version flag:")
    result = subprocess.run(
        [sys.executable, "-m", "your_project_name", "--version"],
        capture_output=True,
        text=True,
        check=False,  # Version flag exits with code 0, but subprocess might see it as an error
    )
    print(result.stdout)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
