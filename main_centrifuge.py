import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
import serial.tools.list_ports
import serial, time

root = tkinter.Tk()
root.wm_title("Centrifuge Interface")

i = tkinter.PhotoImage(width=1, height=1)

fig = Figure(figsize=(5, 4), dpi=100,layout="constrained")
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas)


# canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


def on_stop_press():
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = 'COM5'
    ser.open()
    INPUT = "q"
    for i in INPUT:
        ser.write(i.encode('utf-8',errors="ignore"))
        time.sleep(0.01)
    time.sleep(0.1)
    x = ser.read_all()
    print(x)
    ser.close()


def on_start_press():
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = 'COM5'
    ser.open()
    INPUT = profile_text.get("1.0", "end")
    INPUT = 'u' + INPUT + 'u' # add start and stop characters to the string
    for i in INPUT:
        ser.write(i.encode('utf-8',errors="ignore"))
        time.sleep(0.01)
    time.sleep(0.1)
    x = ser.read_all()
    print(x)
    ser.close()

# popup for manual mode
def open_popup():
   top= tkinter.Toplevel(root)
   top.geometry("750x250")
   top.title("Child Window")
   button_close = tkinter.Button(master=top, text="close", command=top.destroy, image=i, compound='c', width=100, height=100)
   button_close.pack(side=tkinter.BOTTOM)

root.grid_propagate(False)


entryFrame = tkinter.Frame(root)
entryFrame.grid_propagate(False)
entryFrame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
profile_text = tkinter.Text(master=entryFrame, bg = "light yellow")
profile_text.place(x=0, y=0, relwidth=1, relheight=1)
profile_text.insert(tkinter.END,"0, 1\n\
6300, 4\n\
8600, 4.5\n\
11000, 2\n\
23000, 3\n\
31000, 1\n\
38000, 1")


# create buttons to be on the main window
button_start = tkinter.Button(master=root, text="Start", command=on_start_press, image=i, compound='c', width=100, height=100)
button_start.pack(side=tkinter.TOP)

button_stop = tkinter.Button(master=root, text="Stop", command=on_stop_press, image=i, compound='c', width=100, height=100)
button_stop.pack(side=tkinter.TOP)

button_manual = tkinter.Button(master=root, text="Manual", command=open_popup, image=i, compound='c', width=100, height=100)
button_manual.pack(side=tkinter.TOP)

button_status = tkinter.Button(master=root, text="Status", command=_quit, image=i, compound='c', width=100, height=100)
button_status.pack(side=tkinter.TOP)

# scale the window
def task():
    w, h = root.winfo_width(), root.winfo_height()
    #print(w, h)
    profile_text.config(width=int(w/4))
    # button_start.config(width=int(w/4))
    # button_stop.config(width=int(w/4))
    # button_manual.config(width=int(w/4))
    # button_status.config(width=int(w/4))

    profile_text.config(width=int(w/4), height=int(h*4/10))
    button_start.config(width=int(w/4), height=int(h*2/10))
    button_stop.config(width=int(w/4), height=int(h*2/10))
    button_manual.config(width=int(w/4), height=int(h*1/10))
    button_status.config(width=int(w/4), height=int(h*1/10))
    root.after(1000, task)  # reschedule event in 2 seconds

root.after(10, task)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.