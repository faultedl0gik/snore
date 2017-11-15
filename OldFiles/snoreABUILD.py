#!/usr/bin/python
#Authors: 1LT Daniel Brown
#         SGT Matlock
#Purpose: Designed to allow error free snort rule entry for non 
#technical personnel.
#############################

from Tkinter import *

root = Tk()
root.geometry("700x100")
root.title("Snore")
root.pack_propagate(False)

#DropMenu_Action
action_options = ["Alert","Log","Pass","Active","Dynamic","Drop","Reject","sdrop"]
action_var=StringVar()
action_var.set("Alert")
action = OptionMenu(root, action_var, *action_options)
action.grid(column=1,row=10)

#DropMenu_Protocol
proto_options = ["TCP","UDP","ICMP","IP"]
proto_var=StringVar()
proto_var.set("IP")
proto = OptionMenu(root, proto_var, *proto_options)
proto.grid(column=2,row=10)

#InputBlock_SOURCE_IPAddress
source_ip = Entry(root,width=10,bg='light blue')
source_ip.grid(column=3,row=10)

#InputBlock_SOURCE_Port
source_port = Entry(root,width=5,bg='sea green')
source_port.grid(column=4,row=10)

#DropMenu_Direction
direction_options = ["<-","->","<->"]
direction_var=StringVar()
direction_var.set("<->")
direction = OptionMenu(root, direction_var, *direction_options)
direction.grid(column=5,row=10)

#InputBlock_DESTINATION_IPAddress
destination_ip = Entry(root,width=10,bg='light blue')
destination_ip.grid(column=6,row=10)

#InputBlock_DESTINATION_Port
destination_port = Entry(root,width=5,bg='sea green')
destination_port.grid(column=7,row=10)

#InputBlock_LastField
lastfield = Entry(root,width=50,bg='slate gray')
lastfield.grid(column=8,row=10)

def enterRule():
	text = action_var.get() + " " + proto_var.get() + " " + source_ip.get() + " " + source_port.get() + " " + direction.get() + " " + destination_ip.get() + " " + destination_port.get() + " " + lastfield.get()
	with open('/etc/snort/rules/local.rules','a') as f:
		try:
			f.write(text)
	        finally:
		    f.close
	print("Rule is " + text)
	print("Rule saved to Snort Conf File")

b = Button(root, text="Save Rule", width=10, command=enterRule,bg='green')
b.pack(side=BOTTOM)

root.mainloop()	
