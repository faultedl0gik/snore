#!/usr/bin/python
from Tkinter import *
#from PIL import Image, ImageTk

root = Tk()
root.geometry("500x400")
root.title("Snore Snort Rule Entry Tool")
root.pack_propagate(False)

#Gonna use this mainframe laterszzzz
mainFrame = Frame(root,
                  width=300,
                  height=200,
                  borderwidth=2,
                  relief="ridge",
                  padx=10,
                  pady=10,
                  bg="red")
#mainFrame.pack()
#mainFrame.pack_propagate(False)

ruleFrame = Frame(root,width=100,bg = 'red')

# This will be the button
e = Entry(ruleFrame, width=100, bg = 'red')
e.pack()

#This is the text entry box
e1 = Entry(root,width=100,bg = 'orange red')
e1.pack()

#Going to put a coolio image in the background
#image = Image.open("~/Desktop/index.png")
#photo = ImageTk.PhotoImage(image)

#label = Label(image=photo)
#label.image = photo
#label.pack()

def enterRule():
    #ruleFrame.pack(expand = True, fill = 'both')
    text = e.get() + " " + e1.get() + "\n"
    with open('/etc/snort/rules/local.rules','a') as f:
        try:
            f.write(text)
        finally:
            f.close()
    print("Rule Saved to Snort Conf File")

b = Button(root, text="Save Rule :D",width=25, command=enterRule, bg = 'Green')
b.pack()        

mainloop()
