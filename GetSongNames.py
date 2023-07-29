import spotipy, csv
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

title = []
artist = []
album = []

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

for i in range(0, 14):
    results = sp.current_user_saved_tracks(limit=50, offset=50*i)
    for idx, item in enumerate(results['items']):
        track = item['track']

        title.append(track['name'])
        artist.append(track['artists'][0]['name'])
        album.append(track['album']['name'])
    

with open('Songs.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter='`')

    for j in range(0, len(title)):
        row = [title[j], artist[j], album[j]]
        writer.writerow(row)