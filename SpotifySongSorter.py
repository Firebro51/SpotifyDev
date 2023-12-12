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

def search_tracks(sp, keyword):
    results = sp.search(q=keyword, limit=50, type='track')
    tracks = results['tracks']['items']
    return [track['id'] for track in tracks]

def create_playlist(sp, name):
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user_id, name)
    return playlist['id']

def add_tracks_to_playlist(sp, playlist_id, track_ids):
    # Add tracks to the playlist in batches of 100
    for i in range(0, len(track_ids), 100):
        batch = track_ids[i:i + 100]
        sp.playlist_add_items(playlist_id, batch)

def main(keyword):
    sp = authenticate_spotify()
    track_ids = search_tracks(sp, keyword)

    playlist_id = create_playlist(sp, f'{keyword} Playlist')
    add_tracks_to_playlist(sp, playlist_id, track_ids)

if __name__ == '__main__':
    keyword = "Love"  # keyword for song
    main(keyword)