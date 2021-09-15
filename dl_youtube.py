from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from track_list import tracks


def download_yt_vid():
    YouTube('https://www.youtube.com/watch?v=OenNkC8kVNY&list=PLcxVmDBWAvdSYujyAAYFnTiXUtksc9CHL&index=14')\
            .streams\
            .filter(file_extension='mp4', only_audio=True)\
            .first()\
            .download(output_path='out_directory', filename='out_filename')


def convert_mp4_mp3(origin, output_folder):
    for track in tracks:
        ffmpeg_extract_subclip(origin, track[1], track[2], targetname=f'{output_folder}/{track[0]}.mp3')    

def clip_individually(origin, name, start, stop):
    ffmpeg_extract_subclip(origin, start, stop, targetname=f'{name}.mp3')    


# download_yt_vid()
# convert_mp4_mp3('car_music.mp3', 'output')
clip_individually('F:\\unravel.mp3', './unravel', 0, 195)

