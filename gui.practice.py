from tkinter import *
from tkinter import Tk
from tkinter import ttk

def on_login_button_click():
    print("Button clicked")
    x = text.get()
    label = ttk.Label(root,text=x)
    label.pack()
    # x = entry.get() 
    print(x)

root = Tk()
root.title("Hello") 

root.geometry("800x500")

label = ttk.Label(root,text="Hello World")
label.pack()

text = StringVar()
entry = ttk.Entry(root,textvariable=text)
entry.pack()

button = ttk.Button(root,command=on_login_button_click)
button.pack()

root.mainloop()