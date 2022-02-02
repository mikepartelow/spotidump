# Dump Spotify Playlists to JSON

### Build

    docker build -t spotidump .

### Configure

1. Get Spotify [Developer credentials](https://developer.spotify.com/dashboard/login)
2. Create a [dumpus.json](dumpus.json.example)

### Run

    docker run -v `pwd`/app:/spotidump -ti spotidump bash
    python ./dumpus.py
