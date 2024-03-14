# feedback_processor.py
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FeedbackProcessor:
    def __init__(self, user_preferences_db):
        """
        Initializes the FeedbackProcessor with a reference to a database or storage
        system where user preferences are stored.
        
        Parameters:
        - user_preferences_db: A reference to the database or storage system containing
                               user preferences and feedback.
        """
        self.user_preferences_db = user_preferences_db

    def process_feedback(self, user_id, track_id, feedback_type):
        """
        Processes feedback from a user for a specific track.

        Parameters:
        - user_id: The ID of the user providing the feedback.
        - track_id: The ID of the track for which feedback is provided.
        - feedback_type: The type of feedback (e.g., 'like', 'dislike').
        """
        try:
            if feedback_type == 'like':
                self.add_like(user_id, track_id)
            elif feedback_type == 'dislike':
                self.add_dislike(user_id, track_id)
            else:
                raise ValueError(f"Unknown feedback type: {feedback_type}")
        except Exception as e:
            logging.error(f"Error processing feedback: {e}")

    def add_like(self, user_id, track_id):
        """
        Updates the user's preferences to reflect a 'like' for a specific track.

        Parameters:
        - user_id: The ID of the user.
        - track_id: The ID of the track.
        """
        try:
            # Implementation for adding a 'like' to the user's preferences
            logging.info(f"User {user_id} liked track {track_id}")
            # Actual database interaction code to add a 'like'
            self.user_preferences_db.add_user_like(user_id, track_id)
        except Exception as e:
            logging.error(f"Error adding like for user {user_id} on track {track_id}: {e}")

    def add_dislike(self, user_id, track_id):
        """
        Updates the user's preferences to reflect a 'dislike' for a specific track.

        Parameters:
        - user_id: The ID of the user.
        - track_id: The ID of the track.
        """
        try:
            # Implementation for adding a 'dislike' to the user's preferences
            logging.info(f"User {user_id} disliked track {track_id}")
            # Actual database interaction code to add a 'dislike'
            self.user_preferences_db.add_user_dislike(user_id, track_id)
        except Exception as e:
            logging.error(f"Error adding dislike for user {user_id} on track {track_id}: {e}")
