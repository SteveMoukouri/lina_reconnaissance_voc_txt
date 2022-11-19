import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import config

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = config.APP_CLIENT_ID,
                                                           client_secret = config.APP_CLIENT_SECRET))


name    = 'sch'
q       = f'"{name}" genre:"french hip hop"'
results = spotify.search(q, type='artist', market="FR")

pprint(results['artists']['items'])
