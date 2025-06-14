import tkinter
from tkinter import *


window = Tk()
window.geometry("220x100")

#Labels
euro = Label(text = "€",font = ("Times", 12))
euro.place(x=73,y= 7)

#Text boxex
euroimputent = Entry(window, width=10)
euroimputent.place(x=10,y=10)


dolaroutputent = Entry(window, width=10)
dolaroutputent.place(x=140,y=10)
dolaroutputent.insert(0, "Dollars")

yenoutputent = Entry(window, width=10)
yenoutputent.place(x=140,y=40)
yenoutputent.insert(0, "Yens")

poundsoutputent = Entry(window, width=10)
poundsoutputent.place(x=140,y=70)
poundsoutputent.insert(0, "Pounds")
def convert():
    global euroimputent
    global dolaroutputent
    euroimput = euroimputent.get()
    if euroimput == '':
        euroimput = 0
    dolaroutput = int(euroimput) * 1
    dolaroutputent.delete(0,END)
    dolaroutputent.insert(0,dolaroutput)

    yenoutput = int(euroimput) * 146
    yenoutputent.delete(0,END)
    yenoutputent.insert(0,yenoutput)

    poundoutput = int(euroimput) * 0.87
    poundsoutputent.delete(0,END)
    poundsoutputent.insert(0,poundoutput)

#Buttons
arrow= Button(text="\N{RIGHTWARDS BLACK ARROW}", font = ("Times", 20),command= convert,borderwidth=0,relief=SUNKEN)
arrow.place(x=90,y=-5)



window.title("Here come the money")
window.mainloop()
