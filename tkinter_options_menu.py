"""
The Tkinter OptionMenu Widget
The OptionMenu class is a helper class that creates a popup menu, and a button to display it. The option menu is similar to the combobox widgets commonly used on Windows. To get the currently selected value from an option menu, you have to pass in a Tkinter variable.
"""

#initializing Tkinter
from tkinter import *



master = Tk()




"""
Option Menu: To create an option menu, call the OptionMenu class constructor, and pass in the variable and a list of options. To get the selected option, use get on the variable. 
"""

def print_option():
    print ("value is", default.get())
    master.quit()

#sets the default value
default = StringVar(master)
default.set("None")


#Create option menu by passing arguments
option = OptionMenu(master, default,"option1","option2","option3")


#Or Create option Menu from a list of options:
OPTIONS = ["egg","bunny","chicken"]
default = StringVar(master)
default.set(OPTIONS[0])

#Use the command: *list to unpack a list
option = OptionMenu(master, default, *OPTIONS)
option.pack()


#Not sure
button = Button(master, text="Print", command=print_option)
button.pack()

mainloop()
