import logging

# Assuming other necessary imports and parts of the file are already present

def _convert_preferences_to_query_params(preferences):
    """
    Convert predicted preferences to query parameters for the recommendation API.
    """
    query_params = {}
    for key, value in preferences.items():
        if isinstance(value, list):
            # Convert list to comma-separated string
            query_params[key] = ','.join(map(str, value))
        elif isinstance(value, bool):
            # Convert boolean to lowercase string
            query_params[key] = str(value).lower()
        elif value is not None:
            query_params[key] = str(value)
        else:
            raise ValueError(f"Invalid preference value for key '{key}': None is not allowed")
    return query_params

def generate_personalized_recommendations(user_id):
    """
    Generate personalized recommendations for a user based on their preferences.
    """
    try:
        # Assuming there is a function get_user_preferences that retrieves user preferences
        preferences = get_user_preferences(user_id)
        
        # Validate preferences
        if not preferences:
            raise ValueError(f"No preferences found for user {user_id}")
        
        # Convert preferences to query parameters
        query_params = _convert_preferences_to_query_params(preferences)
        
        # Assuming there is a function call_recommendation_api that takes query parameters
        recommendations = call_recommendation_api(query_params)
        
        return recommendations
    except ValueError as ve:
        logging.error(f"Value error while generating recommendations for user {user_id}: {ve}")
        return []
    except Exception as e:
        logging.error(f"Failed to generate personalized recommendations for user {user_id}: {e}")
        # Depending on the requirements, we could return an empty list, a default set of recommendations, or re-raise the exception
        return []

# Other parts of the file remain unchanged