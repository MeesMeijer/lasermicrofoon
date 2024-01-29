from pytube import YouTube
import os
from pathlib import Path


def youtube2mp3 (url):
    # url input from user
    yt = YouTube(url)
    # print(yt.streams)
    ##@ Extract audio with 160kbps quality from video
    video = yt.streams.filter(abr='128kbps').last()

    ##@ Downloadthe file
    out_file = video.download(output_path="./test2")
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    os.rename(out_file, new_file)
    ##@ Check success of download
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
    else:
        print(f'ERROR: {yt.title}could not be downloaded!')

youtube2mp3("https://www.youtube.com/watch?v=dFfC92iBxNw")

