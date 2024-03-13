# recommendation_engine.py

from utils.spotify_api_utils import get_recommendations_based_on_seeds

class RecommendationEngine:
    def __init__(self, user_preference_model, sp):
        self.user_preference_model = user_preference_model
        self.sp = sp

    def generate_personalized_recommendations(self, user_features):
        predicted_preferences = self.user_preference_model.predict(user_features)
        seed_genres, target_attributes = self._convert_preferences_to_query_params(predicted_preferences)
        recommendations = get_recommendations_based_on_seeds(seed_genres, target_attributes, self.sp)
        return recommendations

    def _convert_preferences_to_query_params(self, predicted_preferences):
        seed_genres = ['rock', 'pop']  # Dynamic conversion based on model output
        target_attributes = {'energy': 0.7, 'danceability': 0.5}
        # Implement logic to dynamically adjust genres and attributes based on preferences
        return seed_genres, target_attributes
