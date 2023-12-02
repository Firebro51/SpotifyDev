import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

def authenticate_spotify():
    auth_manager = SpotifyOAuth(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
        scope='user-library-read playlist-modify-public'
    )
    return spotipy.Spotify(auth_manager=auth_manager)

def fetch_users_liked_songs(sp):
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return [track['track']['id'] for track in tracks]

def filter_instrumental_tracks(sp, track_ids):
    instrumental_tracks = []
    # Process in batches of 100 tracks
    for i in range(0, len(track_ids), 100):
        batch = track_ids[i:i + 100]
        features_list = sp.audio_features(batch)
        for features in features_list:
            if features and features['instrumentalness'] > 0.5:
                instrumental_tracks.append(features['id'])
    return instrumental_tracks


def create_playlist(sp, name):
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user_id, name)
    return playlist['id']

def add_tracks_to_playlist(sp, playlist_id, track_ids):
    # Add tracks to the playlist in batches of 100
    for i in range(0, len(track_ids), 100):
        batch = track_ids[i:i + 100]
        sp.playlist_add_items(playlist_id, batch)


def main():
    sp = authenticate_spotify()
    liked_songs = fetch_users_liked_songs(sp)
    instrumental_tracks = filter_instrumental_tracks(sp, liked_songs)

    playlist_id = create_playlist(sp, 'Instrumental Liked Songs')
    add_tracks_to_playlist(sp, playlist_id, instrumental_tracks)

if __name__ == '__main__':
    main()
