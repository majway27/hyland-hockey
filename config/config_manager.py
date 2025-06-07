"""
Configuration manager for the jersey order management system.
Provides a class-based interface to access configuration settings.
"""

import os
from pathlib import Path
from ruamel.yaml import YAML
from typing import Any, Dict, List, Optional


class ConfigManager:
    """Manages configuration settings loaded from YAML files."""
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize the configuration manager.
        
        Args:
            config_file: Optional path to a specific config file. If not provided,
                        will look for config.yaml in the config directory.
        """
        self._config: Dict[str, Any] = {}
        self._load_config(config_file)
    
    def _load_config(self, config_file: Optional[str] = None) -> None:
        """Load configuration from YAML file."""
        if config_file is None:
            # Get the directory where this file is located
            current_dir = Path(__file__).parent
            config_path = current_dir / 'config.yaml'
        else:
            config_path = Path(config_file)
        
        if not config_path.exists():
            template_path = config_path.parent / 'config.yaml.template'
            if template_path.exists():
                raise FileNotFoundError(
                    f"config.yaml not found at {config_path}. Please copy "
                    f"config.yaml.template to config.yaml and update the values."
                )
            else:
                raise FileNotFoundError(
                    f"Neither config.yaml nor config.yaml.template found in {config_path.parent}"
                )
        
        yaml = YAML(typ='safe')
        with open(config_path) as f:
            self._config = yaml.load(f)
    
    @property
    def scopes(self) -> List[str]:
        """Get Google API scopes."""
        return self._config['scopes']
    
    @property
    def demo_worksheet_name(self) -> str:
        """Get demo worksheet name."""
        return self._config['demo_worksheet_name']
    
    @property
    def jersey_worksheet_name(self) -> str:
        """Get jersey worksheet name."""
        return self._config['jersey_worksheet_name']
    
    @property
    def demo_sender_email(self) -> str:
        """Get demo sender email."""
        return self._config['demo_sender_email']
    
    @property
    def demo_default_to_email(self) -> str:
        """Get demo default recipient email."""
        return self._config['demo_default_to_email']
    
    @property
    def jersey_sender_email(self) -> str:
        """Get jersey sender email."""
        return self._config['jersey_sender_email']
    
    @property
    def jersey_default_to_email(self) -> str:
        """Get jersey default recipient email."""
        return self._config['jersey_default_to_email']
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value by key.
        
        Args:
            key: The configuration key to look up
            default: Default value to return if key is not found
            
        Returns:
            The configuration value or default if not found
        """
        return self._config.get(key, default) 