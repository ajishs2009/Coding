from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.geometry('650x400')
root.title('Denomination Calculator')
root.configure(bg='light blue')
upload = Image.open('')
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)
label1 = Label(root,
               text='Hey User! Welcome to Denomination Calculator App.',
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo('Alert!', 'Do you wanna calculate the denomination count?')
    if MsgBox == 'ok':
        topwin()

button1 = Button(root,command=msg, text='Lets get started!', bg='brown', fg='white')
button1.place(x=260, y=360)

def topwin():
    top = TopLevel()
    top.title('Denomination Calculator')
    top.configure()
