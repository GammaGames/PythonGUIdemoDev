# *************************************************************
# PROJECT: FindBestStudent
#
# FILE:	  testStudent.py
#
# DEVELOPMENT ENVIRONMENTS:
# PyCharm Comm 2.7.11
#
# EXECUTION ENVIRIONMENTS
# PyCharm Comm 2.7.11
#
# HISTORY:
# Date		Author			Description
# ====		======			===========
# 08/07/16	F. Ackerman		Standards example
#
# DESCRIPTION
# Tests the class "Student" requirements
# **************************************************************

# ---------------
# Python imports
# ---------------
import Tkinter
import tkMessageBox
from Tkinter import *
import string

# --------------------
# Application imports
# --------------------
#http://www.tutorialspoint.com/python

def buttonTest(str):
    tkMessageBox.showinfo("Test", str)

def main():
    window = Tkinter.Tk("test")

    button = Tkinter.Button(window, text = "confirm", command = buttonTest("aa"))
    button.pack(side = RIGHT)

    field = Entry(window)
    field.pack(side = LEFT)

    window.mainloop()
# def main()

main()

# end PythonGUIdemo.py