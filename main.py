import os
import joblib
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils.recommendation_engine import RecommendationEngine
from utils.feedback_processor import FeedbackProcessor
from user_preference_model import UserPreferenceModel
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

def initialize_spotify_client():
    try:
        # Use environment variables for Spotify credentials
        client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('SPOTIFY_CLIENT_ID'), 
                                                              client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'))
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return sp
    except Exception as e:
        logging.error("Failed to initialize Spotify client: %s", e)
        return None

def load_user_preference_model(model_path):
    try:
        # Load a pre-trained user preference model from disk.
        return joblib.load(model_path)
    except Exception as e:
        logging.error("Failed to load user preference model: %s", e)
        return None

# Additional functions and main method remain unchanged
