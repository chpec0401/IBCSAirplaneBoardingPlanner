import tkinter as tk
import tkinter.font as tkFont
import numpy as np
import os
from cellular import *
from moviepy.editor import *
import cv2
from os import startfile
global d,e,f
d,e,f=0,0,0
def function():
    a=int(d)/192
    b=int(e)/192
    c=int(f)/192
    data = np.array([our(a,b,c).returnTime(), backfront(a,b,c).returnTime(), reversepy(a,b,c).returnTime(), outsidein(a,b,c).returnTime()])
    index = 0
    print (data)
    for i in range(1, 4):
        if data[i] < data[index]:
            index = i
    if i==1:
        arr = os.listdir('C:\\Users\\Eric Chang\\PycharmProjects\\IA\\our')
        print (arr)
        a=[]
        for i in arr:
            a.append('C:\\Users\\Eric Chang\\PycharmProjects\\IA\\our\\'+i)
    if i==2:
        arr = os.listdir('C:\\Users\\Eric Chang\\PycharmProjects\\IA\\outsidein')
        print (arr)
        a=[]
        for i in arr:
            a.append('C:\\Users\\Eric Chang\\PycharmProjects\\IA\\outsidein\\'+i)

    if i==3:
        arr = os.listdir('C:\\Users\\Eric Chang\\PycharmProjects\\IA\\reversepy')
        print (arr)
        a=[]
        for i in arr:
            a.append('C:\\Users\\Eric Chang\\PycharmProjects\\IA\\reversepy\\'+i)
    if i==0:
        arr = os.listdir('C:\\Users\\Eric Chang\\PycharmProjects\\IA\\backfront')
        print (arr)
        a=[]
        for i in arr:
            a.append('C:\\Users\\Eric Chang\\PycharmProjects\\IA\\backfront\\'+i)
    a=sorted(a)
    print (a)
    clip = ImageSequenceClip(a, fps=10)
    clip.write_videofile("C:\\Users\\Eric Chang\\PycharmProjects\\IA\\video.mp4", fps=5)
def video():
    os.startfile("C:\\Users\\Eric Chang\\PycharmProjects\\IA\\video.mp4")
def ca():
    window = tk.Tk()
    window.title('Boarding Assessment')
    window.geometry('350x300')
    window.grid()
    font1 = tkFont.Font(family="Helvetica", weight="bold")
    title = tk.Label(window, text='Boarding Method \nGenerator', font=font1)
    label1 = tk.Label(window, text='Passengers with luggage')
    label2 = tk.Label(window, text='passengers with purse')
    label3 = tk.Label(window, text='Passengers with disabilities')


    entry1 = tk.Entry(window)
    entry2 = tk.Entry(window)
    entry3 = tk.Entry(window)
    d, e, f = entry1.get(), entry2.get(), entry3.get()
    button = tk.Button(window, command=function,text="Generate Order")
    button1 = tk.Button(window, command=video, text="Play Video")
    label1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    label3.grid(row=3, column=0)

    entry1.grid(row=1, column=1)
    entry2.grid(row=2,column=1)
    entry3.grid(row=3,column=1)
    button.grid(row=4,column=0)
    button1.grid(row=5,column=0)
    window.mainloop()









