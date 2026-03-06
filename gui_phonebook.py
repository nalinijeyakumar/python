from tkinter import *
from tkinter import Tk
from tkinter import ttk

root = Tk()
root.title("PhoneBook") 

root.geometry("800x500")

label = ttk.Label(root,text="PhoneBook")
label.pack()

root.mainloop()