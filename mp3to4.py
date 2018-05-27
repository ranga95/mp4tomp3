from moviepy.editor import *
import os
mp4=input("Paste the location of the file")
mp4 = mp4.replace( '\\', '\\\\')
mp4=mp4.replace('"','')
if mp4.find(".")==True:

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
else:
    listmp4=os.listdir(mp4)
    print(listmp4)
    for i in listmp4:
        if i.endswith(".mp3"):
            pass
        else:
            dirmp4=mp4 +"\\"+i
            print(  dirmp4  )
            video = VideoFileClip( dirmp4)
            dotnum = dirmp4.rfind( '.' )
            mp3converted = dirmp4[0:dotnum] + '.mp3'
            mp3converted = mp3converted.replace( '\\\\', '\\' )
            print( mp3converted )
            print( "The location of the converted file is in the same location{}".format( mp3converted ) )
            # Make the text. Many more options are available.
            video.audio.write_audiofile( mp3converted )
