import pytube

v_list = [
"'https://youtu.be/hgIDXTmmgDg'",
]

download_location = r'C:\Users\USER\Desktop\python\suv'
for video_url in v_list :
    yt = pytube.YouTube(video_url)
    print('開始下載')
    print(type(yt.streams.filter(res="720p")))
    stream = yt.streams.filter(res="720p").first()
    print(stream)
    stream.download(download_location)
    print('下載完成!!')
