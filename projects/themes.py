from tkinter import *
#from tkinter.ttk import *
window = Tk()
window.geometry("200x100")
global theme
theme = "white"
print(theme)
def Change_Theme(*args):
    global theme
    print(theme)
    if theme == "black":
        theme = "white"
        not_Theme = "black"
    else:
        theme = "black"
        not_Theme = "white"
    Theme_lbl.configure(bg=theme,fg=not_Theme)
    check_button.configure(bg = theme,fg=not_Theme)
    window.configure(bg=theme)
check_state = BooleanVar()
check_state.set(False)
check_state.trace("w",Change_Theme)
check_button = Checkbutton(window,text= "To see or not to see?", var = check_state, bg = theme)
check_button.place(x=0,y=0)
Theme_lbl = Label(window,text ="Test text please ignore",bg = theme)
Theme_lbl.place(x=0,y=80)
window.title("Welcome")
window.mainloop()
