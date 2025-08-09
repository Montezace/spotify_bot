import spotipy
from spotipy .oauth2 import SpotifyClientCredentials
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def get_client():
    auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
    return spotipy.Spotify(auth_manager=auth_manager)

def get_track_name(url):
    sp = get_client()
    if 'track' in url:
        track = sp.track(url)
        return f"{track['name']} {track['artists'][0]['name']}"
    return None

