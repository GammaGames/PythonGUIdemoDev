#*************************************************************
# PROJECT: PythonGUIdemoDev
#
# FILE:	   PythonGUIdemoDev.py
#
# DEVELOPMENT ENVIRONMENTS:
# PyCharm Comm 2016.2.1
#
# EXECUTION ENVIRIONMENTS:
# PyCharm Comm 2016.2.1
#
# HISTORY:
# Date		Author			Description
# ====		======			===========
# 09/1/16   Jesse Lieberg   Initial writing and MTM Standard
# 09/2/16   Logan Warner    Standards compliance cleanup
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
    """
    # Create main window for test application to display to
    window = Tkinter.Tk("test")
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
