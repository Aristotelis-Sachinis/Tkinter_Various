from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Survey form")
window.geometry("550x650")
pc1=False
pc2=False
pc3=False
pc4=False
pc5=False

progr =IntVar()
progr.set(0)
bar =Progressbar(window, length=200, style="black.Horizontal.TProgressbar", variable=progr)
bar.grid(column=1, row=0)

def ChangeValue(a):
    global progr, pc1, pc2, pc3, pc4, pc5
    if pc1==False and a==1:
        progr.set(progr.get() +20)
        pc1=True
    if pc2==False and a==2:
        progr.set(progr.get() +20)
        pc2=True
    if pc3==False and a==3:
        progr.set(progr.get() +20)
        pc3=True
    if pc4==False and a==4:
        progr.set(progr.get() +20)
        pc4=True
    if pc5==False and a==5:
        progr.set(progr.get() +20)
        pc5=True

lblq1 = Label(window, text='1) How many programming languages do you know?')
lblq1.grid(column=0, row=2, columnspan=2)
combo1 = Combobox(window)
combo1['values']= (0, 1, 2, 3, 4, "more")
combo1.current()
combo1.grid(column=0, row=3, columnspan=2)
combo1.bind("<<ComboboxSelected>>",lambda event=None: ChangeValue(1))

lblq2 = Label(window, text="2) Which of the following do you know best?")
lblq2.grid(column=0, row=4, columnspan=2)
rb1=StringVar()
rad11 = Radiobutton(window, text='Java', value='Java', variable=rb1,command=lambda:ChangeValue(2))
rad11.grid(column=0, row=5, columnspan=2)
rad12 = Radiobutton(window, text='C++', value='C++', variable=rb1,command=lambda:ChangeValue(2))
rad12.grid(column=0, row=6, columnspan=2)
rad13 = Radiobutton(window, text='Python', value='Python', variable=rb1,command=lambda:ChangeValue(2))
rad13.grid(column=0, row=7, columnspan=2)
rad14 = Radiobutton(window, text='C#', value='C#', variable=rb1,command=lambda:ChangeValue(2))
rad14.grid(column=0, row=8, columnspan=2)
#rb1.trace("w", ChangeValue(2))

lblq3 = Label(window, text="3) Do you like coding?")
lblq3.grid(column=0, row=9, columnspan=2)
rb2=StringVar()
rad21 = Radiobutton(window, text='Yes', value='Yes', variable=rb2,command=lambda:ChangeValue(3))
rad21.grid(column=0, row=10)
rad22 = Radiobutton(window, text='No', value='No', variable=rb2,command=lambda:ChangeValue(3))
rad22.grid(column=1, row=10)
#rb2.trace("w",lambda :  ChangeValue(3))

lblq4 = Label(window, text="4) Which browser do you prefer?")
lblq4.grid(column=0, row=11, columnspan=2)
combo2 = Combobox(window)
combo2['values']= ("Google Chrome", "Mozilla Firefox", "Internet Explorer", "Yahoo", "Bing")
combo2.current()
combo2.grid(column=0, row=12, columnspan=2)
combo2.bind("<<ComboboxSelected>>",lambda event=None: ChangeValue(4))

lblq5 = Label(window, text="5) Which of the above would you like to study?")
lblq5.grid(column=0, row=13, columnspan=2)
rb3=StringVar()
rad31 = Radiobutton(window, text='Coding', value='Coding', variable=rb3,command=lambda:ChangeValue(5))
rad31.grid(column=0, row=14, columnspan=2)
rad32 = Radiobutton(window, text='Robotics', value='Robotics', variable=rb3,command=lambda:ChangeValue(5))
rad32.grid(column=0, row=15, columnspan=2)
rad33 = Radiobutton(window, text='Microsoft Word', value='Microsoft Word', variable=rb3,command=lambda:ChangeValue(5))
rad33.grid(column=0, row=16, columnspan=2)
rad34 = Radiobutton(window, text='Microsoft Excel', value='Microsoft Excel', variable=rb3,command=lambda:ChangeValue(5))
rad34.grid(column=0, row=17, columnspan=2)
rad35 = Radiobutton(window, text='Microsoft PowerPoint', value='Microsoft PowerPoint', variable=rb3,command=lambda:ChangeValue(5))
rad35.grid(column=0, row=18, columnspan=2)
#rb3.trace("w", lambda : ChangeValue(5))

lblfinal1 = Label(window, text="")
lblfinal1.grid(column=0, row=26)
lblfinal2 = Label(window, text="")
lblfinal2.grid(column=0, row=27)
lblfinal3 = Label(window, text="")
lblfinal3.grid(column=0, row=28)
lblfinal4 = Label(window, text="")
lblfinal4.grid(column=0, row=29)
lblfinal5 = Label(window, text="")
lblfinal5.grid(column=0, row=30)

def Check():
    global ansq1
    global ansq4
    global txt
    global txtt
    ansq1 = combo1.get()
    ansq4 = combo2.get()
    txt=""
    txtt=""
    if rb1.get()=="Java":
        txt= " Java"
    elif rb1.get()=="C++":
        txt = " C++"
    elif rb1.get()=="Python":
        txt = " Python"
    elif rb1.get()=="C#":
        txt = " C#"
    else:
        txt="None of the above"
    lblfinal2.configure(text="The language you know best is : "+txt)

    if rb3.get()=='Coding':
        txtt= txtt + " Coding"
    elif rb3.get()=='Robotics':
        txtt = " Robotics"
    elif rb3.get()=='Microsoft Word':
        txtt = " Microsoft Word"
    elif rb3.get()== 'Microsoft Excel':
        txtt = " Microsoft Excel"
    elif rb3.get()=="Microsoft PowerPoint":
        txtt = " Microsoft PowerPoint"
    else:
        txtt = "You didn't answer Q5."
    lblfinal5.configure(text="You would like to study: "+txtt)

    lblfinal1.configure(text="You know "+ str(ansq1) + " different programming languages")
    lblfinal4.configure(text="For browsing you prefer: "+ str(ansq4))

    if rb2.get()=="Yes":
        lblfinal3.configure(text="You like coding")
    elif rb2.get()=="No":
        lblfinal3.configure(text="You don't like coding")
    else:
        lblfinal3.configure(text="You didn't answer Q3.")

btn = Button(window, text="Submit", command=Check)
btn.grid(column=1, row=24)


window.mainloop()