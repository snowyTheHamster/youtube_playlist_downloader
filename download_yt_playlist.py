# since youtubes progressive videos (video + audio) has capped resolution of 720p
# we'll download the adaptive video (high quality but no sound) + audio only file separately & merge them aftewards with ffmpeg.

from pytube import Playlist
import ffmpeg
import os
import shutil

def dl_yt_videos_low(playlist_url, save_dir):

    pl = Playlist(playlist_url)
    for yt in pl.videos:
        stream = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first() # gets the highest quality out of progressive videos (vid+audio)
        print(stream) # print result of stream
        stream.download(save_dir) # folder to download

    print('done downloading files from the playlist')



# extra work to get highest quality video (must also install ffmpeg on workstation)
def dl_yt_videos_high(playlist_url, save_dir):

    pl = Playlist(playlist_url)

    # create a temp directory to store temp audio and video file
    temp_dir = os.path.join(save_dir, 'tempdir')

    for yt in pl.videos:

        # delete temp folder, then create it to keep it empty
        try:
            shutil.rmtree(temp_dir, ignore_errors=True)
            os.mkdir(temp_dir)
        except:
            print('temp directory already exists')

        # get audio only
        video = yt.streams.filter(only_audio=True).first()
        print(f'file audio only: {video}')
        out_file = video.download(output_path=temp_dir)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)


        # get highest quality video (no sound)        
        stream_noaudio = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first()
        print(f'file without audio: {stream_noaudio}')
        stream_noaudio.download(temp_dir)


        for root, dirs, files in os.walk(temp_dir):
            for filename in files:
                if filename.endswith('.mp3'):
                    audiofile = os.path.join(root, filename) # fullpath of temp audiofile
                if filename.endswith('.mp4'):
                    videofile = os.path.join(root, filename) # fullpath of temp videofile
                    final_videofile = os.path.join(save_dir, filename) # fullpath to final videofile in save directory
                    print(f'print savedir here: {save_dir}')
                    print(f'print filename here: {filename}')
                    print(f'print finalpath here: {final_videofile}')


        # merge the audio and video file
        input_video = ffmpeg.input(videofile)
        input_audio = ffmpeg.input(audiofile)
        ffmpeg.concat(input_video, input_audio, v=1, a=1).output(final_videofile).run()


        # delete temp folder to reset process
        try:
            shutil.rmtree(temp_dir, ignore_errors=True)
        except:
            print('failed the delete the temp directory')


    print('done downloading files from the playlist')