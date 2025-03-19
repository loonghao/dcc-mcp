"""Command-line interface for the project."""

# Import built-in modules
import argparse
import sys
from typing import List, Optional

# Import local modules
from .__version__ import __version__


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse command line arguments.
    
    Args:
        args: Command line arguments. If None, uses sys.argv.
        
    Returns:
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Your project description",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Show version and exit",
    )
    
    # Add your arguments here
    parser.add_argument(
        "-c", "--config",
        help="Path to configuration file",
    )
    
    return parser.parse_args(args)


def main(args: Optional[List[str]] = None) -> int:
    """Main entry point for the application.
    
    Args:
        args: Command line arguments. If None, uses sys.argv.
        
    Returns:
        Exit code.
    """
    parsed_args = parse_args(args)
    
    # Your application logic here
    print(f"Running your_project_name version {__version__}")
    
    if parsed_args.config:
        print(f"Using configuration file: {parsed_args.config}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
