"""
Using the BUTTON widget in Tkinter: The Button widget is used to add buttons in a Python application. These buttons can display text or images that convey the purpose of the buttons. You can attach a function or a method to a button which is called automatically when you click the button.
"""
#Initialize Tkinter
from tkinter import *
import messagebox

#create Widget Grid (gui) named "gui"
gui = Tk()
gui.title("Coalescent Parameters") #grid title


Label(gui, text="Ne:").grid(row=0)  #Labels entry1: "Ne"
Label(gui, text="k:").grid(row=1)   #Lables entry2: "k"

#defines user entry spots
e1 = Entry(gui)
e2 = Entry(gui)
e1.grid(row=0, column=1) #puts an Ne entry spot in 0,1
e2.grid(row=1, column=1) #puts a k entry spot in 1,1

#Makes buttons
Button(gui, text='Quit', command=gui.quit).grid(row=3, column=1, sticky=W, pady=4)  #Creates a quit button
Button(gui, text='Graph', command=simulation).grid(row=3, column=2, sticky=W, pady=4)  #creates a graph button, executes simulation function on press

#creates figure frame
frame=Frame(gui)
frame.grid(row=0,rowspan=5, column=3)
f = plot(figsize=(6,5), dpi=100)

#Plots figure (graph) into gui
canvas = FigureCanvasTkAgg(f, master=frame)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
gui.mainloop( )