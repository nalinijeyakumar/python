from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog, messagebox

def create_window(title):
    root = Tk()
    root.title(title) 

    root.geometry("800x500+10+10")
    return root

def add_click():
    print(text.get())
    print(ph_text.get())
    print(phone.get())
    print(measureSystem.get())
    print(state.get())

    data = text.get()+","+phone.get()+"-"+ph_text.get()
    contact = ttk.Label(frame_right, text= data )
    contact.pack()

root = create_window(title="Grid Layout")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu, tearoff=0)
menu.add_cascade(label = "File", menu=file)

file.add_command(label="New")
file.add_command(label="Open")

file.add_command(label="Import")
file.add_command(label="Export")
file.add_separator()
file.add_command(label="Exit", command=root.destroy)

about = Menu(menu, tearoff=0)
menu.add_cascade(label="About", menu = about )

frame_right = ttk.LabelFrame(root,padding= 3,text = "Contact List")
frame_right.grid(row=0, column = 1,padx = 5, pady = 5, sticky="news")

frame_left = ttk.LabelFrame(root,padding= 3,text="Enter Information")
frame_left.grid(row=0, column = 0,padx = 5, pady = 5,sticky="news")


label = ttk.Label(frame_left,text="Name")
label.grid(row=0, column=0, padx=20, pady=10, sticky="e")

text = StringVar()
entry = ttk.Entry(frame_left,textvariable=text)
entry.grid(row = 0, column = 1,padx=20, pady=10)

ph_label = ttk.Label(frame_left,text="Phone No")
ph_label.grid(row=1, column=0, padx=20, pady=10 , sticky="e")

ph_text = StringVar()
ph_entry = ttk.Entry(frame_left,textvariable=ph_text)
ph_entry.grid(row = 1, column = 1,padx=20, pady=10)

phone = StringVar()
# home = ttk.Radiobutton(frame_left, text='Home', variable=phone, value='home')
# home.grid(row = 2, column = 0,padx=20, pady=10)
# office = ttk.Radiobutton(frame_left, text='Office', variable=phone, value='office')
# office.grid(row = 3, column = 0,padx=20, pady=10)
# cell = ttk.Radiobutton(frame_left, text='Mobile', variable=phone, value='cell')
# cell.grid(row = 4, column = 0,padx=20, pady=10)

measureSystem = StringVar()
time = ttk.Checkbutton(frame_left, text='Morning', 
	    command=frame_left, variable=measureSystem,
	    onvalue='Morning', offvalue='Afternoon')
time.grid(row = 5, column = 1,padx=20, pady=10)

state = StringVar()
country = ttk.Combobox(frame_left, text="state",
                       values=["Tamilnadu","Karnataka","Kerala"])
country.grid(row = 3, column = 1,padx=20, pady=10) 

button = ttk.Button(frame_left,text = "Add",command=add_click)
button.grid(row = 6, column = 1,padx=20, pady=10,sticky="w")

style = ttk.Style()
style.configure("TFrame",background="#D2CBCB")

style.configure("frame_left", background="#16d8db", bordercolor="#0008ff")
style.configure("frame_left.Label", background="#dadfe8", foreground="#eae8e7")

style.configure("frame_right", background="#eadfe9")
style.configure("frame_right", background="#16181c", foreground="#eae7e9")


root.mainloop()