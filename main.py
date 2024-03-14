import os
import joblib
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils.recommendation_engine import RecommendationEngine
from utils.feedback_processor import FeedbackProcessor
from user_preference_model import UserPreferenceModel

# Load environment variables from .env file
load_dotenv()

def initialize_spotify_client():
    # Use environment variables for Spotify credentials
    try:
        client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('SPOTIFY_CLIENT_ID'), 
                                                              client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'))
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return sp
    except Exception as e:
        print(f"Error initializing Spotify client: {e}")
        return None

def load_user_preference_model(model_path):
    # Load a pre-trained user preference model from disk.
    try:
        user_preference_model = joblib.load(model_path)
        return user_preference_model
    except Exception as e:
        print(f"Error loading user preference model: {e}")
        return None

def get_user_features():
    # Fetch user features for recommendation. Adjust based on actual implementation.
    # Note: This is a placeholder function. In a real-world application, user features should be dynamically retrieved.
    user_features = {"feature1": 0.5, "feature2": 0.3}
    return user_features

def main():
    # Check for required environment variables
    required_env_vars = ['SPOTIFY_CLIENT_ID', 'SPOTIFY_CLIENT_SECRET', 'USER_PREFERENCE_MODEL_PATH', 'USER_PREFERENCES_DB_PATH']
    missing_env_vars = [var for var in required_env_vars if not os.getenv(var)]
    if missing_env_vars:
        print(f"Missing required environment variables: {', '.join(missing_env_vars)}")
        return

    # Initialize Spotify client
    sp = initialize_spotify_client()
    if not sp:
        return

    # Load the pre-trained User Preference Model
    user_preference_model = load_user_preference_model(os.getenv('USER_PREFERENCE_MODEL_PATH'))
    if not user_preference_model:
        return

    # Instantiate the RecommendationEngine with the model and Spotify client
    recommendation_engine = RecommendationEngine(user_preference_model, sp)

    # Initialize the FeedbackProcessor with the user preferences database path
    feedback_processor = FeedbackProcessor(user_preferences_db=os.getenv('USER_PREFERENCES_DB_PATH'))

    # Fetch user features
    user_features = get_user_features()

    # Generate personalized recommendations
    personalized_recommendations = recommendation_engine.generate_personalized_recommendations(user_features)

    # Example feedback data (for demonstration purposes)
    feedback_data = {'user_id': '123', 'track_id': 'abc', 'feedback_type': 'like'}
    feedback_processor.process_feedback(**feedback_data)

    # Output recommendations
    print("Recommended Track IDs:", personalized_recommendations)

if __name__ == '__main__':
    main()