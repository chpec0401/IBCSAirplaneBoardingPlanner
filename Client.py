import socket
import tkinter
import tkinter.messagebox
import threading
import json
import tkinter.filedialog
from tkinter.scrolledtext import ScrolledText

IP = ''
PORT = ''
user = ''
listbox1 = ''
show = 1
users = []
chat = '------Group chat-------'

#登陆窗口

root0 = tkinter.Tk()
root0.geometry("300x150")
root0.title('Login Page')
root0.resizable(0,0)
one = tkinter.Label(root0,width=300,height=150,bg="LightBlue")
one.pack()

IP0 = tkinter.StringVar()
IP0.set('')
USER = tkinter.StringVar()
USER.set('')

labelUSER = tkinter.Label(root0,text='Username',bg="LightBlue")
labelUSER.place(x=20,y=70,width=100,height=40)

entryUSER = tkinter.Entry(root0, width=60, textvariable=USER)
entryUSER.place(x=120,y=75,width=100,height=30)

def Login(*args):
	global IP, PORT, user
	IP, PORT = str('127.0.0.1:9999').split(':')
	user = entryUSER.get()
	if not user:
		tkinter.messagebox.showwarning('warning', message='Username blank!')
	else:
		root0.destroy()

loginButton = tkinter.Button(root0, text ="login", command = Login,bg="Yellow")
loginButton.place(x=135,y=110,width=40,height=25)
root0.bind('<Return>', Login)

root0.mainloop()


global s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, int(PORT)))
if user:
    s.send(user.encode())
else:
    s.send('user DNE'.encode())
    user = IP + ':' + PORT


root1 = tkinter.Tk()
root1.geometry("640x480")
root1.title('Chat')
root1.resizable(0,0)


listbox = ScrolledText(root1)
listbox.place(x=5, y=0, width=640, height=320)
listbox.tag_config('tag1', foreground='red',backgroun="yellow")
listbox.insert(tkinter.END, 'Welcome to the chat!', 'tag1')

INPUT = tkinter.StringVar()
INPUT.set('')
entryIuput = tkinter.Entry(root1, width=120, textvariable=INPUT)
entryIuput.place(x=5,y=320,width=580,height=170)


listbox1 = tkinter.Listbox(root1)
listbox1.place(x=510, y=0, width=130, height=320)


def send(*args):
	message = entryIuput.get() + '~' + user + '~' + chat
	s.send(message.encode())
	INPUT.set('')

sendButton = tkinter.Button(root1, text ="\n发\n\n\n送",anchor = 'n',command = send,font=('Helvetica', 18),bg = 'white')
sendButton.place(x=585,y=320,width=55,height=300)
root1.bind('<Return>', send)


def receive():
	global uses
	while True:
		data = s.recv(1024)
		data = data.decode()
		print(data)
		try:
			uses = json.loads(data)
			listbox1.delete(0, tkinter.END)
			listbox1.insert(tkinter.END, "Online")
			listbox1.insert(tkinter.END, "------Group chat-------")
			for x in range(len(uses)):
				listbox1.insert(tkinter.END, uses[x])
			users.append('------Group chat-------')
		except:
			data = data.split('~')
			message = data[0]
			userName = data[1]
			chatwith = data[2]
			message = '\n' + message
			if chatwith == '------Group chat-------':
				if userName == user:
					listbox.insert(tkinter.END, message)
				else:
					listbox.insert(tkinter.END, message)
			elif userName == user or chatwith == user:
				if userName == user:
					listbox.tag_config('tag2', foreground='red')
					listbox.insert(tkinter.END, message, 'tag2')
				else:
					listbox.tag_config('tag3', foreground='green')
					listbox.insert(tkinter.END, message,'tag3')

			listbox.see(tkinter.END)
r = threading.Thread(target=receive)

r.start()

root1.mainloop()
s.close()
