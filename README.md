# SpotifyMate - Your Personal Music Assistant

## Overview
SpotifyMate is a sophisticated personal music assistant designed to enhance your music listening experience on Spotify. Leveraging advanced machine learning techniques and the Spotify API, SpotifyMate analyzes your music preferences to generate personalized music recommendations.

## Features
- **Personalized Music Recommendations**: Utilizes a pre-trained machine learning model to predict user preferences and suggest songs that match your taste.
- **Spotify API Integration**: Fetches music data directly from Spotify, ensuring up-to-date and relevant recommendations.
- **User Preference Modeling**: Employs a RandomForestClassifier to analyze and predict user music preferences based on historical data.

## Technology Stack
- **Programming Language**: Python
- **Key Libraries**:
  - Spotipy (Spotify API client)
  - Pandas (Data handling)
  - Scikit-learn (Machine Learning)
  - Python-dotenv (Environment and serialization)
  - Joblib (Model serialization)

## Getting Started
1. Clone the repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up your Spotify API credentials in a `.env` file.
4. Run `main.py` to start receiving personalized music recommendations.

## Contribution
Contributions to SpotifyMate are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

## License
SpotifyMate is open-source software licensed under the MIT license.