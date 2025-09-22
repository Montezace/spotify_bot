import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

# Function to create and return a Spotify client using Spotipy
def get_client():
    # Authenticate with Spotify using client credentials
    auth_manager = SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    )
    return spotipy.Spotify(auth_manager=auth_manager)

# Function to get the track name and artist from a Spotify URL
def get_track_name(url):
    sp = get_client()  # Get the authenticated Spotify client
    if 'track' in url:  # Check if the URL is a track URL
        track = sp.track(url)  # Fetch track details from Spotify
        # Return the track name and the first artist's name
        return f"{track['name']} {track['artists'][0]['name']}"
    return None  # Return None if the URL does not contain a track
