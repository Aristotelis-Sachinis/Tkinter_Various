from tkinter import *
import random
import time
s = 0
timeleft=30
def startGame(event):
    if timeleft == 30:
        countdown()
def place():
    global s
    s += 1
    btn.place(x=random.randint(20,400), y=random.randint(100,400))
    lbl3.configure(text="Score: "+str(s))
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        lbl1.config(text="Time" + str(timeleft))
        lbl1.after(1000, countdown)
window = Tk()
window.title("Welcome")
lbl0 = Label(window,text="Click the moving btn",fg='red',bg='dark blue',font=('Helvetica',25))
lbl0.place(x=105,y=20)
btn = Button(window,text="Click me", command=place)
btn.place(x=20,y=100)
lbl1 = Label(window,text="Time",font=('Helvetica',15))
lbl1.place(x=20,y=460)
lbl3 = Label(window,text="Score: 0",font=('Helvetica',15))
lbl3.place(x=405,y=460)
window.bind('<Return>', startGame)
window.geometry("500x500")
window.mainloop()