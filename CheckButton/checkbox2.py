from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome")

conclusion = "The checkbutton was not checked"

def Check(*args):
    global conclusion
    
    if chk_state.get():
        conclusion="The checkbutton was checked"
    else:
        conclusion = "The checkbutton was not checked"

    lbl.configure(text=conclusion)

chk_state=BooleanVar()
chk_state.set(False)
chk_state.trace("w", Check)
chk=Checkbutton(window, text="Interested", var=chk_state)
chk.pack()

lbl = Label(window, text=conclusion)
lbl.pack()

window.geometry("400x400")
window.mainloop()