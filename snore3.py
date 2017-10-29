#!/usr/bin/python
##Authors: 1LT Daniel Brown
##         SGT Matlock
##Purpose: Designed to allow error free snort rule entry for non 
##technical personnel.
################################################################
from Tkinter import *

root = Tk()
root.pack_propagate(False)
root.geometry("800x500")
root.title("Snore")

f = open('C://Users//Daniel//Desktop//Snore//snore-master//logs//local.rules','r')
file_contents = f.read()

##addFrame = Frame(root, bg = 'white')
##readFrame = Frame(root, bg = 'orange')
##deleteFrame = Frame(root, bg = 'green')
##
##menuBar = Menu(root)
##filemenu = Menu(menuBar)
##menuBar.add_cascade(label="DO STUFF", menu=filemenu)
##filemenu.add_command(label="Switch Frame")
##root.config(menu = menuBar)

######################################################################################
##These classes make adding widgets easier...ostensibly. Classes are kind
##of a pain in the ass.
class Menuz(OptionMenu):
    def __init__(self, master, current, *options):
        self.master = master
        self.var=StringVar(master)
        self.var.set(current)
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(font=('calibri',(10)),bg='light blue',width=5)
        
class EnterField(Entry):
    def __init__(self,master,current):
        self.master=master
        self.var=StringVar()
        self.var.set(current)
        Entry.__init__(self, textvariable=self.var)
        self.config(bg='cadet blue', width=15)

class Labelz(Label):
    def __init__(self,master,current):
        self.master=master
        self.var=StringVar()
        self.var.set(current)
        Label.__init__(self, textvariable=self.var)
        self.config(bg='snow', relief=RAISED,width=10)

##Working on this button....it mostly works, but I haven't programmed
##in two years so I'm doing the best that I can so stop whining.
##class Buttonz(Button):
##    def __init__(self,master,current,function):
##        self.master=master
##        self.var=StringVar()
##        self.var.set(current)
##        Button.__init__(self,text=self.var,command=function)
##        self.config(width=10,bg='green')

##This section is where the widgets are insantiated. 
#menu1 = Menu(root)

menu1 = Menuz(root, 'Alert','Alert','Log','Pass','Active','Dynamic','Drop','Reject','sdrop')
menu2 = Menuz(root, 'IP', 'TCP', 'UDP','ICMP','IP')

entry1 = EnterField(root,'ENTER IP')
entry2 = EnterField(root,'PORT')
menu3 = Menuz(root, '<->','<-','->','<->')
entry3 = EnterField(root,'ENTER IP')
entry4 = EnterField(root,'PORT')
entry5 = EnterField(root,'ENTER MSG')

label1 = Labelz(root,'ALERT TYPE')
label1.grid(column=1,row=1)
menu1.grid(column=1,row=2)
menu1.config(width=6)

label2 = Labelz(root,'PROTO TYPE')
label2.grid(column=2,row=1)
menu2.grid(column=2,row=2)

label3 = Labelz(root, 'SRC IP')
label3.grid(column=3,row=1)
label3.config(width=5)
entry1.grid(column=3,row=2)

label4 = Labelz(root,'SRCPORT')
label4.grid(column=4,row=1)
label4.config(width=8)
#Entry field for Port Number
entry2.grid(column=4,row=2)
entry2.config(bg='orange red',width=7)

label5 = Labelz(root,'DIRECTION')
label5.grid(column=5,row=1)
#Menu for direction
menu3.grid(column=5,row=2)

#Entry for destination IP Address
label6 = Labelz(root,'DST IP')
label6.grid(column=6,row=1)
label6.config(width=5)
entry3.grid(column=6,row=2)
entry3.config(bg='cadet blue',width=15)

#Entry for Destination Port
label7 = Labelz(root,'DSTPORT')
label7.grid(column=7,row=1)
label7.config(width=7)
entry4.grid(column=7,row=2)
entry4.config(bg='orange red',width=7)

label8 = Labelz(root,'ALERT DATA')
label8.grid(column=8,row=1)
entry5.grid(column=8,row=2)
entry5.config(bg='seashell3',width=40)

#label9 = Labelz(root, 'DO COOL THINGS')
#label9.config(width=30)
#label9.pack(side=BOTTOM,fill=X)

##This function concatenates the text variables the user has inputed
##above in the different classes and saves it as a rule to the snort
##file.
def enterRule():
    a = (menu1.var).get()
    b = (menu2.var).get()
    c = (menu3.var).get()
    d = (entry1.var).get()
    e = (entry2.var).get()
    f = (entry3.var).get()
    g = (entry4.var).get()
    h = (entry5.var).get()
    text = a+ " "+b+" "+d+" "+e+" "+c+" "+f+" "+g+" "+h+"\n"

 #   with open('/etc/snort/rules/local.rules','a') as f:
 #If you're using windows ensure you use // slashes...or else the file won't work.
    with open('C://Users//Daniel//Desktop//Snore//snore-master//logs//local.rules','a') as f:
        try:
            f.write(text)
        finally:
            f.close
    v = StringVar()
    Label(root,textvariable=v).pack(side=BOTTOM)
    v.set("Rule " + text + "saved to snort rules local.rules file")

button1 = Button(root,text="Save Rule",command=enterRule)
button1.grid(column=5,row=3)
x = StringVar()
ruleLabel = Label(root,textvariable=x,width=100,height=100)
f.close()
def showRules():
    x.set(file_contents)
    ruleLabel.pack(side=RIGHT)
    print x
    f.close()

def hideRules():
    ruleLabel.pack_forget()

button2 = Button(root,text="Show Rules",command=showRules)
button2.grid(column=1,row=4)
button3 = Button(root,text="Hide Rules",command=hideRules)
button3.grid(column=1,row=5)

######################################################################################

##def showRoot():
##    root.pack(expand = True, fill = 'both')
##    addFrame.pack_forget()
##    deleteFrame.pack_forget()
##    readFrame.pack_forget()
##menuBar.add_command(label = 'HOME', command = showRoot)

##def showAdd():
##    addFrame.pack(expand = True, fill = 'both')
##    readFrame.pack_forget()
##    deleteFrame.pack_forget()
##menuBar.add_command(label = 'ADD RULE', command = showAdd)
##
##def showRead():
##    readFrame.pack(expand = True, fill = 'both')
##    addFrame.pack_forget()
##    deleteFrame.pack_forget()
##menuBar.add_command(label = 'READ RULES', command = showRead)
##
##def showDelete():
##    deleteFrame.pack(expand = True, fill = 'both')
##    readFrame.pack_forget()
##    addFrame.pack_forget()
##menuBar.add_command(label = 'DELETE RULES', command = showDelete)
    
root.mainloop()
