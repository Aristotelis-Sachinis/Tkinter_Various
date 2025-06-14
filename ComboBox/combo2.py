from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to IT Experts")
window.geometry('350x200')

selected = '2'

def GetCombo():
    global selected
    selected = combo.get()
    
    print(selected)


combo = Combobox(window)
combo['values'] = (1,2,'Python', 4, 5, 'Programming')
combo.current(1)
combo.grid(column=0, row=0)

btn = Button(window, text="Select", command=GetCombo)
btn.grid(column=1,row=0)

btn2 = Button(window, text="Print", command=lambda: lbl.configure(text=selected))
btn2.grid(column=1,row=1)

lbl = Label(window, text=selected)
lbl.grid(column=0,row=1)

window.mainloop()