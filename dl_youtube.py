from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip, ffmpeg_extract_audio
from track_list import tracks
import os


# downloads a yt video as a audio only mp4 file
def download_yt_vid(yt_url, output_folder, output_filename):
    YouTube(yt_url)\
            .streams\
            .filter(file_extension='mp4', only_audio=True)\
            .first()\
            .download(output_path=output_folder, filename=output_filename)


# converts all mp4 files in input folder
def convert_mp4s_in_folder(input_folder, output_folder):
    try:
        os.makedirs(output_folder)
    except OSError:
        print(f'Failed to create folder: {output_folder}')
    else:
        print(f'Successfully created folder: {output_folder}')
    for root, dirs, files in os.walk(input_folder):
        for mp4 in files:
            mp4_path = os.path.join(root, mp4)
            filename = os.path.split(mp4)[1]
            filename = os.path.splitext(filename)[0]
            mp3_path = filename + '.mp3'
            mp3_path = os.path.join(output_folder, mp3_path)
            ffmpeg_extract_audio(mp4_path, mp3_path)    


# splits mp4 into several mp3 files with reference to the tracks.py file
def convert_mp4_mp3(origin, output_folder):
    for track in tracks:
        ffmpeg_extract_subclip(origin, track[1], track[2], targetname=f'{output_folder}/{track[0]}.mp3')    


# clips an individualy mp3 file
def clip_individually(origin, name, start, stop):
    ffmpeg_extract_subclip(origin, start, stop, targetname=f'{name}')    


# download_yt_vid('https://www.youtube.com/watch?v=j1hft9Wjq9U&list=PLcxVmDBWAvdReUSprMH1e59dCHXTIOMKu&index=9', 'output2', 'yorunikakete.mp4')
# convert_mp4_mp3('car_music.mp3', 'output')
# convert_mp4s_in_folder('output2', 'output3')
clip_individually('output3\\yorunikakete.mp3', 'F:\\first_take\\yorunikakete.mp3', 27, 275)