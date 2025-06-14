from tkinter import *

result = 0
window = Tk()
window.geometry("300x156")

n1lbl = Label(window, text = "First number")
n1lbl.place(x = 0,y= 10)
n2lbl = Label(window, text = "Second number")
n2lbl.place(x = 0,y= 40)
resultlbl = n1lbl = Label(window, text = "Result")
resultlbl.place(x = 0,y=90)

global n1ent
n1ent = Entry(window,width=15)
n1ent.place(x=100,y= 10)
global n2ent
n2ent = Entry(window,width=15)
n2ent.place(x = 100,y= 40)


resultent = Entry(window,width=15)
resultent.place(x= 100,y =90)
resultent.config(state=DISABLED)
def addition():
    no1 = n1ent.get()
    if no1 == '':
        no1 = 0
    no2 = n2ent.get()
    if no2 == '':
        no2 = 0
    result = int(no1) + int(no2)
    resultent.config(state=NORMAL)
    resultent.delete("-1","end")
    resultent.insert(0, result)
    resultent.config(state=DISABLED)
def subtract():
    no1 = n1ent.get()
    if no1 == '':
        no1 = 0
    no2 = n2ent.get()
    if no2 == '':
        no2 = 0
    result = int(no1) - int(no2)
    resultent.config(state=NORMAL)
    resultent.delete("-1","end")
    resultent.insert(0, result)
    resultent.config(state=DISABLED)
def multiply():
    no1 = n1ent.get()
    if no1 == '':
        no1 = 0
    no2 = n2ent.get()
    if no2 == '':
        no2 = 0
    result = int(no1) * int(no2)
    resultent.config(state=NORMAL)
    resultent.delete("-1","end")
    resultent.insert(0, result)
    resultent.config(state=DISABLED)
def divide():
    no1 = n1ent.get()
    if no1 == '':
        no1 = 0
    no2 = n2ent.get()
    if no2 == '':
        no2 = 1
    elif no2 == '0':
        no2 = 1
    result = int(no1) / int(no2)
    resultent.config(state=NORMAL)
    resultent.delete("-1","end")
    resultent.insert(0, result)
    resultent.config(state=DISABLED)
def powerup():
    no1 = n1ent.get()
    if no1 == '':
        no1 = 0
    no2 = n2ent.get()
    if no2 == '':
        no2 = 0
    result = int(no1) ** int(no2)
    resultent.config(state=NORMAL)
    resultent.delete("-1","end")
    resultent.insert(0, result)
    resultent.config(state=DISABLED)
def clear():
    global n1ent
    global n2ent
    n1ent.delete("0",END)
    n2ent.delete("0",END)
    resultent.config(state=NORMAL)
    resultent.delete("-1","end")
    resultent.config(state=DISABLED)
#Buttons
additivebtn = Button(window, text = "Add", width=10,height=1,command = addition)
additivebtn.place(x=225,y=10)
subtractionbtn = Button(window, text = "Subtract", width=10,height=1,command = subtract)
subtractionbtn.place(x=225,y=50)
multiplicationbtn = Button(window, text = "Multiply", width=10,height=1,command = multiply)
multiplicationbtn.place(x=225,y=90)
divisionbtn = Button(window, text = "Divide", width=10,height=1,command = divide)
divisionbtn.place(x=225,y=130)
powerbtn = Button(window, text = "Power up", width=10,height=1,command = powerup)
powerbtn.place(x=75,y=130)

clearbtn = Button(window, text = "Clear", width=10,height=1,command = clear)
clearbtn.place(x=0,y=130)



window.title("Simple Calculuse")
window.mainloop()
