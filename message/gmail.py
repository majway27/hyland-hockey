"""
Gmail functionality for sending emails.
"""

import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build

from auth.google_auth import get_credentials
from config.config_manager import ConfigManager

def send_gmail(sender_email, to_email, subject, message_text):
    """
    Send an email using Gmail API.
    
    Args:
        sender_email (str): The email address of the sender
        to_email (str): The email address of the recipient
        subject (str): The subject of the email
        message_text (str): The body text of the email
        
    Returns:
        dict: The sent message object
    """
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    # Create message
    message = MIMEMultipart()
    message['to'] = to_email
    message['from'] = sender_email
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    # Encode the message
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    
    try:
        # Send the message
        message = service.users().messages().send(
            userId='me',
            body={'raw': raw_message}
        ).execute()
        print(f'Message Id: {message["id"]}')
        return message
    except Exception as e:
        print(f'An error occurred: {e}')
        return None 