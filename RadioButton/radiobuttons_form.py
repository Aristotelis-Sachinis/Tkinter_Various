from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to IT Experts!")

def PrintText(*args):
    lblFinal.configure(text="My name is " + rb1.get() + "\nI am from " + rb2.get() + "\nI am from " + rb3.get())

#Radiobutton Variables
rb1 = StringVar()
rb2 = StringVar()
rb3 = StringVar()
rb1.trace("w", lambda *args: lbl1.configure(text="My name is "+rb1.get()))
rb2.trace("w", lambda *args: lbl2.configure(text="I live in "+rb2.get()))
rb3.trace("w", lambda *args: lbl3.configure(text="I am "+rb3.get()+" years old"))

#Labels
lbl1 = Label(window, text="My name is ")
lbl1.grid(column=0,row=0,padx=10,pady=20)

lbl2 = Label(window, text="I live in ")
lbl2.grid(column=0,row=1,padx=10,pady=20)

lbl3 = Label(window, text="I am ? years old")
lbl3.grid(column=0,row=2,padx=10,pady=20)

lblFinal = Label(window, text="")
lblFinal.grid(column=0,row=3, pady=20,columnspan=3)

#Radiobuttons
rad_name_1 = Radiobutton(window, text="Mark", value="Mark", variable=rb1)
rad_name_2 = Radiobutton(window, text="Mpampis", value="Mpampis", variable=rb1)

rad_city_1 = Radiobutton(window, text="Athens", value="Athens", variable=rb2)
rad_city_2 = Radiobutton(window, text="Havana", value="Havana", variable=rb2)

rad_age_1 = Radiobutton(window, text="23", value="23", variable=rb3)
rad_age_2 = Radiobutton(window, text="36", value="36", variable=rb3)

rad_name_1.grid(column=1,row=0)
rad_name_2.grid(column=2,row=0)

rad_city_1.grid(column=1,row=1)
rad_city_2.grid(column=2,row=1)

rad_age_1.grid(column=1,row=2)
rad_age_2.grid(column=2,row=2)

#Button
btn = Button(window, text="Print \nText", command=PrintText)
btn.grid(column=3, row=1)

window.mainloop()