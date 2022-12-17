import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

IP_ADDRESS = '127.0.0.1'
PORT = 8181
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry('300x300')
    window.configure(bg='lightskyblue')

    selectLabel = Label(window,text='Select Song', bg='lightskyblue', font=('Calibri',8))
    selectLabel.place(x=2,y=1)
    
    listBox = Listbox(window,height=10,width=39,activestyle='dotbox', bg='lightskyblue',borderwidth = 2, font=('Calibri',10))
    listBox.place(x=10,y=18)

    scrollbar1 = Scrollbar(listBox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listBox.yview)

    play = Button(window, text='Play', width=10,bd=1,bg='skyblue',font=('Calibri',10))
    play.place(x=30,y=200)

    stop = Button(window,text='Stop',bd=1,width=10,bg='skyblue',font=('calibri',10))
    stop.place(x=200,y=200)

    upload = Button(window,text='Upload',width=10, bd=1,bg='skyblue', font=('calibri',10))
    upload.place(x=30,y=250)

    download = Button(window, text="Download", width=10, bd=1, bg='skyblue', font=('calibri', 10))
    download.place(x=200,y=250)

    info = Label(window, text="", fg='blue', font=('calibri', 10))
    info.place(x=4,y=280)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    musicWindow()

setup()

