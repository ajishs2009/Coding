from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('200x200')

def msg():
    messagebox.showwarning('Alert', 'Virus found!')
    messagebox.showinfo('Info', 'This virus is not halmful!')
    messagebox.showerror('Error', 'Syntax Error!')
    messagebox.askquestion('You know?', 'Yes or no')
    messagebox.askokcancel('Cancel', 'Yes!')
    messagebox.askyesno('Yes?', 'No!')
    messagebox.askretrycancel('Alert', 'Virus found!')

button = Button(root, text='Scan for virus', command=msg)
button.place(x=40, y=80)

root.mainloop()