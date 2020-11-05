# importing YouTube from pytube
from pytube import YouTube
# asking user to enter link
link = input("https://www.youtube.com/watch?v=Urdlvw0SSEc&list=RDUrdlvw0SSEc&start_radio=1")
# showing user that the process has started
print("Downloding...")
# main code to download Video
YouTube(link).streams.first().download()
# showing user that the video has downloaded
print("Video downloaded successfully")