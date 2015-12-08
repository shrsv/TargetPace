#!/usr/bin/python

from Tkinter import *
import target_pace
import tkMessageBox

top = Tk()

frame = Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )

lastframe = Frame(bottomframe)
lastframe.pack( side = BOTTOM )

dist_label = Label(frame, text="Distance (kms)")
dist_label.pack( side = LEFT)
distuu = Entry(frame, bd = 2)
distuu.pack(side = RIGHT)

time_label = Label(bottomframe, text="Target Time (mins)")
time_label.pack( side = LEFT)
time = Entry(bottomframe, bd = 2)
time.pack(side = RIGHT)

def doCalculation():
    global distuu, time
    d = float(distuu.get())
    t = int(time.get())
    tkMessageBox.showinfo("Target pace", "Target pace should be: %s mins/km" % target_pace.calc_pace(d, t))
    print

calculate = Button(lastframe, text="Calculate", command=doCalculation)
calculate.pack()

top.mainloop()
