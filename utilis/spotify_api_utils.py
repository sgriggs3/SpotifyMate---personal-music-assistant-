import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize the Spotify client with credentials
def initialize_spotify_client(client_id, client_secret):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

# Fetch track details using the Spotify Web API
def fetch_track_details(sp, track_id):
    track = sp.track(track_id)
    return track

# Fetch user's recently played tracks
def fetch_user_recently_played(sp, limit=20):
    results = sp.current_user_recently_played(limit=limit)
    return results
