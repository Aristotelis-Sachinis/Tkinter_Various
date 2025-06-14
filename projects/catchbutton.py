import time
import tkinter
from tkinter import *
from random import *

window = Tk()
window.geometry("800x800")
score = 0
timeer = 0
def clicked():
    global score
    button.place_configure(x = randint(10,750) ,y = randint(10,760))
    score += 1
    scoring.configure(text = "Your score is"+" "+ str(score))
    print(timeer)
def quiting():
    quit()
def timer_update():
    global timeer
    timeer += 1
    timer.configure(text = str(timeer))
button = tkinter.Button(window, text = "1$", width=10,height=1, bg = "green",cursor = "dotbox" ,command = clicked)
quitB = tkinter.Button(window, text = "Quit", width=10,height=2, command = quiting)
timer = Label(window, text = timeer)
timer.after(1000,timer_update())
timer.place(x=0, y =0)
quitB.place(x=0,y=760)
scoring = tkinter.Label(window, text = "Your score is"+" "+ str(score))
timer_update()
scoring.place(x = 400,y =10)
button.place(x = 400, y = 400)
window.title("Catch the button")
window.mainloop()
