#*************************************************************
# PROJECT: PythonGUIdemoDev
#
# FILE:	   PythonGUIdemoDev.py
#
# PYTHON VERSION: 2.7
#
# HISTORY:
# Date		Author			Description
# ====		======			===========
# 09/1/16   Jesse Lieberg   Initial writing and MTM Standard
# 09/2/16   Logan Warner    Standards compliance cleanup
# 09/12/16	Jesse & Logan	Standards compliance
#
# DESCRIPTION:
# Creates a test GUI
#**************************************************************

#---------------
# Python imports
#---------------
import Tkinter
import tkMessageBox
from Tkinter import *


#---------------
# Local Functions
#---------------
def buttonTest(check, str):
    """
    Displays message with text
    """
    if check:
        tkMessageBox.showinfo("Test", str)
    else:
        tkMessageBox.showinfo("Test", "Hello world!")
    # else
# def buttonTest()


def main():
    """
    Create a test GUI with various options
    ----------------------------------------------------
	REQUIREMENTS:
	R01.
	
	DESIGN
	Algorithm
	---------
	A01 Create small, fixed window titled "Test"
	A02
	----------------------------------------------------"""
    window = Tkinter.Tk("test")							#L01
    window.wm_title("Test")
    window.resizable(width = False, height = False)
    window.minsize(width = 200, height = 64)

    # Variables used for checkbox
    checkVar = BooleanVar()
    checkButton = Checkbutton(window, text = "Show field text?", variable = checkVar)

    # Create a label and field for entering text
    fieldLabel = Label(window, text = "Message:")
    field = Entry(window)

    # create button that calls the function buttonTest when pressed
    button = Tkinter.Button(window, text = "Display message", command = lambda: \
      buttonTest(checkVar.get(), field.get()), cursor = "hand2")

    # Configure grid to center elements
    window.grid_columnconfigure(0, weight = 1)
    window.grid_columnconfigure(1, weight = 1)

    # Add GUI elements to the window in a grid layout
    fieldLabel.grid(row = 0, column = 0, sticky = E)
    field.grid(row = 0, column = 1, sticky = W)
    checkButton.grid(row = 1, columnspan = 2)
    button.grid(row = 2, columnspan = 2)

    window.mainloop()
# def main()

main()

# end PythonGUIdemo.py
