"""
Configuration settings for the jersey order management system.
Loads settings from a local YAML file.
"""

import os
from ruamel.yaml import YAML
from pathlib import Path

def load_config():
    """Load configuration from YAML file."""
    # Get the directory where this config.py file is located
    current_dir = Path(__file__).parent
    config_path = current_dir / 'config.yaml'
    
    if not config_path.exists():
        template_path = current_dir / 'config.yaml.template'
        if template_path.exists():
            raise FileNotFoundError(
                "config.yaml not found. Please copy config.yaml.template to config.yaml "
                "and update the values."
            )
        else:
            raise FileNotFoundError(
                "Neither config.yaml nor config.yaml.template found."
            )
    
    yaml = YAML(typ='safe')
    with open(config_path) as f:
        return yaml.load(f)

# Load configuration
config = load_config()

# Export configuration values
WORKSHEET_NAME = config['worksheet_name']
SENDER_EMAIL = config['sender_email']
DEFAULT_TO_EMAIL = config['default_to_email']
SCOPES = config['scopes'] 