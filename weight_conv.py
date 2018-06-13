from tkinter import *

window = Tk()

def convert():
    kg = float(e1_val.get())
    g = 1000 * kg
    lb = kg / .453592
    grams.configure(text = str(g) + ' g')
    pounds.configure(text = '%6.2f lb' % lb)

b1 = Button(window, text="Convert", command = convert)
b1.grid(row=2, column=0)

b2 = Button(window, text="Quit", command = window.quit)
b2.grid(row=2, column=2)

l0 = Label(window, height=1, width=20)
l0.configure(text = "Enter weight in kilograms:")
l0.grid(row = 0, column = 0)

e1_val = StringVar()
e1 = Entry(window, textvariable = e1_val)
e1.bind("<Return>", (lambda event: convert()))
e1.grid(row = 1, column = 0)

grams = Label(window, height=1, width=20)
grams.grid(row = 1, column = 1)

pounds = Label(window, height=1, width=20)
pounds.grid(row = 1, column = 2)

window.mainloop()
