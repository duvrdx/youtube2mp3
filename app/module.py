import os
from moviepy.video.io.VideoFileClip import AudioFileClip
import pytube
from pytube import YouTube

def is_only_audio(value):
    return value[-1] == "3"

def delete_files(path):
    for file in (os.listdir(path)):
        if file[-1] == '4':
            os.remove(f"{path}/{file}")

def mp4_to_mp3(filename):
    clip = AudioFileClip(filename)
    clip.write_audiofile(filename[:-4] + ".mp3")
    clip.close()

def download_video_or_audio(video_link, only_audio):
    if only_audio:
        mp4_to_mp3(video_link.streams.get_audio_only().download(output_path="./audio"))
        delete_files("audio")
    else:
        video_link.streams.get_highest_resolution().download(output_path="./video")

def download_playlist(playlist_link, only_audio):
    for url in playlist_link.video_urls:
        try:
            video_link = YouTube(url)
        except pytube.exceptions.VideoUnavailable:
            print(f'\nVideo {url} is unavaialable, skipping.')
        else:
            download_video_or_audio(video_link, only_audio)
            print(f"Download Concluido: {video_link.title}'")

