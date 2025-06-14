from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

window = Tk()
window.title("Progress Bar")
window.geometry("330x100")

progr = IntVar()
progr.set(0)

def ChangeValue(num):
    global progr
    if num == 10 and progr.get() < 100 or num == -10 and progr.get() > 0:
        progr.set(progr.get() + num)
        print(progr.get())
        
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(window, length=200, style="black.Horizontal.TProgressbar", variable=progr)
bar.grid(column=1, row=0)

btn = Button(window, text='+10', command=lambda: ChangeValue(10))
btn.grid(column=0, row=1)

btn2 = Button(window, text='-10', command=lambda: ChangeValue(-10))
btn2.grid(column=2, row=1)

window.mainloop()