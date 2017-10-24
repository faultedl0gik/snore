#!/usr/bin/python
#Authors: 1LT Daniel Brown
#         SGT Matlock
#Purpose: Designed to allow error free snort rule entry for non 
#technical personnel.
#############################

from Tkinter import *

root = Tk()
root.geometry("850x100")
root.title("Snore")
root.pack_propagate(False)

class Menu(OptionMenu):
    def __init__(self, master, current, *options):
        self.master = master
        self.var=StringVar(master)
        self.var.set(current)
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(font=('calibri',(10)),bg='light blue',width=5)
    
    def getattA(self):
        return self.var

class EnterField(Entry):
    def __init__(self,master):
        Entry.__init__(self,master)
        self.config(bg='cadet blue',width=15)

class Labelz(Label):
    def __init__(self,master,current):
        self.master=master
        self.var=StringVar()
        self.var.set(current)
        Label.__init__(self,textvariable=self.var)
        self.config(bg='snow',relief=RAISED,width=10)

class Buttonz(Button):
    def __init__(self,master,current,function):
        self.master=master
        self.var=StringVar()
        self.var.set(current)
        Button.__init__(self,text=self.var,command=function)
        self.config(width=10,bg='green')



#menu1 = Menu(root)
menu1 = Menu(root, 'Alert','Alert','Log','Pass','Active','Dynamic','Drop','Reject','sdrop')
menu2 = Menu(root, 'IP', 'TCP', 'UDP','ICMP','IP')
entry1 = EnterField(root)
entry2 = EnterField(root)
menu3 = Menu(root, '<->','<-','->','<->')
entry3 = EnterField(root)
entry4 = EnterField(root)
entry5 = EnterField(root)


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
entry5.config(bg='seashell3',width=20)

def enterRule():
    text = menu1.self.var() + " " + menu2.self.var() + " " 
    + entry1() + " " + entry2() + " " 
    + menu3.self.var() + " " + entry3() + " " 
    + entry4() + " " + entry5()

    with open('/etc/snort/rules/local.rules','a') as f:
        try:
            f.write(text)
        finally:
            f.close
    print("Rule is " + text)
    print("Rule saved to snort rules local.rules file")

button1 = Buttonz(root,'Save Rule',enterRule())

root.mainloop()
