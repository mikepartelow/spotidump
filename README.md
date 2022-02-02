# Dump Spotify Playlists to JSON

### Build

    docker build -t spotidump .

### Run

    docker run -v `pwd`/app:/spotidump -ti spotidump bash
    python ./dumpus.py
