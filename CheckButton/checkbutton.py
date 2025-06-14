from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to IT Experts!")
window.geometry("350x200")

chk_state = BooleanVar()
chk_state.set(True)

chk_intstate = IntVar()
chk_intstate.set(0)

chk = Checkbutton(window, text="Check Boolean", var=chk_state)
chk.grid(column=0,row=0)

chk2 = Checkbutton(window,text="Check Int", var=chk_intstate)
chk2.grid(column=1,row=0)

window.mainloop()