#!/usr/bin/python

import Tkinter

root = Tkinter.Tk()

def iFrame():
    stringVar = Tkinter.StringVar()
    frame = Tkinter.Frame(root)
    frame.pack()
    label = Tkinter.Label(frame,
                          text = ':',
                          width = 10,
                          anchor = 'e')
    label.pack(side = 'left')
    entry = Tkinter.Entry(frame,
                          textvariable = stringVar,
                          width = 50)
    entry.pack(side = 'left')

iFrame()
