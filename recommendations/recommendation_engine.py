# recommendation_engine.py

from utils.spotify_api_utils import get_recommendations_based_on_seeds

class RecommendationEngine:
    def __init__(self, user_preference_model, sp):
        """
        Initializes the RecommendationEngine.
        
        Parameters:
        - user_preference_model: A pre-trained model for predicting user music preferences.
        - sp: An authenticated Spotify client.
        """
        self.user_preference_model = user_preference_model
        self.sp = sp

    def generate_personalized_recommendations(self, user_features):
        """
        Generates personalized music recommendations based on user features.
        
        Parameters:
        - user_features: A dictionary of user features.
        
        Returns:
        A list of recommended track IDs.
        """
        try:
            predicted_preferences = self.user_preference_model.predict(user_features)
            seed_genres, target_attributes = self._convert_preferences_to_query_params(predicted_preferences)
            recommendations = get_recommendations_based_on_seeds(seed_genres, target_attributes, self.sp)
            return recommendations
        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return []

    def _convert_preferences_to_query_params(self, predicted_preferences):
        """
        Converts predicted preferences into query parameters for the Spotify recommendation API.
        
        Parameters:
        - predicted_preferences: The output from the user preference model.
        
        Returns:
        A tuple containing a list of seed genres and a dictionary of target attributes.
        """
        # TODO: Implement logic to dynamically adjust genres and attributes based on preferences
        # This should involve analyzing the predicted_preferences to extract meaningful genres and attributes
        seed_genres = ['rock', 'pop']  # Example static values, to be replaced
        target_attributes = {'energy': 0.7, 'danceability': 0.5}  # Example static values, to be replaced
        return seed_genres, target_attributes
