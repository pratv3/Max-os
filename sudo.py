if __name__=='__main__':
    print("you need to load the kernel first")
    print("can`t get 1100101 from root")
    print("try to run kernel.py")
if __name__!='__main__':
    from tkinter import *
    import time
    import os
    import appdata as a
    print("grub permission 01111001")
    print("loading grub  initramfs 0xFFeBx00")
    print("GUI loading")
    time.sleep(4)
    print(time.strftime("%H:%M:%S"))
    def desktop():
        os.system("cls")
        r=Tk()
        r.title("myos startup")
        def web():
            a.GUI()
        def roll():
            a.start()
        r.geometry("700x480")
        r.configure(bg="light blue")
        h=time.strftime("%I:%M %p")
        wem=Button(r,text="WemRowser",fg="black",bg="pink",command=web).pack(anchor=W)
        b=Button(r,text=f"<*M*> :time--{h}",bg="black",fg="grey",font="lucida 13 bold",relief=SUNKEN,anchor=W,command=roll).pack(side=BOTTOM,fill=X)
        r.mainloop()
    desktop()

