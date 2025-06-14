from tkinter import *
from tkinter import messagebox
from tkinter import Radiobutton
from tkinter.ttk import *
import tkinter.ttk as ttk
import tkinter as tk
import random

root = Tk()
root.configure(background='black')
root.geometry('600x600')
name = ''
a = 30
b = 0
d = 0
c = 0
z = 0
ii = 0
j = 0
ll = 0
k = 0
p = 0

list = [
           'Who is the most followed on Instagram', '1.Madonna', '2.Cristiano Ronaldo', '3.Dwayne Johnson',
           '4.Akis Petretzikis',
           '2'] \
    , ['Which one is the toughest material', '1.Diamond', '2.Granite', '3.Gold', '4.Silver', '1'] \
    , [
           'Who was the MVP in NBA season 19-20', '1.Lebron James', '2.Michael Jordan', '3.Giannis Antentokoumpo',
           '4.Basilis Spanoulis',
           '3'] \
    , [
           'Who is the prime minister of Greece', '1.Alexis Tsipras', '2.Andreas Papadreou', '3.Giannis Varoufakis',
           '4.Kyriakos Mitsotaskis',
           '4'] \
    , ['When did Greece win the Euro', '1.2020', '2.1897', '3.2004', '4.2048', '3']


def back():
    global btn5, btn4, btn6, z
    z = 1
    btn4 = tk.Button(text='Go Back', command=menu, fg='white', bg='black', font=('Tahoma', 25))
    btn4.pack()
    btn5 = tk.Button(text='Play Again', command=color_game, fg='white', bg='black', font=('Tahoma', 25))
    btn5.pack()
    btn6 = tk.Button(text='Exit', command=quit, fg='white', bg='black', font=('Tahoma', 25))
    btn6.pack()


def back2():
    global btn5, btn4, btn6, z, p
    z = 2
    p = 1
    btn4 = tk.Button(text='Go Back', command=menu, fg='white', bg='black', font=('Tahoma', 25))
    btn4.pack()
    btn5 = tk.Button(text='Play Again', command=quiz_game, fg='white', bg='black', font=('Tahoma', 25))
    btn5.pack()
    btn6 = tk.Button(text='Exit', command=quit, fg='white', bg='black', font=('Tahoma', 25))
    btn6.pack()


def quiz_game():
    root.title('Quiz Game')
    global z, a, ii, rb1, rb22, rb33, rb44, k, j, ll, p
    if z == 0:
        btn2.destroy()
        btn.destroy()
        lbl2.destroy()
        lbl8.destroy()
        btn66.destroy()
        label.destroy()
    elif z == 2:
        rb1.destroy()
        rb22.destroy()
        rb33.destroy()
        rb44.destroy()
        lbl2.destroy()
        lbl100.destroy()
        lbl11.destroy()
        bar.destroy()
        btn4.destroy()
        btn5.destroy()
        btn6.destroy()

    z = 0
    ii = 0
    j = 0
    ll = 0
    k = 0

    list = [
               'Who is the most followed on Instagram', '1.Madonna', '2.Cristiano Ronaldo', '3.Dwayne Johnson',
               '4.Akis Petretzikis',
               '2'] \
        , ['Which one is the toughest material', '1.Diamond', '2.Granite', '3.Gold', '4.Silver', '1'] \
        , [
               'Who was the MVP in NBA season 19-20', '1.Lebron James', '2.Michael Jordan', '3.Giannis Antentokoumpo',
               '4.Basilis Spanoulis',
               '3'] \
        , [
               'Who is the prime minister of Greece', '1.Alexis Tsipras', '2.Andreas Papadreou', '3.Giannis Varoufakis',
               '4.Kyriakos Mitsotaskis',
               '4'] \
        , ['When did Greece win the Euro', '1.2020', '2.1897', '3.2004', '4.2048', '3']

    def check(*args):
        global list, ii, j, k, answer, rb1, rb22, rb33, rb44, ll, p, lbl11, lbl100
        if ll == 0:
            j, k = 0, 0
            ll += 1
        if answer.get() == str(list[ii][5]):
            j += 1
            lbl100.configure(text='Correct:' + str(j))
            lbl100.update()
        else:
            k += 1
            lbl11.configure(text='Wrong:' + str(k))
            lbl11.update()
        progr.set(progr.get() + 20)
        if ii <= 3:
            ii += 1
            lbl2.configure(text=list[ii][0])
            lbl2.update()
            rb1.configure(text=list[ii][1])
            rb22.configure(text=list[ii][2])
            rb33.configure(text=list[ii][3])
            rb44.configure(text=list[ii][4])
        else:
            rb1.configure(state='disabled')
            rb22.configure(state='disabled')
            rb33.configure(state='disabled')
            rb44.configure(state='disabled')
            back2()

    def start22():
        global lbl2, list, lbl100, lbl11, j, k, rb1, rb22, rb33, rb44, answer, ii, bar, progr
        answer = StringVar()
        answer.set('10')
        answer.trace("w", check)
        lbl2 = tk.Label(root, text=list[ii][0], fg='white', bg='black', font=('Tahoma', 25))
        lbl2.pack()
        rb1 = tk.Radiobutton(root, text=list[ii][1], value='1', variable=answer, fg='white', bg='black',
                          font=('Tahoma', 25))
        rb1.pack()
        rb22 = tk.Radiobutton(root, text=list[ii][2], value='2', variable=answer, fg='white', bg='black',
                           font=('Tahoma', 25))
        rb22.pack()
        rb33 = tk.Radiobutton(root, text=list[ii][3], value='3', variable=answer, fg='white', bg='black',
                           font=('Tahoma', 25))
        rb33.pack()
        rb44 = tk.Radiobutton(root, text=list[ii][4], value='4', variable=answer, fg='white', bg='black',
                           font=('Tahoma', 25))
        rb44.pack()
        j = 0
        k = 0
        lbl100 = tk.Label(root, text='Correct: 0', fg='white', bg='black', font=('Tahoma', 25))
        lbl100.pack()
        lbl100.update()
        lbl11 = tk.Label(root, text='Wrong: 0', fg='white', bg='black', font=('Tahoma', 25))
        lbl11.pack()
        lbl11.update()
        progr = IntVar()
        progr.set(0)

        bar = ttk.Progressbar(root, length=800, style='grey.Horizontal.TProgressbar', variable=progr)
        bar.pack()

    start22()


def color_game():
    root.title('Color Game')
    global z, a, c, d, b
    if z == 0:
        btn2.destroy()
        btn.destroy()
        lbl2.destroy()
        lbl8.destroy()
        btn66.destroy()
        label.destroy()
    elif z == 1:
        lbl.destroy()
        lbl2.destroy()
        lbl3.destroy()
        lbl4.destroy()
        entr.destroy()
        btn4.destroy()
        btn5.destroy()
        btn6.destroy()

    z = 0
    a = 30
    b = 0
    d = 0
    c = 0

    colorss = ['Red', 'Green', 'Yellow', 'Blue', 'Brown', 'White', 'Purple']

    def count():
        global a
        a -= 1
        lbl3.configure(text='Time left:' + str(a))
        lbl3.update()
        if a == 0:
            entr.configure(state='disabled')
            messagebox.showinfo('Finish', message='Time is over')
            back()
        else:
            lbl3.after(1000, count)

    def change(*args):
        global b
        random.shuffle(colorss)
        lbl4.configure(fg=str(colorss[0]), text=str(colorss[1]), font=('Arial', 55))

    def go(*args):
        global b, d, c

        if c == 0:
            count()
            c = 1
        else:
            f = entr.get()
            if f == str(colorss[0]) or f == str(colorss[0].upper()) or f == str(colorss[0].lower()):
                b += 1
                lbl2.configure(text='Score:' + str(b))
                lbl2.update()
            entr.delete(0, 'end')

        change()
        lbl2.configure(text='Score:' + str(b))
        entr.delete(0, 'end')

    def menuu():
        global a, colorss, lbl4, lbl2, lbl3, entr, lbl
        lbl = tk.Label(root, text='Type the color, not the word!!!', fg='white', bg='black', font=('Tahoma', 25))
        lbl.pack()
        lbl2 = tk.Label(root, text='Press ENTER to start', fg='white', bg='black', font=('Tahoma', 25))
        lbl2.pack()
        lbl3 = tk.Label(root, text='Time left:' + str(a), fg='white', bg='black', font=('Tahoma', 25))
        lbl3.pack()
        lbl4 = tk.Label(root, text='', fg='white', bg='black', font=('Tahoma', 25))
        lbl4.pack()
        entr = tk.Entry(root, font=('Tahoma', 25))
        entr.pack()

        logo = PhotoImage(file="projects/logo.png")
        labellogo = tk.Label(root, image=logo, bg='black')
        labellogo.pack()        
        root.bind('<Return>', go)
    menuu()


def menu(*args):
    global name, lbl2, btn, btn2, z, lbl8,btn66,label,logo

    if z == 1:
        lbl.destroy()
        lbl2.destroy()
        lbl3.destroy()
        lbl4.destroy()
        entr.destroy()
        btn4.destroy()
        btn5.destroy()
        btn6.destroy()
    elif z == 2:
        rb1.destroy()
        rb22.destroy()
        rb33.destroy()
        rb44.destroy()
        lbl2.destroy()
        lbl100.destroy()
        lbl11.destroy()
        bar.destroy()
        btn4.destroy()
        btn5.destroy()
        btn6.destroy()
    else:
        name = entr.get()
        entr.destroy()
        lbl.destroy()
        label2.destroy()
    root.title('Main Menu')
    z = 0
    lbl8 = tk.Label(root, text='Welcome ' + name, fg='white', bg='black', font=('Tahoma', 25))
    lbl8.pack()
    lbl2 = tk.Label(text='Choose a game to play', fg='white', bg='black', font=('Tahoma', 25))
    lbl2.pack()
    btn = tk.Button(root, text='Color Game', command=color_game, fg='white', bg='black', font=('Tahoma', 25))
    btn.pack()
    btn2 = tk.Button(root, text='Quiz Game', command=quiz_game, fg='white', bg='black', font=('Tahoma', 25))
    btn2.pack()
    btn66 = tk.Button(text='Exit', command=quit, fg='white', bg='black', font=('Tahoma', 25))
    btn66.pack()
    logo = PhotoImage(file="projects/logo.png")
    label = tk.Label(root, image=logo, bg='black')
    label.pack(side=BOTTOM)

root.title('Welcome')
lbl = tk.Label(root, text='Please type your name', fg='white', bg='black', font=('Tahoma', 25))
lbl.pack()
entr = tk.Entry(root, font=('Tahoma', 25))
entr.pack()
root.bind('<Return>', menu)
logo = PhotoImage(file="projects/logo.png")
label2 = tk.Label(root, image=logo, bg='black')
label2.pack(side=BOTTOM)



root.mainloop()