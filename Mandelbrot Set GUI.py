
import numpy as np
import matplotlib.pyplot as plt
import time

from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
  

window = Tk()

window.title("Mandelbrot Set")
window.geometry('700x600')


x0, y0 = 0, 0
c = 0

end = 0


def mandelbrot(x0, y0, max_iter):
    x, x2 = 0, 0
    y, y2 = 0, 0
    n = 0

    while (x2 + y2 < 4) and (n < max_iter):
        x2 = x*x
        y2 = y*y
        x, y = x2 - y2 + x0, 2*x*y + y0
        n += 1

    return n

def reset():
    x0Val.delete(0, 'end')
    x0Val.insert(0, "-2")
    x1Val.delete(0, 'end')
    x1Val.insert(0, "1")

    y0Val.delete(0, 'end')
    y0Val.insert(0, "-1.5")
    y1Val.delete(0, 'end')
    y1Val.insert(0, "1.5")

    iters.delete(0, 'end')
    iters.insert(0, 20)

def update():  
    
    xLow = float(x0Val.get())
    xUp = float(x1Val.get())
    yLow = float(y0Val.get())
    yUp = float(y1Val.get())
    max_iter = int(iters.get())

    ratio = (yUp - yLow) / (xUp - xLow)
    columns = 900
    rows = 900

    #print(globals())

    result = np.zeros((rows, columns)) 

    start = time.time()

    for ind, x in np.ndenumerate(result):
        y0 = yLow + (yUp - yLow) * ind[0] / rows
        x0 = xLow + (xUp - xLow) * ind[1] / columns
        c = mandelbrot (x0, y0, max_iter)
        result[ind[0],ind[1]] = c


    end = time.time()
    t = "{:.2f}".format(end - start)

    # the figure that will contain the plot
    #fig = Figure(figsize = (5, 5), dpi = 100)
    fig.clear()
  
    # # adding the subplot
    plot = fig.add_subplot(1,1,1)
    
    # # plotting the graph
    plot.imshow(result, cmap = "turbo_r", extent=[xLow,xUp,-yUp,yUp], aspect = 'auto')
    canvas.draw()

    lbl_t.configure(text="CPU Time:\n" + t +" sec")
    


btn = Button(window, text="Update", command = update)
btn.place(x=50, y=350)

rst_btn = Button(window, text="Reset", command = reset)
rst_btn.place(x=50, y=400)

lbl_x0 = Label(window, text="X Min")
lbl_x0.place(x=50, y = 30)
x0Val = Entry(window,width=10)
x0Val.place(x=50, y = 50)

lbl_x1 = Label(window, text="X Max")
lbl_x1.place(x=50, y = 80)
x1Val = Entry(window,width=10)
x1Val.place(x=50, y = 100)

lbl_y0 = Label(window, text="Y Min")
lbl_y0.place(x=50, y = 130)
y0Val = Entry(window,width=10)
y0Val.place(x=50, y = 150)

lbl_y1 = Label(window, text="Y Max")
lbl_y1.place(x=50, y = 180)
y1Val = Entry(window,width=10)
y1Val.place(x=50, y = 200)

lb_iter = Label(window, text="Max Iterations:")
lb_iter.place(x=10, y = 230)
iters = Entry(window,width=10)
iters.place(x=10, y = 250)

lbl_t = Label(window, text="CPU Time: ",font=("Arial", 12))
lbl_t.place(x=20, y = 470)

reset()

fig = Figure(figsize = (5, 5), dpi = 100)

# creating the Tkinter canvas
# containing the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master = window)  

# placing the canvas on the Tkinter window
canvas.get_tk_widget().place(x=150, y=50)

window.mainloop()




