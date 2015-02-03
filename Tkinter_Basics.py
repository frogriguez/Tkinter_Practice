"""
I. INTRODUCTION
	It is often necessary to being to communicate with a robot while it is in use. This can be done simply through a remote control or more complexly through a GUI. The GUI can allow the robot to both send an receive information while a remote control will only be able to send to the robot. A simple way to make a GUI is through Python Tkinter. Using Tkinter along with Serial, the code will allow easy communication between the robot. This tutorial will show how to use various parts of Tkinter and show how to make a GUI look good.Taken From: (http://robotic-controls.com/learn/python-guis/basics-tkinter-gui)
	For More Information: (http://www.tutorialspoint.com/python/python_gui_programming.htm)
	"""

#Initializing Tkinter
from tkinter import *
"""Importing the library in this fashion means that when the library is used, it does not have to be called every time. For communication between a robot, it will also be necessary to import the Serial library.
For Example:

	import tkinter

	#you will have to:
	tkinter.Tk()
	tkinter.Button
	tkinter.Canvas
	#etc...
"""

root = Tk() #Makes the window
root.title("Window Title") #Makes the title that will appear in the top left
root.config(background = "#FFFFFF") #sets background color to white

	#put widgets here

#root.mainloop() - start monitoring and updating the GUI. Nothing below here runs.
	
"""
II. Frame
Frames are useful for the organization of a GUI. Frames get built into the grid of the window and then in turn each have a grid of their own. This means that nesting frames may be necessary if the GUI is going to look nice. To add a frame, the following code is needed:
"""
#puts the frame in the main window. height/width specified, but will resize to what's inside
leftFrame = Frame(root, width=200, height = 600)

#Places frame in first grid spot open in root (0,0)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

"""
III. Label
A label allows either text or a picture to be placed. The text inside the label can be updated later if necessary.
"""
#This rests 'label1' in left frame with the following text in the first spot of leftFrame.
label1 = Label(leftFrame, text="This is my first label")
label1.grid(row=0, column=0, padx=10, pady=2)


#To get a picture in the label, use Image:
import Image
pic1 = Image.open(file = 'pic.jpg')
Label(leftFrame, image=pic1).grid(row=0, column=0, padx=10, pady=2)
#The image should be in the same folder that the Python file is in. 

"""
IV. Entry
The Entry widget is an input widget. It allows the user to type something that can then be read into the program.
"""

#rests a spot for a user to type something
userInput = Entry(leftFrame, width = 10) #the width refers to the number of characters
userInput.grid(row=0, column=0, padx=10, pady=2)

#Use the get function to extract the text from userinput
userInput.get()
It may be necessary to get the inside of the entry when a button is pushed or when the user strikes enter.

"""
V. Button
A button causes a specified action to occur.
"""
def function():
	print("Hello!")

#The command specified in the button is a function that will be called when button is pushed.
newButton = Button(leftFrame, text="Okay", command=function)	#fx should be above the button
newButton.grid(row=0, column=0, padx=10, pady=2)

"""
VI. CANVAS
	A canvas allows for various shapes and designs to be drawn onto it. These shapes will remain if more are added unless the shape's pixels are completely overwritten. To draw on the canvas there are a large number of functions available, such as create_arc and create_line.
"""

#rests a canvas in the window:
newCanvas = Canvas(leftFrame, width=100, height=100, bg='white')
newCanvas.grid(row=0, column=0, padx=10, pady=2)

"""
VI. Text
A Text widget can either be written in or can be written to. The Text widget is good for creating logs since the data will remain and the user can look back at it.
"""

#Puts text in window
newText = Text(leftFrame, width=50, height=8, takefocus=0)
newText.grid(row=0, column=0, padx=10, pady=2)

#write to widget
newText.insert(0.0, "Text to insert") #0.0 is beginning of widget












