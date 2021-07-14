from pytube import Playlist


def dl_yt_videos(playlist_url, save_dir):

    pl = Playlist(playlist_url)
    for yt in pl.videos:
        stream = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first() # gets the highest quality video
        print(stream) # print result of stream
        stream.download(save_dir) # folder to download

    print('done downloading files from the playlist')