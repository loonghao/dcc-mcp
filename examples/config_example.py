#!/usr/bin/env python
"""Example of using configuration in your-project-name."""

# Import built-in modules
import json
import os
import sys

# Add the parent directory to sys.path to import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the package
from your_project_name.config import get_config, save_config


def main():
    """Main function to demonstrate configuration usage."""
    # Load example config
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    
    with open(config_path, 'r') as f:
        example_config = json.load(f)
    
    print("Example configuration:")
    print(json.dumps(example_config, indent=2))
    
    # Modify configuration
    example_config['settings']['debug'] = True
    example_config['settings']['log_level'] = 'DEBUG'
    
    # Save modified configuration
    modified_path = os.path.join(os.path.dirname(__file__), 'modified_config.json')
    save_config(example_config, modified_path)
    
    # Load the modified configuration
    loaded_config = get_config(modified_path)
    
    print("\nModified configuration:")
    print(json.dumps(loaded_config, indent=2))
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
