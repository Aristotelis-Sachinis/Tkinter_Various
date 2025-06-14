import tkinter
from tkinter import *
from tkinter.ttk import *
from  tkinter import ttk
window = Tk()
window.geometry("300x250")
question_amount = 6
redstyle = ttk.Style()
redstyle.configure("Red.TCheckbutton", foreground="red")
greenstyle = ttk.Style()
greenstyle.configure("Green.TCheckbutton", foreground="green")
redstylecmb = ttk.Style()
redstylecmb.configure("Red.TCombobox", foreground="red")
greenstylecmb = ttk.Style()
greenstylecmb.configure("Green.TCombobox", foreground="green")
#Defs
def Submit(event=0):
    global q1_check_state,q2_check_state,q3_check_state,q4_check_state,question_amount,question5comb,question6comb
    if q1_check_state.get() == False:
        q1score = 100 / question_amount
        question1chk.configure(style="Green.TCheckbutton")
    else:
        q1score = 0
        question1chk.configure(style="Red.TCheckbutton")
    if q2_check_state.get() == True:
        q2score= 100 / question_amount
        question2chk.configure(style="Green.TCheckbutton")
    else:
        q2score = 0
        question2chk.configure(style="Red.TCheckbutton")
    if q3_check_state.get() == True:
        q3score=100 / question_amount
        question3chk.configure(style="Green.TCheckbutton")
    else:
        q3score = 0
        question3chk.configure(style="Red.TCheckbutton")
    if q4_check_state.get() == False:
        q4score=100 / question_amount
        question4chk.configure(style="Green.TCheckbutton")
    else:
        q4score = 0
        question4chk.configure(style="Red.TCheckbutton")
    if question5comb.get() == "Let the bodies flow":
        q5score = 100 / question_amount
        question5comb.configure(style="Green.TCombobox")
    else:
        q5score = 0
        question5comb.configure(style="Red.TCombobox")
    if question6comb.get() == "Selling organs":
        q6score = 100 / question_amount
        question6comb.configure(style="Green.TCombobox")
    else:
        q6score = 0
        question6comb.configure(style="Red.TCombobox")
    #Doing the %
    score = q1score + q2score + q3score + q4score + q5score + q6score
    score = round(score)
    Scorelbl.configure(text = "Your score is"+" "+str(score)+ "%")
    Scorelbl.place(x=50,y=230)

#Labels
Titlelbl = tkinter.Label(window,text= "Rimworld quiz",state="active")
Titlelbl.place(x=115,y=10)
Scorelbl = tkinter.Label(window,text= "Results",state="active")

#Buttons
Fintbtn = tkinter.Button(window,text= "Submit",command= Submit)
Fintbtn.place(x=0,y=225)

#Checkboxes
q1_check_state = BooleanVar()
q1_check_state.set(False)
q2_check_state = BooleanVar()
q2_check_state.set(False)
q3_check_state = BooleanVar()
q3_check_state.set(False)
q4_check_state = BooleanVar()
q4_check_state.set(False)
question1chk = Checkbutton(window,text= "Are warcrimes illigal?", var = q1_check_state)
question1chk.place(x=10,y=40)

question2chk = Checkbutton(window,text= "Sould you have your slaves?", var = q2_check_state)
question2chk.place(x=10,y=60)

question3chk = Checkbutton(window,text= "Should you sell drugs on the black market?", var = q3_check_state)
question3chk.place(x=10,y=80)

question4chk = Checkbutton(window,text= "Sould you follow the geniva convention?", var = q4_check_state)
question4chk.place(x=10,y=100)

#Comboboxes

#   i) Comboboxes def

def updt1(event=None):
    choise = question5comb.get()
def updt2(event=None):
    choise = question5comb.get()

#    ii) Comboboxes Things

question5comb = Combobox(window,state="readonly",width=34)
question5comb ["values"] = ("Let the bodies flow","I don't care about it","It's illegal")
question5comb.bind("<<ComboboxSelected>>",lambda e: window.focus())
question5comb.set("What are your views on kidnapping?")
question5comb.place(x=10,y=120)

question6comb = Combobox(window,state="readonly",width=34)
question6comb ["values"] = ("Selling minerals","Selling organs","Selling food produce")
question6comb.bind("<<ComboboxSelected>>" ,lambda e: window.focus())
question6comb.set("In what way sould you make money?")
question6comb.place(x=10,y=160)

window.title("Rimworld quiz time")
window.mainloop()
