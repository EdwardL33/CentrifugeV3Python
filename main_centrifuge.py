import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
import serial.tools.list_ports
import serial, time

top = None
BAUDRATE = 115200
root = tkinter.Tk()
root.wm_title("Centrifuge Interface")

i = tkinter.PhotoImage(width=1, height=1)

fig = Figure(figsize=(5, 4), dpi=100,layout="constrained")
# t = np.arange(0, 3, .01)
# fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

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
    ser.baudrate = BAUDRATE
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
    ser.baudrate = BAUDRATE
    ser.port = 'COM5'
    ser.open()
    INPUT = profile_text.get("1.0", "end")
    INPUT = 'u' + INPUT + 'uo' # add start and stop characters to the string
    for i in INPUT:
        ser.write(i.encode('utf-8',errors="ignore"))
        time.sleep(0.01)
    time.sleep(0.1)
    x = ser.read_all()
    print(x)
    ser.close()






# popup for manual mode
def open_popup():
    ser = serial.Serial()
    ser.baudrate = BAUDRATE
    ser.port = 'COM5'
    ser.open()
    INPUT = "m"
    for c in INPUT:
        ser.write(c.encode('utf-8',errors="ignore"))
        time.sleep(0.01)
        time.sleep(0.1)
    x = ser.read_all()
    print(x)
    ser.close()

    global top
    top= tkinter.Toplevel(root)
    top.geometry("750x250")
    top.title("Manual Mode")

    top.protocol("WM_DELETE_WINDOW", manual_mode_off)

    button_close = tkinter.Button(master=top, text="Exit Manual Mode", command=manual_mode_off, image=i, compound='c', width=100, height=100)
    button_close.pack(side=tkinter.BOTTOM)

    button_motor_on_brake_off = tkinter.Button(master=top, text="Motor ON", command=motor_on_brake_off, image=i, compound='c', width=100, height=100)
    button_motor_on_brake_off.pack(side=tkinter.LEFT)

    button_motor_off_brake_off = tkinter.Button(master=top, text="Motor OFF", command=motor_off_brake_off, image=i, compound='c', width=100, height=100)
    button_motor_off_brake_off.pack(side=tkinter.LEFT)

    button_motor_off_brake_on = tkinter.Button(master=top, text="BRAKE", command=motor_off_brake_on, image=i, compound='c', width=100, height=100)
    button_motor_off_brake_on.pack(side=tkinter.LEFT)

    label = tkinter.Label(top, text="Sending voltage:")
    label.pack(side=tkinter.TOP, pady=(10, 0))  # Padding: 10 above, 0 below

    slider = tkinter.Scale(top, from_=0, to=9, orient=tkinter.HORIZONTAL, length=300)
    slider.pack(side=tkinter.TOP, pady=10)
    
    def set_voltage():
        val = slider.get()  
        char_to_send = str(val)      # convert integer to string character, e.g. '5'
        print(val)
        ser = serial.Serial()
        ser.baudrate = BAUDRATE
        ser.port = 'COM5'
        ser.open()
        ser.write(char_to_send.encode('utf-8'))  # send as bytes over serial
        time.sleep(0.01)
        time.sleep(0.1)
        x = ser.read_all()
        print(x)
        ser.close()

    button_set_voltage = tkinter.Button(top, text="Set Voltage", command=set_voltage, width=10)
    button_set_voltage.pack(side=tkinter.TOP, padx=10)

def manual_mode_off():
    global top
    # send 2nd m to enter idle mode
    ser = serial.Serial()
    ser.baudrate = BAUDRATE
    ser.port = 'COM5'
    ser.open()
    INPUT = "m"
    ser.write(INPUT.encode('utf-8',errors="ignore"))
    time.sleep(0.01)
    time.sleep(0.1)
    x = ser.read_all()
    print(x)
    ser.close()
    if top:  # Close popup if it exists
        top.destroy()

def motor_on_brake_off():
    ser = serial.Serial()
    ser.baudrate = BAUDRATE
    ser.port = 'COM5'
    ser.open()
    INPUT = "C"
    for i in INPUT:
        ser.write(i.encode('utf-8',errors="ignore"))
        time.sleep(0.01)
    time.sleep(0.1)
    x = ser.read_all()
    print(x)
    ser.close()

def motor_off_brake_off():
    ser = serial.Serial()
    ser.baudrate = BAUDRATE
    ser.port = 'COM5'
    ser.open()
    INPUT = "c"
    for i in INPUT:
        ser.write(i.encode('utf-8',errors="ignore"))
        time.sleep(0.01)
    time.sleep(0.1)
    x = ser.read_all()
    print(x)
    ser.close()

def motor_off_brake_on():
    ser = serial.Serial()
    ser.baudrate = BAUDRATE
    ser.port = 'COM5'
    ser.open()
    INPUT = "b"
    for i in INPUT:
        ser.write(i.encode('utf-8',errors="ignore"))
        time.sleep(0.01)
    time.sleep(0.1)
    x = ser.read_all()
    print(x)
    ser.close()









 
 

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

button_status = tkinter.Button(master=root, text="Close", command=_quit, image=i, compound='c', width=100, height=100)
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

def update_plot():
    INPUT = profile_text.get("1.0", "end")
    lines = INPUT.strip().split('\n')
    x_vals = []
    y_vals = []
    for line in lines:
        try:
            if ',' not in line:
                continue
            parts = line.strip().split(',')
            if len(parts) != 2:
                continue
            x, y = parts
            x = int(x.strip())
            y = float(y.strip())
            x_vals.append(x)
            y_vals.append(y)
        except ValueError:
            continue  # skip malformed lines

    fig.clear()
    ax = fig.add_subplot(111)  # get the Axes instance
    ax.plot(x_vals, y_vals, marker='o', linestyle='-', color='b')
    ax.set_title("Profile")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("g")
    ax.grid(True)
    canvas.draw()
    root.after(1000, update_plot) 

root.after(10, task)
root.after(10, update_plot) 

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.