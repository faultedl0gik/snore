# snore
# Author: Daniel Brown
This program is designed to be a snort rule manager. Currently it can add rules and view rules (Although the view option is kind of wonky).
You simply run the program and then enter the rule and click the 'save' button. It will append the rule, it will not overwrite currently
stored rules. 
This tool is based on Tkinter Widgest using python classes. You can add and subtract modules to change the layout of the buttons, labels, and entry fields.

# CHANGING RULE FILE LOCATION:
To change the file location of the rules go to line 20 "f = open(path)" and line 148 "with open(path)"  and change the location to the rule file that you would like to alter.

# This tool is a work in progress!! Future features will include the ability to delete rules, and better file location specification ability.
