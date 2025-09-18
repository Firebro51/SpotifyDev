# Spotify Playlist Generator

Automatically generates themed playlists from your Spotify liked songs using audio feature analysis. Built with Python and the Spotify Web API, this tool analyzes the musical characteristics of your saved tracks and creates custom playlists based on configurable audio features like energy, danceability, valence, and instrumentalness.

## Features

- Analyzes all your saved tracks using Spotify's audio features
- Creates custom playlists based on configurable themes
- Automatically adds matching songs to new playlists in your account
- Supports any combination of audio characteristics (energy, mood, tempo, etc.)

## How It Works

Fetches all your Spotify liked songs and retrieves their audio features through the Spotify API. Each track gets analyzed for characteristics like energy level, danceability, valence (positivity), tempo, and instrumentalness. Based on your configured filtering criteria, matching tracks are automatically added to a new themed playlist in your account.

<img width="4743" height="2692" alt="Generated Running Playlist" src="https://github.com/user-attachments/assets/434da9d1-9cf2-4dae-9fc7-9790d4a05a4e" />
<sub><i>Example: 148-song running playlist automatically generated from liked songs library</i></sub>


## Customization

Edit the code to create different themed playlists:
- **Instrumental**: `instrumentalness > 0.5`
- **High Energy**: `energy > 0.7 and danceability > 0.6`
- **Chill/Study**: `energy < 0.4 and valence < 0.5`
- **Happy/Upbeat**: `valence > 0.7 and energy > 0.5`
- **Workout**: `energy > 0.8 and tempo > 120`

Change playlist name, combine multiple features, or adjust thresholds for any mood or theme.
