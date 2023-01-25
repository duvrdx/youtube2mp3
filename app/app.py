from flask import Flask, flash, request, render_template, redirect, url_for
import webview
from pytube import YouTube
from pytube import Playlist
from module import *

app = Flask(__name__)
window = webview.create_window('youtube2mp3 (or mp4)', app, width=332, height=432, resizable=False, confirm_close=True)

@app.route("/")
def index():
    return redirect(url_for("application"))

@app.route("/app", methods=['GET','POST'])
def application():
    if request.method == "POST":
        values = (request.form["fURL"], request.form["type"], request.form["extension"])

        if values[1] == "v":
            download_video_or_audio(YouTube(values[0]), is_only_audio(values[2]))
        else:
            download_playlist(Playlist(values[0]), is_only_audio(values[2]))
        
    return render_template("index.html")

if __name__ == "__main__":
    #app.run(debug=True)
    webview.start()
    