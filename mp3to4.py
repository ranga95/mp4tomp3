from moviepy.editor import *
mp4=input("Paste the location of the file")
mp4 = mp4.replace( '\\', '\\\\')
mp4=mp4.replace('"','')
print(mp4)
print(type(mp4))
print(mp4)
video= VideoFileClip(mp4)
dotnum=mp4.rfind('.')
mp3converted=mp4[0:dotnum]+'.mp3'
mp3converted = mp3converted.replace( '\\\\', '\\')
print(mp3converted)
print("The location of the converted file is in the same location{}".format(mp3converted))
# Make the text. Many more options are available.
video.audio.write_audiofile(mp3converted)
