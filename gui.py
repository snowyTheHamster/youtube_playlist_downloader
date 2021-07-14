import download_yt_playlist
import download_yt_playlist_audio_only
import PySimpleGUI as sg
import traceback
import os


sg.theme('Dark Blue 3')

layout = [
        [sg.Text('Youtube Playlist URL:')],
        [sg.InputText('https://www.youtube.com/playlist?list=PLcxVmDBWAvdRMszkkbF7oLQojlbunO3ea', key='_PLAYLIST_URL_', size=(80,1))],
        [sg.Text('')],
        [sg.Text('Select Save Folder:')],
        [sg.Input(key='_SAVE_DIR_'), sg.FolderBrowse()],
        [sg.Text('')],
        [sg.Text('Download Video or audio:'), sg.Radio('Video', "_RADIO_MODE_", default=True, key='Radio_video'), sg.Radio('Audio', "_RADIO_MODE_", key='Radio_audio')],
        [sg.Text('')],
        [sg.Text('Video Quality'), sg.Radio('Low (progressive)', "_QUALITY_", default=True, key='Radio_low'), sg.Radio('Highest (Adaptive + ffmpeg merging)', "_QUALITY_", key='Radio_high')],
        [sg.Button("Process", size=(10, 1), bind_return_key=True, key='_PROCESS_')],
	    [sg.Output(size=(80, 20))],
    ]

window = sg.Window('Youtube Playlist Downloader', layout)

try:
    while True:
        event, values = window.read()
        if event is None:
            break
        if event == '_PROCESS_':
            playlist_url = values['_PLAYLIST_URL_']
            save_dir = values['_SAVE_DIR_']

            if playlist_url == '':
                print('please input the url for the youtube playlist')
            elif save_dir == '':
                print('please specify an empty folder to save the files')
            elif os.listdir(save_dir) :
                print('The Save Folder must be Empty')
            elif values['Radio_video'] == True:
                if values['Radio_high'] == True:
                    print('Adaptive videos - Highest Quality')
                    download_yt_playlist.dl_yt_videos_high(playlist_url, save_dir)
                elif values['Radio_low'] == True:
                    print('Progressive videos - Lower Quality')
                    download_yt_playlist.dl_yt_videos_low(playlist_url, save_dir)
            elif values['Radio_audio'] == True:
                print('save as audio files')
                download_yt_playlist_audio_only.dl_yt_audios(playlist_url, save_dir)

    window.close()

except Exception as e:
    tb = traceback.format_exc()
    sg.Print(f'An error happened.  Here is the info:', e, tb)
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)