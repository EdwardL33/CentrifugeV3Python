import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import TextBox, Button

fig, FULL_ax = plt.subplots(layout="constrained")
# fig.subplots_adjust(bottom=0.2)
FULL_ax.axis('off')

import matplotlib.gridspec as gridspec
gs0 = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[1, 4])
gs1 = gridspec.GridSpecFromSubplotSpec(5, 1, subplot_spec=gs0[0], height_ratios=[4, 2, 2, 1, 1])

plot_ax = fig.add_subplot(gs0[1])
text_ax = fig.add_subplot(gs1[0])
text_ax.axis('off')
start_ax = fig.add_subplot(gs1[1])
stop_ax = fig.add_subplot(gs1[2])
man_ax = fig.add_subplot(gs1[3])
upload_ax = fig.add_subplot(gs1[4])

t = np.arange(-2.0, 2.0, 0.001)
l, = plot_ax.plot(t, np.zeros_like(t), lw=2)


def submit(expression):
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    plot_ax.relim()
    plot_ax.autoscale_view()
    plt.draw()

def start(event):
    print("Start")

def stop(event):
    print("Sto9p")

def manual(event):
    print("Man")

def upload(event):
    print("Upload")

# axbox = fig.add_axes([0.1, 0.05, 0.6, 0.075])
# axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
# axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
# text_box = TextBox(text_ax, "", textalignment="left")
# text_box.on_submit(submit)
# text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
text_ax.text(0.05, 0.95, "yeetus", transform=text_ax.transAxes, fontsize=14,
        verticalalignment='top')
bnext = Button(start_ax, 'Start')
bnext.on_clicked(start)
bprev = Button(stop_ax, 'Stop')
bprev.on_clicked(stop)
bprev = Button(man_ax, 'Manual')
bprev.on_clicked(manual)
bprev = Button(upload_ax, 'Upload')
bprev.on_clicked(upload)

plt.show()