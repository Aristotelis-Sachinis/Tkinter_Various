from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Welcome to IT Experts")

window.geometry('350x200')

combo = Combobox(window)

combo['values'] = (1,2,'Python', 4, 5, 'Programming')

combo.current(1)

combo.grid(column=0, row=0)

window.mainloop()