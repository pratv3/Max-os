# application of all are here
if __name__=="__main__":
    print("00F*0100B failed to load os")
    print("invalid magical number you need to load the kernel first")
if __name__!='__main__':
    import os
    from pygame import mixer
    import wikipedia
    from tkinter import *
    import time
    import turtle as t
    def music ():
        print("mus 0.32.0 Copyright © 2005-2020")
        print("built on UNKNOWN")
        print("ffmpeg library versions:")
        print("libavutil       56.51.100")
        print("libavcodec      58.91.100")
        print("libavformat     58.45.100")
        print("libswscale      5.7.100")
        print("libavfilter     7.85.100")
        print("libswresample   3.7.100")
        print("ffmpeg version: 4.3.2-0+deb11u1")
        mdir="F:\\"
        songs=os.listdir(mdir)
        print(songs)
        p=input("enter song name.....:")
        try:
            mixer.init()
            mixer.music.load(f"F:\\{p}")
            mixer.music.play()
            while True:
                h=input()
                if h=="stop":
                    mixer.music.stop()
                    break
        except:
            print(f"{p} is not an mp3,ogg,wav extention file")

    

    

def web ():
    try:
        k=input("enter search:__")
        print("searching...")
        results=wikipedia.summary(k,sentences=10)
        print("results:",results)
    except Exception as e:
        print("you have not an internet connection or speed")
        u=input("do you want to see drivers error type yes to see error or press any key to exit  :")
        if u=="yes":
            print("ERROR: " ,e)
        else:
            return None
            
            
def cd (path):
    os.chdir(path)
    os.listdir(path)
   
def GUI ():
    se=t.textinput("WIKIPEDIA","search")
    at=wikipedia.summary( se,sentences=2)
    c=t.textinput("result",f"{at}/// want to search anything")
    wikipedia.summary( c,sentences=2)


def start():
    r=Tk()
    r.title("user")
    def shut():
        print("shutting down")
        time.sleep(5)
        quit()
    
    b=Button(r,text="0!",bg="red",fg="white",command=shut).pack(anchor=W)
    r.mainloop()