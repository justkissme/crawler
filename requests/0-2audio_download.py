import requests
url='https://static.pandateacher.com/Over%20The%20Rainbow.mp3'

res=requests.get(url)
audio=res.content
music=open('Wind_crawler\\requests\\0-2audio_download.mp3','wb')
music.write(audio)
music.close()