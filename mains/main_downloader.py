# -*- coding: utf-8 -*-
"""
https://steam.oxxostudio.tw/category/python/example/youtube-download.html#a4
https://steam.oxxostudio.tw/category/python/example/youtube-list-download.html
"""
import os
from pytube import YouTube
from pydub import AudioSegment
from glob import glob


# TODO: params
date = '2023-10-24'
lst = [
    'https://www.youtube.com/watch?v=LCA7N5mHmI8',
    # 'https://www.youtube.com/watch?v=p59Ri1YVcS0',
    'https://www.youtube.com/watch?v=tH-4cGbkOL8',
    'https://www.youtube.com/watch?v=w0QskMLW-UU',
]
format = 'wav'
basic_path = f'{os.getcwd()}/data/mini-ielts/listening/{date}'
print(f'basic_path: {basic_path}')
os.system(f'mkdir -p {basic_path}')  # create dir
os.chdir(f'{basic_path}')  # cd


def downloader(input_url, fmt='mp3'):
    yt = YouTube(f'{input_url}')
    print(f'title: {yt.title}')
    print(f'length: {yt.length} (sec)')  # length in seconds
    # print(f'author: {yt.author}')
    # print(f'channel_url: {yt.channel_url}')  # 影片作者頻道網址
    # print(f'thumbnail_url: {yt.thumbnail_url}')  # 影片縮圖網址
    # print(f'views: {yt.views}')

    print('downloading...')
    yt.streams.filter().get_audio_only().download(filename=f'{yt.title}.{fmt}')
    # save as mp3
    print(f'{yt.title} ok!')


for file in lst:
    downloader(input_url=file, fmt=format)
print(f'Downloading tasks are done successfully!')

"""
google: python merge multiple mp3 files
[Python library to split and join mp3 files](https://stackoverflow.com/questions/2952309/python-library-to-split-and-join-mp3-files)

google: pydub merge audio
[Combine audio files in Python](https://stackoverflow.com/questions/61499350/combine-audio-files-in-python)
"""
two_sec_silence = AudioSegment.silent(duration=2*1000)  # pydub does things in milliseconds
playlist_songs = [AudioSegment.from_file(audio_file) for audio_file in glob(f"{basic_path}/*.{format}")]
print(f'playlist_songs: {playlist_songs}')
merged_sound = two_sec_silence
for song in playlist_songs:
    merged_sound = merged_sound + song

# export
merged_sound.export(f"{basic_path}/{date}-merged.{format}", format=f"{format}")
print(f'Merging tasks are done successfully!')

print(f'All tasks are done successfully!')
"""

python mains/main_downloader.py
"""