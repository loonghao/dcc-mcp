"""Configuration handling for the project."""

# Import built-in modules
from pathlib import Path
from typing import Dict, Optional, Union

# Import third-party modules
from platformdirs import user_config_dir

# Constants
APP_NAME = "your_project_name"
CONFIG_DIR = Path(user_config_dir(APP_NAME))
DEFAULT_CONFIG_PATH = CONFIG_DIR / "config.json"


def ensure_config_dir() -> None:
    """Ensure the configuration directory exists."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def get_config(config_path: Optional[Union[str, Path]] = None) -> Dict:
    """Get configuration from file.
    
    Args:
        config_path: Path to configuration file. If None, uses default path.
        
    Returns:
        Configuration dictionary.
    """
    import json
    
    if config_path is None:
        config_path = DEFAULT_CONFIG_PATH
    else:
        config_path = Path(config_path)
    
    if not config_path.exists():
        return {}
    
    with open(config_path, "r") as f:
        return json.load(f)


def save_config(config: Dict, config_path: Optional[Union[str, Path]] = None) -> None:
    """Save configuration to file.
    
    Args:
        config: Configuration dictionary to save.
        config_path: Path to save configuration to. If None, uses default path.
    """
    import json
    
    if config_path is None:
        config_path = DEFAULT_CONFIG_PATH
    else:
        config_path = Path(config_path)
    
    ensure_config_dir()
    
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
