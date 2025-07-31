from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="ridge")
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)


ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

# content.grid(column=0, row=0)
content.pack(expand="True")
frame.pack(expand="True")
# namelbl.grid(column=3, row=0, columnspan=2)
# name.grid(column=3, row=1, columnspan=2)

ok.pack( side = LEFT , fill=BOTH, expand=1)


root.mainloop()