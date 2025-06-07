"""
Google Sheets operations for the record module.
"""

import pandas as pd
import gspread

from auth.google_auth import get_credentials

def read_google_sheet(sheet_name):
    """
    Read data from a Google Sheet and return it as a pandas DataFrame.
    
    Args:
        sheet_name (str): Name of the Google Sheet to read
        
    Returns:
        pandas.DataFrame: The sheet data as a DataFrame
    """
    creds = get_credentials()
    gc = gspread.authorize(creds)

    # Open the spreadsheet
    spreadsheet = gc.open(sheet_name)

    # Get the first worksheet
    worksheet = spreadsheet.get_worksheet(0)

    # Get all values and convert to pandas DataFrame
    data = worksheet.get_all_values()
    headers = data[0]
    df = pd.DataFrame(data[1:], columns=headers)

    return df 