from tkinter import *

#Create empty window
window = Tk()

b1 = Button(window, text="Press Me")
b1.grid(row=0, column=0)
#b1.pack()

e1 = Entry(window)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()  #Goes to the end of the code
