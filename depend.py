if __name__=="__main__":
     print("Malfunction by initramfs")
     print("info=try to run kernel first")
if __name__!='__main__':
     from pygame import mixer
     import os
     print("running dependencies")
     k=input("specify path of music folder")
     os.listdir(k)
     mixer.init()
     f=input("enter song name")
     mixer.music.load(k,f)
     mixer.music.play()
     while True:
          h=input()
          if h=="stop":
               mixer.music.stop()
               break

