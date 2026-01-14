import local_simple_database
import tkinter as tk
import tkinter.font as tkFont
import json
from dataStructures import Genetic


class GA():
    def genetic():

        window = tk.Tk()
        window.title('Distribution Algorithm')
        window.geometry('350x200')
        window.grid()
        font1 = tkFont.Font(family="Helvetica", weight="bold")
        label0 = tk.Label(window, text='Passenger Distribution \nGenerator',font=font1)
        label1=tk.Label(window,text='Number of Passengers')
        entry1=tk.Entry(window)
        def a ():
            thing=Genetic(int(entry1.get()),"0").generate()
            '''dictionary={
                entry1.get():str(thing)
            }
            with open("thing.json", "w") as outfile:
                json.dump(dictionary, outfile)
                s=json.loads(outfile)
            print (s{entry1.get()})'''



        button1=tk.Button(window,text='Generate',command=a)
        label0.grid(row=0, column=0)
        label1.grid(row=1,column=0)
        entry1.grid(row=1,column=1)
        button1.grid(row=2,column=0)


        window.mainloop()