#!/usr/bin/python
#Authors: 1LT Daniel Brown
#         SGT Matlock
#Purpose: Designed to allow error free snort rule entry for non 
#technical personnel.
#############################

from Tkinter import *

root = Tk()
root.geometry("700x100")
#root.title("Snore")
root.pack_propagate(False)

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("Snore")

        #These define the action menu
        self.action_options = ["Alert","Log","Pass","Active","Dynamic","Drop","Reject","sdrop"]
        self.action_var=StringVar()
        self.action_var.set("Alert")
        self.action = OptionMenu(root, self.action_var, *self.action_options)
        self.action.grid(column=1,row=2)
        
        #DropMenu_Protocol
        self.proto_options = ["TCP",
                              "UDP",
                              "ICMP",
                              "IP"]
        self.proto_var=StringVar()
        self.proto_var.set("IP")
        self.proto = OptionMenu(root, proto_var, *proto_options)
        self.proto.grid(column=2,row=2)

        

        #Input Src IP Address
        self.ip = Entry(root,width=10,bg='light blue')
        self.ip.grid(column=3,row=2)

        #Entry Field for a port
        self.port = Entry(root,width=5,bg='sea green')
        self.port.grid(column=7,row=2)

        #Last Field
        self.lastfield = Entry(root,width=50,bg='slate gray')
        self.lastfield.grid(column=8,row=10)

        def enterRule():
            	proto_var.get() + " " + source_ip.get() + " " + source_port.get() + " " + direction.get() + " " + destination_ip.get() + " " + destination_port.get() + " " + lastfield.get(otext = action_var.get() + " " +o
proto_var.get() + " " + source_ip.get() + " " + source_port.get() + " " + direction.get() + " " + destination_ip.get() + " " + destination_port.get() + " " + lastfield.get()
                with open('/etc/snort/rules/local.rules','a') as f:
		    try:
			f.write(text)
	            finally:
		        f.close
	        print("Rule is " + text)
	        print("Rule saved to Snort Conf File")

        b = Button(root, text="Save Rule", width=10, command=enterRule,bg='green')
        b.pack(side=BOTTOM)

my_gui = Menu(root)

my_gui.action_options = ["TCP","UDP","ICMP","IP"]
my_gui.action_var.set("IP")
my_gui.action.grid(column=2,row=10)

my_gui.port.grid(column=4,row=10)

my_gui.action_options = ["<-","->","<->"]
my_gui.action_var.set("<->")
my_gui.action.grid(column=5,row=10)

my_gui.ip.grid(column=6,row=10)

my_gui.port.grid(column=6,row=10)

root.mainloop()
