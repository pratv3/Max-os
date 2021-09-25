import os
import time
import colorama
import appdata as a
# myos is a linux based operating system on debian distro and bash language
os.system("cls")
os.system("title myos rolling/64")
os.system("color 07")
print("\u001b[32m**myoslinux *64/86bit operating system**")
time.sleep(2)
print("\u001b[37mlocating kernel...")
time.sleep(2)
print("inflating kernel...")
time.sleep(2)
print("loading grub...")
time.sleep(3)
os.system("color 97")
os.system("cls")
print("---------------------------GRUB------------------------------")
print("                        1.myos CLI *64/86")
print("                        2.myos GUI, *64/86")
print("                        3.myos only ram *64/86")
print("                        4.myos exit *64/86")
print("                        5.open shell here")
b=input("write number of action and press enter to continue:")
os.system("color 0a")
if b=="1" :
    os.system("cls")
    print("opening window...")
    print("booting myos.sfs...")
    print("loading os to ram...")
    print("opening window...")
    print("booting myos.sfs...")
    print("loading os to ram...")
    print("opening window...")
    print("booting myos.sfs...")
    print("loading os to ram...")
    print("opening window...")
    print("booting myos.sfs...")
    print("loading os to ram...")
    time.sleep(1)
    os.system("cls")
    os.system("color e0")
    print("login")
    print("date",time.strftime("%I %M %p on %A, %B  %e ,%Y"))
    p=input("enter username..:")
    x=input("enter password..:")
    if  x=="root" :
        print("acess granted")
        time.sleep(1)
        os.system("cls")
        os.system("color fc")
        print("PRETTY_NAME=MYOS GNU/Linux Rolling")
        print("ID like= debian")
        print("version= 2020.2")
        print("devloper pratv3")   
        while True:
            k=input("user@myos : $")

            if k=="ls":
                os.system("dir")
            elif k=="cat /etc/os-release":
                print("PRETTY_name=MYOS /GNU/LINUX/rolling")
                print("ID_LIKE=Debian")
                print("VERSION=2020.1")
                print(f"USERNAME={p}")

            elif k=="sudo su":
                k=input("root@myos : #")
            elif k=="myaudio":
                a.music()

            elif k=="w3m":
                a.web()


            elif "cd" in k:
                m=k.replace("cd","")
                a.cd(m)
            elif k=="shutdown":
                print("shutting down...")
                time.sleep(1)
                os.system("color 0a")
                os.system("cls")
                print("unmounting systerm...")
                time.sleep(1)
                print("shutting down myos.sfs...")
                print("session saved for further snapshots....")
                time.sleep(1)
                os.system("cls")
                exit()

            elif k=="clear":
                os.system("cls")
                
                

            else:
                print(f"bash:{k} command not found") 
            
        
             
    else:
        print("acess denied")
        print("shutting down")
        exit()

elif b=="2":
    import sudo

elif b=="5":
    o=input("user@myos: $")


if __name__=='__main__':
    pass
    
