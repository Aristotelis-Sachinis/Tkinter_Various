from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('ATM')
root.configure(background='black')

m = 1000
c = 0
n = 0


def clear1():
    entr.destroy()
    btn4.destroy()
    btn5.destroy()


def clear2():
    entr2.destroy()
    btn44.destroy()
    btn55.destroy()


def change():
    global m

    if c == 1:
        if entr.get().isdecimal() == True :
            if int(entr.get()) > 0:
                if m >= int(entr.get()):
                    m = m - int(entr.get())
                    messagebox.showinfo('Info', message='Withdraw was successful')
                    menu()
                else:
                    entr.delete(0, 'end')
                    messagebox.showerror('Error', message='You do not have enough money')
        else:
            entr.delete(0, 'end')
            messagebox.showerror('Error', message='Something is wrong')
    elif c == 2:
        if int(entr2.get()) > 0:
            if entr2.get().isdecimal() == True:
                messagebox.showinfo('Info', message='Deposit was successful')
                m = m + int(entr2.get())
                menu()
            else:
                entr2.delete(0, 'end')
                messagebox.showerror('Error', message='Something is wrong')


def withdraw():
    lbl.destroy()
    lbl2.destroy()
    btn.destroy()
    btn2.destroy()
    btn3.destroy()

    global entr
    global btn5
    global btn4
    global c

    c = 1
    entr = Entry(root, font=('Tahoma', 15))
    entr.pack()
    btn4 = Button(root, text='Submit', command=change, fg='white', bg='black', font=('Tahoma', 25))
    btn4.pack()
    btn5 = Button(root, text='Cancel', command=menu, fg='white', bg='black', font=('Tahoma', 25))
    btn5.pack()


def deposit():
    lbl.destroy()
    lbl2.destroy()
    btn.destroy()
    btn2.destroy()
    btn3.destroy()

    global entr2
    global btn55
    global btn44
    global c

    c = 2
    entr2 = Entry(root, font=('Tahoma', 15))
    entr2.pack()
    btn44 = Button(root, text='Submit', command=change, fg='white', bg='black', font=('Tahoma', 25))
    btn44.pack()
    btn55 = Button(root, text='Cancel', command=menu, fg='white', bg='black', font=('Tahoma', 25))
    btn55.pack()


def name():
    global n
    n = entr3.get()
    menu()


def menu():
    global lbl
    global lbl2
    global btn
    global btn2
    global btn3

    if c == 1:
        clear1()
    elif c == 2:
        clear2()
    elif c == 0:
        entr3.destroy()
        lbl7.destroy()
        btn7.destroy()

    lbl = Label(root, text='Hello ' + n, fg='white', bg='black', font=('Tahoma', 25))
    lbl.pack()
    lbl2 = Label(root, text=m, fg='white', bg='black', font=('Tahoma', 25))
    lbl2.pack()
    btn = Button(root, text='Withdraw', command=withdraw, fg='white', bg='black', font=('Tahoma', 25))
    btn.pack()
    btn2 = Button(root, text='Deposit', command=deposit, fg='white', bg='black', font=('Tahoma', 25))
    btn2.pack()
    btn3 = Button(root, text='Exit', command=quit, fg='white', bg='black', font=('Tahoma', 25))
    btn3.pack()


lbl7 = Label(root, text='Whats your name?', fg='white', bg='black', font=('Tahoma', 25))
entr3 = Entry(root, font=('Tahoma', 25))
lbl7.pack()
entr3.pack()
btn7 = Button(root, text='Next', command=name, fg='white', bg='black', font=('Tahoma', 25))
btn7.pack()

root.mainloop()