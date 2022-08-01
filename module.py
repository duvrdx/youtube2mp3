import os
from PySimpleGUI import PySimpleGUI as sg
from moviepy.video.io.VideoFileClip import AudioFileClip
import pytube
from pytube import YouTube

def create_window():
    sg.theme("Reddit")

    layout = [
        [sg.Radio('Vídeo',"RAD01", key="v"),sg.Radio('Playlist',"RAD01", key="p")],
        [sg.Text('Link'), sg.Input(key='link')],[sg.Radio('MP3', "RAD02", key='m3'),
        sg.Radio('MP4',"RAD02", key='m4')],[sg.Button('Baixar')],
        [sg.Text('', key='status')]
    ]

    return sg.Window("Youtube2mp3", layout)

def is_window_closed(event):
    return event == sg.WINDOW_CLOSED

def is_only_audio(values):
    if values["m4"]:
        return False
    else:
        return True

def delete_files(path):
    for file in (os.listdir(path)):
        if file[-1] == '4':
            os.remove(f"{path}/{file}")

def mp4_to_mp3(filename):
    clip = AudioFileClip(filename)
    clip.write_audiofile(filename[:-4] + ".mp3")
    clip.close()

def change_label_text(window, element, text):
    window.find_element(element).Update(value = text)

def download_video_or_audio(window, video_link, only_audio):
    change_label_text(window, "status", "Seu ")
    window.find_element("status").Update(value = f"Baixando: {video_link.title}")

    if only_audio:
        mp4_to_mp3(video_link.streams.get_audio_only().download(output_path="./audio"))
        delete_files("audio")
    else:
        video_link.streams.get_highest_resolution().download(output_path="./video")
    
    window.find_element("status").Update(value = (f"Download concluido: {video_link.title}"))

def download_playlist(window, playlist_link, only_audio):

    print(f'\nDownloading: {playlist_link.title}')
    window.find_element('status').Update(value=(f'\nDownloading: {playlist_link.title}'))
    for url in playlist_link.video_urls:
        try:
            video_link = YouTube(url)
        except pytube.exceptions.VideoUnavailable:
            window.find_element('status').Update(value=(f'\nVideo {url} is unavaialable, skipping.'))
        else:
            download_video_or_audio(window, video_link, only_audio)
            window.find_element('status').update(value=f"Download Concluido: {video_link.title}'")

