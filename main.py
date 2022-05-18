from tkinter import  *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Nguva Zvamanje manje...")

def getTime():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, getTime)

label = Label(root, font=("ds-digital",  80), background= "black", foreground="skyblue")
label.pack(anchor='center')
getTime()

mainloop()