from pytube import Playlist
import os


def dl_yt_audios(playlist_url, save_dir):

    pl = Playlist(playlist_url)
    for yt in pl.videos:
    
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
        print(video)
    
        # download the file
        out_file = video.download(output_path=save_dir)
    
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    
        # result of success
        print(yt.title + " has been successfully downloaded.")

    print('done downloading files from the playlist')