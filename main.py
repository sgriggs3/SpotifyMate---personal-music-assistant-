import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import joblib  # For loading a pre-trained model

# Correcting the import paths based on the actual project structure
from spotify_api_utils import sp, fetch_track_details
from recommendation_engine import RecommendationEngine
from feedback_processor import FeedbackProcessor
from user_preference_model import UserPreferenceModel

# Load environment variables from .env file
load_dotenv()

def initialize_spotify_client():
    # Use environment variables for Spotify credentials
    client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('SPOTIFY_CLIENT_ID'), 
                                                          client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'))
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

def load_user_preference_model(model_path):
    # Load a pre-trained user preference model from disk.
    return joblib.load(model_path)

def get_user_features():
    # Fetch user features for recommendation. Adjust based on actual implementation.
    user_features = {"feature1": 0.5, "feature2": 0.3}
    return user_features

def main():
    # Initialize Spotify client
    sp = initialize_spotify_client()

    # Load the pre-trained User Preference Model
    user_preference_model = load_user_preference_model("/path/to/your/model.joblib")

    # Instantiate the RecommendationEngine with the model and Spotify client
    recommendation_engine = RecommendationEngine(user_preference_model, sp)

    # (Optional) Initialize the FeedbackProcessor if feedback processing is integrated
    feedback_processor = FeedbackProcessor(user_preferences_db="path/to/your/database")

    # Fetch user features
    user_features = get_user_features()

    # Generate personalized recommendations
    personalized_recommendations = recommendation_engine.generate_personalized_recommendations(user_features)

    # Process user feedback if applicable (demonstration purpose, adjust based on implementation)
    # feedback_processor.process_feedback(feedback_data)

    # Output recommendations
    print("Recommended Track IDs:", personalized_recommendations)

if __name__ == '__main__':
    main()