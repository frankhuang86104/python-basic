import pytube   

video_url = r"https://youtu.be/B9iQHLLdkUY?si=uflmlNM6BNLT2616"
yt = pytube.YouTube(video_url)
video_list = yt.streams
print(video_list)

