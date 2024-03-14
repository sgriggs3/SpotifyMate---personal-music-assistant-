# SpotifyMate

Personalized Music Recommendation System

## Overview

Music recommendation system designed to analyze user music history, preferences and generate personalized playlists. Leveraging the Spotify API, advanced data processing, and machine learning techniques, offers insights into user behavior and trends in music listening. The goal is to enhance the music discovery experience by integrating features such as OpenAI and creating an interactive user interface for prompts.

## Key Components

### Spotify API Integration (`spotify_api_utils.py`)

Spotify Web API to fetch details about tracks, artists, and generate music recommendations. It serves as the backend for accessing Spotify's music library and understanding audio features.

### Data Processing (`data_preprocessing.py`)

Handles the data preprocessing of user data for analysis. This includes normalization, handling missing values, and feature extraction to prepare the dataset for the recommendation model.

### Machine Learning Model (`user_preference_model.py`)

At the base is a machine learning model trained on user data to predict musical preferences. Uses user interaction data and audio features to understand and anticipate user likes and dislikes for tailored recommendations.

### Recommendation Engine (`recommendation_engine.py`)

Uses the preference model to generate personalized music recommendations. It dynamically adjusts based on user preferences to fetch recommendations from Spotify that align with the user's taste.

## Testing Strategy

To ensure the reliability and performance of SpotifyMate, a comprehensive testing strategy is essential. This includes both unit and integration testing to cover individual components and their interactions.

### Unit Testing

- **Environment Variables**: Verify correct loading and usage of Spotify credentials.
- **Spotify Client Initialization**: Ensure the Spotify client is correctly initialized with valid credentials.
- **User Preference Model Loading**: Test loading of the pre-trained model from disk.
- **Recommendation Engine**: Validate the generation of personalized recommendations based on user features.

### Integration Testing

- **End-to-End Workflow**: Test the complete workflow from initializing the Spotify client, loading the user preference model, generating recommendations, and optionally processing user feedback.
- **External Dependencies**: Use mocking to simulate external services like the Spotify API to ensure the system can handle API responses correctly.

### Mocking External Dependencies

For components that interact with external services (e.g., Spotify API), it's crucial to use mocks during testing to simulate responses. This allows for testing the system's behavior under various scenarios without making actual API calls.

## Goals

1. **OpenAI or ChatGPT Integration**: Implement natural language processing capabilities for more engaging user interactions.
2. **User-friendly Chatbot Interface**: Serve as the primary user interaction point for seamless communication and music discovery.
3. **Enhanced Database**: Develop a robust database system for scalability and performance as user data grows.