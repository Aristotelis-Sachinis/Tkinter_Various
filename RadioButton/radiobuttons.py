from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to IT Experts!")
window.geometry("350x200")

def Change(*args):
    lbl.configure(text="Selected "+rb.get()+" button!")

rb = StringVar()
rb.trace("w", Change)

rad1 = Radiobutton(window, text="First", value="First", variable=rb)
rad1.grid(column=0, row=0)

rad2 = Radiobutton(window, text="Second", value="Second", variable=rb)
rad2.grid(column=1,row=0)

rad3 = Radiobutton(window, text="Third", value="Third", variable=rb)
rad3.grid(column=2, row=0)

lbl = Label(window, text="Selected "+rb.get()+" button!")
lbl.grid(column=1,row=1)

window.mainloop() 
