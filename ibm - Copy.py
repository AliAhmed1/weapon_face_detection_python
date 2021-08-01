import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
import json
from ibm_watson import VisualRecognitionV4
from ibm_watson.visual_recognition_v4 import AnalyzeEnums, FileWithMetadata
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from mail import SendMail
import tkinter as tk
from tkinter import *
import csv
import numpy as np
from PIL import Image,ImageTk
import datetime
import time
import yagmail
import getpass



cap = cv2.VideoCapture(0)    
#cap = cv2.VideoCapture('WhatsApp Video 2021-05-31 at 8.42.24 PM.mp4')
plt.rcParams['figure.figsize'] = [12, 5]


window = tk.Tk()
window.title("Face-Weapon-detection-based-security-System")

window.geometry('1280x600')
window.configure(background='snow')

def camera():
    authenticator = IAMAuthenticator(apikey="ZQBgX2TPs2CmC3wNLWGEr7X3xDmq42sDsqTZVCsjdke8")

    flag = False
    obj = VisualRecognitionV4(version = '2021-06-01',authenticator=authenticator)
    #2021-03-25
    obj.set_service_url(service_url = 'https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/2fa93f7c-36f0-48f9-abb1-15845fbe94e1')
    
    while True:
        success, img = cap.read()
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img = cv2.resize(img,(1000,1000))
        cv2.imwrite('4.jpg',img)
        with open('4.jpg', 'rb') as honda_file,open('4.jpg', 'rb') as dice_file:
            result = obj.analyze(
                collection_ids=["17951ae7-0169-4551-ac19-a3864c7eed65",'17951ae7-0169-4551-ac19-a3864c7eed65'],
                features=[AnalyzeEnums.Features.OBJECTS.value],
                images_file=[
                    FileWithMetadata(honda_file),
                ], 
            threshold=0.15).get_result()
            #print(json.dumps(result, indent=2))
        img = cv2.imread('4.jpg')
        try:
            left = result['images'][0]['objects']['collections'][0]['objects'][0]['location']['left']
            top = result['images'][0]['objects']['collections'][0]['objects'][0]['location']['top']
            width = result['images'][0]['objects']['collections'][0]['objects'][0]['location']['width']
            height = result['images'][0]['objects']['collections'][0]['objects'][0]['location']['height']

            img = cv2.imread('4.jpg')
            cv2.rectangle(img,(left,top),
                        (left+width,top+height)
                        ,(255,0,0), 2)
            name = result['images'][0]['objects']['collections'][0]['objects'][0]['object']
            cv2.putText(img,name,(left,top)
                        ,cv2.FONT_HERSHEY_SIMPLEX,1
                        ,(255,0,0), 2)
            
            #img = cv2.resize(img,(500,500))
            cv2.imshow('gasm', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27: # press 'ESC' to quit
                break
                cv2.show('gasm',img)
        
            if name == 'gun' and flag == False:
                flag = True
                SendMail()
        except:
            cv2.imshow('gasm',img)
            # pass
        # cv2.show('gasm',img)
    cap.release()
    # cv2.waitKey(0)
    cv2.destroyAllWindows()



def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        
window.protocol("WM_DELETE_WINDOW", on_closing)

message = tk.Label(window, text="Face-Weapon-detection-based-security-System", bg="cyan", fg="black", width=50,
                   height=3, font=('times', 30, 'italic bold '))
message.place(x=80, y=50)

Notification = tk.Label(window, text="All things good", bg="Green", fg="white", width=15,
                      height=3, font=('times', 17, 'bold'))

FA = tk.Button(window, text="Start Security Camera",fg="white",command=camera  ,bg="blue2"  ,width=20  ,height=3, activebackground = "blue" ,font=('times', 15, ' bold '))
FA.place(x=550, y=400)

# quitWindow = tk.Button(window, text="Manually Fill Attendance", command=manually_fill  ,fg="black"  ,bg="skyblue"  ,width=20  ,height=3, activebackground = "blue" ,font=('times', 15, ' bold '))
# quitWindow.place(x=990, y=500)

window.mainloop()