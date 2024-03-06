import pandas as pd
from utils.spotify_api_utils import fetch_track_details  # Assuming this utility is implemented

def collect_user_data(sp, user_id):
    """
    Collects data from a user's Spotify listening history.

    Parameters:
    - sp: Spotify client instance
    - user_id: The Spotify user ID

    Returns:
    - A DataFrame containing the collected user data
    """
    # Placeholder for Spotify API call to fetch user listening history
    # This is an example and needs to be replaced with actual Spotify API calls
    user_data = sp.current_user_recently_played()
    
    # Convert the data to a pandas DataFrame for easier processing
    tracks = []
    for item in user_data['items']:
        track_id = item['track']['id']
        track_details = fetch_track_details(sp, track_id)  # Utility function to fetch track details
        tracks.append(track_details)
    
    df = pd.DataFrame(tracks)
    return df

def preprocess_data(df):
    """
    Preprocesses the collected user data.

    Parameters:
    - df: A DataFrame containing the user data

    Returns:
    - A DataFrame with the preprocessed data
    """
    # Example preprocessing steps:
    # - Handle missing values
    df.dropna(inplace=True)
    
    # - Convert categorical data to numerical (if necessary)
    # This is a placeholder; actual implementation depends on the data and model requirements
    
    return df