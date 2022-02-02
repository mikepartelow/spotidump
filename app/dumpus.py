import json
import tekore as tk

if __name__ == "__main__":
    with open('dumpus.json') as f:
        conf = json.load(f)

    client_id, client_secret, playlist_ids = conf['client_id'], conf['client_secret'], conf['playlist_ids']

    token = tk.request_client_token(client_id, client_secret)

    spotify = tk.Spotify(token)

    for playlist_id in playlist_ids:
        name = spotify.playlist(playlist_id).name
        simple_path = f"{name}.{playlist_id}.simple.json"
        raw_path = f"{name}.{playlist_id}.raw.json"

        with open(simple_path, "w") as simple_f, open(raw_path, "w") as raw_f:
            simple_f.write("[")
            raw_f.write("[")
            for idx, track in enumerate(spotify.all_items(spotify.playlist_items(playlist_id, market='US'))):
                if idx > 0:
                    simple_f.write(',')
                    raw_f.write(',')

                track_d=dict(
                    name=track.track.name,
                    artists=[a.name for a in track.track.artists],
                    album_name=track.track.album.name,
                    is_local=track.track.is_local,
                    is_playable=(hasattr(track.track, 'is_playable') and track.track.is_playable),
                )

                # print(repr(track_d))
                simple_f.write(json.dumps(track_d))
                raw_f.write(track.json())

            simple_f.write("]")
            raw_f.write("]")
