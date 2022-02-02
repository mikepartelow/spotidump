FROM python:3.10
RUN apt update -yq && \
    apt install less && \
    pip install tekore apple-music-python

COPY app/ /spotidump

WORKDIR /spotidump

CMD python ./dumpus.py