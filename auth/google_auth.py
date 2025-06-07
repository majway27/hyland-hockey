import os.path
import pickle
from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from config.config_manager import ConfigManager

def get_credentials():
    """
    Get Google API credentials, either from existing token or by initiating OAuth flow.
    
    Returns:
        google.oauth2.credentials.Credentials: The credentials object for Google API access
    """
    config = ConfigManager()
    creds = None
    
    # Get the config directory path
    config_dir = Path(__file__).parent.parent / 'config'
    token_path = config_dir / 'token.pickle'
    credentials_path = config_dir / 'credentials.json'
    
    # The file token.pickle stores the user's access and refresh tokens
    if token_path.exists():
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
            
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(credentials_path), config.scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
            
    return creds 