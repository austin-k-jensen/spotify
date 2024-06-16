import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

client_credentials_mgmt = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_mgmt)

taylor_uri = "spotify:artist:06HL4z0CvFAxyc27GXpf02"

results = sp.artist_albums(taylor_uri, album_type="album")
albums = results["items"]
while results["next"]:
    results = sp.next(results)
    albums.extend(results["items"])

for album in albums:
    print(
        f"""Album: {album["name"]}
    Track count: {album["total_tracks"]}
    Release date: {album["release_date"]}
    URI: {album["uri"]}"""
    )

    tracks = sp.album_tracks(album["uri"])["items"]
    for track in tracks:
        print(
            f"""
    Track: {track["name"]}
        Track number: {track["track_number"]}
        URI: {track["uri"]}"""
        )

        track_data = sp.track(track["uri"])
        print(track_data)

    quit()
