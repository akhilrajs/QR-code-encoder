from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
import threading
import pyqrcode 
import png 
from pyqrcode import QRCode 
import os
import shutil
from PIL import ImageTk, Image

# initialisng the locatio for the output 
if not os.path.exists('OutPut'):
        os.makedirs('OutPut')  
folder = 'OutPut' 
directory = os.getcwd() 
SAVE_PATH = os.path.join(directory, folder)

# making the user interface window
win = root = tk.Tk()
win.geometry("280x395") 
win.title("QR code Encoder") 
win.resizable(False, False) 
win.wm_iconbitmap('icon.ico')


# making function for quit button
def CLOSE():
	win.destroy()
	

# making the thread for accepting rhe name input
def pass_to_name(event):
	n = threading.Thread(target=lambda :namer(event))
	n.start()


# making the function for passing name to variable name_
def namer(event):
	global name_
	name_ = name.get()


# making the thead to pass to the qr code function
def pass_to_qr():
	q = threading.Thread(target=lambda :qr())
	q.start()

# making the qr function 
def qr():
	data_ = (data.get("1.0", "end-1c"))
	url = pyqrcode.create(data_)
	png_name = name_ + ".png"
	url.png(png_name, scale = 6)
	png = url.png(png_name, scale = 6)
	veiw = Toplevel()
	veiw.geometry("250x250")
	veiw.title(png_name)
	img = Image.open(png_name)
	img = img.resize((250, 250), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	pic = Label(veiw, image = img)
	pic.image = img
	pic.pack(side = "bottom", fill = "both", expand = "yes")
	# moving the qr code to the output folder created by shutil module
	source = png_name
	destination = "OutPut"
	shutil.move(source, destination)
	
	
# making the function to open the folder output folder
def pass_to_open_folder():
	f = threading.Thread(target=lambda :open_folder())
	f.start()

# making the function to open the folder
def open_folder():
	os.startfile("OutPut")

# making a laabel saying name
lbl = Label(text = "Enter the name for the output qr code file")
lbl.pack(side = TOP)

# asking what the name of the file should be 
name = Entry(win, width=45)
name.pack(side = TOP, padx = 5)
# getiing the return key and binding it to the element so as to extract the name input to function
name.bind("<Key>",pass_to_name)

# making a laabel saying name
lbl = Label(text = "Enter the text below to convert to qr code")
lbl.pack(side = TOP)


# making the entry box to accept the data form the user
global data
data =  Text(win, width=45, height = 17,bg = "light yellow")
data.pack(side = TOP, padx = 5) 

# making the button for converting the text to qr code
btn = Button(win, text = "convert to qr code", command = pass_to_qr)
btn.place(relx = 0.02, rely = 0.865)

# making a button to open the folder to which the output goes
folder = Button(win, text = "open Folder", command = pass_to_open_folder)
folder.place(relx = 0.418,rely = 0.865)

# making an button for quit option
quit = Button(win, text = "Quit", command = CLOSE)
quit.place(relx = 0.7, rely = 0.865)

# showing my name
lbl = Label(text = "coded by akhil_raj_s/py_57")
lbl.place(relx = 0.01, rely = 0.93)

win.mainloop()