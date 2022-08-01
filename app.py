from pytube import YouTube
from pytube import Playlist
from module import *

if __name__ == "__main__":
    window = create_window()
    window_closed = False

    while not(window_closed):
        event, values = window.read()

        if event == "Baixar" and values["link"] != "":
            if values["v"]:
                try:
                    download_video_or_audio(window, YouTube(values["link"]), is_only_audio(values))
                except:
                    change_label_text(window, "status", "Vídeo inválido ou Inexistente")
            if values["p"]:
                try:
                    download_video_or_audio(window, Playlist(values["link"]), is_only_audio(values))
                except:
                    change_label_text(window, "status", "Vídeo inválido ou Inexistente")
        else:
            window.find_element("status").update(value="Insira um link válido!")
        
        window_closed = is_window_closed(event)
        
