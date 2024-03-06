import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize the Spotify client with environment variables for credentials
client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('SPOTIFY_CLIENT_ID'), 
                                                      client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'))
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def fetch_track_details(track_id):
    """
    Fetches details for a specific track by its Spotify ID, including audio features.
    """
    try:
        track_details = sp.track(track_id)
        audio_features = sp.audio_features(track_id)[0]
    except Exception as e:
        print(f"Error fetching details for track {track_id}: {e}")
        return {}

    # Combine track details with audio features
    details = {**track_details, **audio_features}
    # Simplify the structure if necessary or extract specific fields
    return details

def get_recommendations_based_on_seeds(seed_genres, target_attributes, limit=20):
    """
    Fetches music recommendations from Spotify based on seed genres and target attributes.
    """
    try:
        recommendations = sp.recommendations(seed_genres=seed_genres, limit=limit, **target_attributes)
        recommended_tracks = [track['id'] for track in recommendations['tracks']]
    except Exception as e:
        print(f"Error fetching recommendations: {e}")
        return []

    return recommended_tracks