from tkinter import *

# if you are still working under a Python 2 version,
# comment out the previous line and uncomment the following line
# import Tkinter as tk

window = Tk()
logo = PhotoImage(file="python.gif")
w1 = Label(window, image=logo).pack(side="right")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""

w2 = Label(window,
            justify = LEFT,
            padx = 10,
            text=explanation).pack(side="left")

window.mainloop()
