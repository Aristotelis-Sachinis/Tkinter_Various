import sys
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
from math import sqrt
screen = ThemedTk(theme = "equilux")
screen.configure(themebg = "equilux")
screen.geometry("340x320")

UI = ttk.Entry(screen,width=30,font=('Times' , 15))
UI.grid(column=0,row=0,columnspan=7)

#Defs
def Clear(event=0):
    UI.delete('0' , END)
def press(num):
    num = str(num)
    UI.insert(INSERT,num)
def Evaluate(event=0):
    try:
        fraction = UI.get()
        result = str(eval(fraction))
        UI.delete('0' , END)
        UI.insert(INSERT , result)
    except:
        UI.delete('0' , END)
        UI.insert(INSERT , "error")

def end2(event=0):
    UI.delete(END,"1")
    UI.delete(len(UI.get())-1, END)

def  Add_commas(event=0):
    try:
        fraction = UI.get()
        fraction = "{:,}".format(int(fraction))
        UI.delete('0' , END)
        UI.insert(INSERT , fraction)
    except:
        print()

#Buttons
button_1 = ttk.Button(text="1",command=lambda: press("1"))
button_1.grid(column=1,row=1)
button_2 = ttk.Button(text="2",command=lambda: press("2"))
button_2.grid(column=2,row=1)
button_3 = ttk.Button(text="3",command=lambda: press("3"))
button_3.grid(column=3,row=1)
button_4 = ttk.Button(text="4",command=lambda: press("4"))
button_4.grid(column=1,row=2)
button_5 = ttk.Button(text="5",command=lambda: press("5"))
button_5.grid(column=2,row=2)
button_6 = ttk.Button(text="6",command=lambda: press("6"))
button_6.grid(column=3,row=2)
button_7 = ttk.Button(text="7",command=lambda: press("7"))
button_7.grid(column=1,row=3)
button_8 = ttk.Button(text="8",command=lambda: press("8"))
button_8.grid(column=2,row=3)
button_9 = ttk.Button(text="9",command=lambda: press("9"))
button_9.grid(column=3,row=3)
button_0 = ttk.Button(text="0",command=lambda: press("0"))
button_0.grid(column=2,row=4)
button_dot = ttk.Button(text=".",command=lambda: press("."))
button_dot.grid(column=1,row=4)

button_add = ttk.Button(text="+",command=lambda: press("+"))
button_add.grid(column=4,row=2)

button_subtract = ttk.Button(text="-",command=lambda: press("-"))
button_subtract.grid(column=4,row=3)

button_multiply= ttk.Button(text="*",command=lambda: press("*"))
button_multiply.grid(column=4,row=4)

button_divide= ttk.Button(text="/",command=lambda: press("/"))
button_divide.grid(column=4,row=5)

button_in_power= ttk.Button(text="**",command=lambda: press("**"))
button_in_power.grid(column=1,row=5)

button_root= ttk.Button(text="√",command=lambda: press("sqrt("))
button_root.grid(column=2,row=5)

button_equals= ttk.Button(text="=",command= Evaluate)
button_equals.grid(column=3,row=5)

button_close_parenthesis= ttk.Button(text=")",command=lambda: press(")"))
button_close_parenthesis.grid(column=2,row=6)

button_open_parenthesis= ttk.Button(text="(",command=lambda: press("("))
button_open_parenthesis.grid(column=1,row=6)

button_del_recent= ttk.Button(text="X",command = end2)
button_del_recent.grid(column=4,row=1)

button_clear = ttk.Button(text="C",command = Clear)
button_clear.grid(column=3,row=4)

button_add_commas = ttk.Button(text="Comma",command = Add_commas)
button_add_commas.grid(column=3,row=6)

logo = PhotoImage(file="calculator/logo.png")
label2 = Label(screen, image=logo, bg='#464646')
label2.grid(column=1,row=8,columnspan=4,pady=20)

screen.title("Calculator")
screen.mainloop()
