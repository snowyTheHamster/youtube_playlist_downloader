# youtube_playlist_downloader

### what it does

A gui script that downloads a youtube playlist as:

+ mp3 audio.
+ Lower quality progressive videos (fast).
+ Highest quality Adaptive videos (slow) - merges audio afterwards with ffmpeg.

You need ffmpeg installed on your workstation to download the Video in Highest Quality.

```
git clone https://github.com/snowyTheHamster/youtube_playlist_downloader.git .
python -m venv .venv
. .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

python gui.py
```

Install ffmpeg if needed.

### how to use

- create a public or unlisted youtube playlist.
- run the python gui.py file.
- paste in the youtube playlist url in field.
- select empty folder to save files.
- select whether to save files as video or audio files.
- video only: select whether to save video in low or high quality.
- click process.