from tkinter import *

window = Tk()

def convert():
    kg = float(e1_val.get())
    g = 1000 * kg
    lb = kg / .453592
    t3.insert(END, g)
    t4.insert(END, lb)


b1 = Button(window, text="Convert!", command = convert)
b1.grid(row=2, column=0)

t0 = Text(window, height=1, width=20)
t0.insert(END, "Kilograms")
t0.grid(row = 0, column = 0)

t1 = Text(window, height=1, width=20)
t1.insert(END, "Grams")
t1.grid(row = 0, column = 1)

t2 = Text(window, height=1, width=20)
t2.insert(END, "Pounds")
t2.grid(row = 0, column = 2)

e1_val = StringVar()
e1 = Entry(window, textvariable = e1_val)
e1.grid(row = 1, column = 0)

t3 = Text(window, height=1, width=20)
t3.grid(row = 1, column = 1)

t4 = Text(window, height=1, width=20)
t4.grid(row = 1, column = 2)

window.mainloop()
