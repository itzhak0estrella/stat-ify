from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

def obtain_Spotify_auth() -> Spotify:
    ''' Function to obtain Spotify authentication using Spotipy. 
        Returns a Spotify object with the authenticated session. '''
    
    sp_oauth: SpotifyOAuth = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    )
    
    return Spotify(auth_manager=sp_oauth)

def get_all_playlist_tracks(sp: Spotify, playlist_id: str) -> list:
    ''' Helper function that essentially fetches all tracks from a 
        given playlist by making multiple requests if necessary.'''
    
    tracks = []
    limit = 100  # maximum number of items per request
    offset = 0

    print(f"Fetching tracks for given playlist...")
    while True:
        response = sp.playlist_tracks(playlist_id, offset=offset)
        curr_track_batch  = response['items']

        if not curr_track_batch:
            break

        tracks.extend(curr_track_batch)
        offset += limit # update offset for next batch

    return tracks

def get_only_hundred_tracks(sp: Spotify, playlist_id: str) -> list:
    ''' TEST function that fetches only the first 100 tracks from a 
        given playlist. Useful for quick analysis or display.'''
    
    response = sp.playlist_tracks(playlist_id, limit=100)
    return response['items']

if __name__ == "__main__":
    sp: Spotify = obtain_Spotify_auth()
    print("✅ Successfully authenticated with Spotify API.\n")
    
    # obtain user's playlists and display them with corresponding IDs
    print("🔍 Fetching your Spotify playlists...")
    playlist: dict = sp.current_user_playlists() 
    print("Available playlists:")
    for item in playlist['items']:
        print(f"- {item['name']} (ID: {item['id']})")

    main_playlist_id: str = str(input("\nEnter the ID of the playlist you want to analyze: "))

    main_tracks: list = get_all_playlist_tracks(sp, main_playlist_id)
    print(type(main_tracks))
    print("Size of the playlist:", len(main_tracks))
    
    # for item in main_tracks['items']:
    #     track = item['track']
    #     track_name = track['name']
    #     artists = track['artists']

    #     if not artists:
    #         continue

    #     # Get first artist (usually primary)
    #     artist = artists[0]
    #     artist_name = artist['name']
    #     artist_id = artist['id']

    #     # Get genres from artist profile
    #     artist_info = sp.artist(artist_id)
    #     genres = artist_info.get('genres', [])

    #     print(f"- {track_name} by {artist_name}")
    #     print(f"  Genres: {', '.join(genres) if genres else 'N/A'}")
                                                
