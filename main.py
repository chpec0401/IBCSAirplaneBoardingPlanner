import os
import subprocess
import tkinter as tk

from CA import ca
from GA import GA

window =tk.Tk()
#设置窗口title
window.title('Airplane program')
window.geometry('400x300')
window.grid()
button11=tk.Button(window,text="Enter Chatroom",command=window.quit,width=20,height=2)
button=tk.Button(window,text="exit",command=window.quit,width=20,height=2)
def program1():
    button11.grid(row=6, column=0)
    button.grid(row=7, column=0)
    import Client

label1=tk.Label(window,text="The Airplane App thing",width=50,height=2)
button1=tk.Button(window,text="Chat",command=program1,width=20,height=2)
button0=tk.Button(window,text="Passenger Distribution",command=GA.genetic,width=20,height=2)
button00=tk.Button(window,text="Boarding Method",command=ca,width=20,height=2)


label1.grid(row=1,column=0)
button0.grid(row=3,column=0)
button00.grid(row=4,column=0)
button1.grid(row=5,column=0)
button.grid(row=6,column=0)

window.mainloop()