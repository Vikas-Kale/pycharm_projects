# How to print without using print function in python.
# import sys
# sys.stdout.write("Hello World!")
#
# import pytube
# from pytube import YouTube
#
# link=input("Enter URL of video: ")
# video=YouTube(link)
# stream=video.streams.get_highest_resolution()
# stream.download()

def counter():
    i = 2
    while (i <= 10):
        yield i
        i += 1

print(counter())



