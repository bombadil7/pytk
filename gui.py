from tkinter import *

#Create empty window
window = Tk()

def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get()) * 1.60934
    t1.insert(END, miles)

b1 = Button(window, text="Convert to Miles", command=km_to_miles)
b1.grid(row=0, column=0)
#b1.pack()

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()  #Goes to the end of the code
