from tkinter import *
import random

window = Tk()
window.geometry("300x250")
#varibles and lists
colours = ["pink","red","blue","yellow","green","black","orange"]
colours_text = ["pink","red","blue","yellow","green","black","orange"]
score = 0
time_left = 30
def not_same():
    global color_choice,color_letter_choice
    color_choice = (random.choice(colours))
    color_letter_choice = (random.choice(colours_text))
def game_start(event):
    if time_left == 30:
        timer()
        new_color()
    check_answer()
def new_color():
    global color_choice
    color_choice = (random.choice(colours))
    color_letter_choice = (random.choice(colours_text))
    if color_choice == color_letter_choice:
        not_same()
    game_text.configure(text=color_letter_choice,fg=color_choice)
def check_answer():
    global color_choice,score
    answer = text_box.get()
    answer = answer.lower()
    if answer == color_choice:
        score += 1
        text_box.delete('0' , END)
        score_lbl.configure(text="Your score is: " + str(score))
        new_color()
    elif answer != "":
        text_box.delete('0' , END)
        new_color()
def timer():
    global time_left,score
    if time_left > 0:
        time_left -= 1
        timer_lbl.configure(text="Time left:" + str(time_left))
        timer_lbl.after(1000,timer)
    elif time_left == 0:
        score = 0
        time_left = 30
        score_lbl.configure(text="Your score is: " + str(score))
        timer_lbl.configure(text="Time left: " + str(time_left))
        game_text.configure(text="")
        text_box.delete('0', END)

#Labels
starter_text = Label(window,text= "Type the colour of the letters",font=("Calibri",12))
starter_text.pack()

starter_text2 = Label(window,text= "press 'enter' to start",font=("Calibri",12))
starter_text2.pack()

score_lbl = Label(window,text="Your score is: " + str(score),font=("Calibri",12))
score_lbl.pack()

timer_lbl = Label(window,text="Time left: " + str(time_left),font=("Calibri",12))
timer_lbl.pack()

game_text = Label(window,text="",font=("Calibri",60))
game_text.pack()


text_box = Entry(window)
text_box.pack()

window.bind("<Return>",game_start)

window.title("Colour game")
window.mainloop()
