#!/usr/bin/python
import Tkinter

tk = Tkinter.Tk()

tk.pack_propagate(False)

redFrame = Tkinter.Frame(tk, bg = 'red')
blueFrame = Tkinter.Frame(tk, bg = 'blue')
greenFrame = Tkinter.Frame(tk, bg = 'green')

entry = Tkinter.Entry(redFrame)
entry.pack()

menuBar = Tkinter.Menu(tk)

tk.config(menu = menuBar)

def showRed():
    redFrame.pack(expand = True, fill = 'both')
    greenFrame.pack_forget()
    blueFrame.pack_forget()

menuBar.add_command(label = 'Red', command = showRed)

def showBlue():
    blueFrame.pack(expand = True, fill = 'both')
    greenFrame.pack_forget()
    redFrame.pack_forget()
menuBar.add_command(label = 'Blue', command = showBlue)

def showGreen():
    greenFrame.pack(expand = True, fill = 'both')
    redFrame.pack_forget()
    blueFrame.pack_forget()
menuBar.add_command(label = 'Green', command = showGreen)

tk.mainloop()
