from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random

window = ThemedTk(theme = "equilux")
window.configure(themebg = "equilux")
window.geometry("300x250")

triesno = 0
think_time = random.randint(2,5)
tries_color = "Green"
cr_png = PhotoImage(file="projects/correct.png")
die_png = PhotoImage(file="projects/die.png")
up_arrow = PhotoImage(file="projects/up_arrow.png")
down_arrow = PhotoImage(file="projects/down_arrow.png")
game_started = False
def game_start():
    Think()
    global random_word,game_started,triesno
    game_started = True
    triesno = 0
    tries.config(text="Tries " + str(triesno))
    png_image.config(image=die_png)
    difficulty = rb.get()
    if difficulty == "Radio1":
        random_word = random.randint(0,50)
    elif difficulty == "Radio2":
        random_word = random.randint(0,100)
    elif difficulty == "Radio3":
        random_word = random.randint(0,200)
        print(random_word)
    for radio in all_radios:
        radio.configure(state=DISABLED)
    text_box.config(state=ACTIVE)
    text_box.delete('0' , END)
def guessing(event=0):
    global random_word, triesno, game_started,think_time,tries_color
    if game_started == True:
        guess = str(text_box.get())
        guess = int(guess)
        if guess == random_word:
            triesno += 1
            text_box.delete('0' , END)
            text_box.config(state=DISABLED)
            png_image.config(image=cr_png)
            starter_text2.config(text="Well done! The number was " + str(random_word)+"\n"
                                     "You got it in "+ str(triesno)+ " tries. Good job!")
            thinking_lbl.configure(text="")
            for radio in all_radios:
                radio.configure(state=ACTIVE)
            think_time = random.randint(2,5)
            str_button.config(state=ACTIVE)
            str_button.config(text="Start")
            tries_color = "green"
        elif guess > random_word:
            triesno += 1
            png_image.config(image=down_arrow)
            text_box.delete('0' , END)
        elif guess < random_word:
            triesno += 1
            png_image.config(image=up_arrow)
            text_box.delete('0' , END)
        if triesno > 3 and triesno < 6:
            tries_color = "yellow"
        elif triesno > 6 and triesno < 9:
            tries_color = "orange"
        elif triesno > 9 and triesno < 12:
            tries_color = "red"
        elif triesno > 3 and triesno < 6:
            tries_color = "dark red"
        tries.config(text= "Tries " + str(triesno),foreground=tries_color)
def Think():
    global think_time
    print(think_time)
    think_time -= 1
    if think_time > 0:
        str_button.config(text="Thinking")
        str_button.config(state=DISABLED)
        dots = random.randint(1,3)
        if dots == 1:
            thinking_lbl.configure(text="...")
        if dots == 2:
            thinking_lbl.configure(text=".....")
        if dots == 3:
            thinking_lbl.configure(text=".........")
        if think_time != 0:
            thinking_lbl.after(1000,Think)
    elif think_time == 0:
        str_button.config(text="Thunk")
        thinking_lbl.configure(text="Guess now")
        game_start()





#instructions / info

starter_text = ttk.Label(window,text= "Guessing Game",font=("Calibri",16),anchor=N)
starter_text.place(x=80,y=0)

starter_text2 = ttk.Label(window,text= "The computer will think of a number \n"
                                       "your job is to guess that number good luck",font=("Calibri",12))
starter_text2.place(x=10,y=30)

tries = ttk.Label(window,text= "Tries " + str(triesno),font=("Calibri",12))
tries.place(x=252,y=200)

thinking_lbl = ttk.Label(window,text="",font=("Calibri",12))
thinking_lbl.place(x=0,y=180)


#Image

png_image = ttk.Label(window,image=die_png)
png_image.place(x=100,y=120)

#Buttons

str_button = ttk.Button(window,text= "Start",command=Think)
str_button.place(x=0,y=200,height=50)

#Text box

text_box = ttk.Entry(window)
text_box.place(x=250,y=220,width=50,height=30)
text_box.config(state=DISABLED)

#Combobox

rb = StringVar()
rb.set("Radio2")
radio1 = ttk.Radiobutton(window, text="Easy (0,50)",value="Radio1",variable= rb)
radio2 = ttk.Radiobutton(window, text="Normal (0,100)",value="Radio2",variable= rb)
radio3 = ttk.Radiobutton(window, text="Hard (0,200)",value="Radio3",variable= rb)
radio1.place(x=0,y=75)
radio2.place(x=85,y=75)
radio3.place(x=195,y=75)
all_radios = [radio1,radio2,radio3]
#check with enter
window.bind("<Return>",guessing)

window.title("Speed typer")
window.mainloop()
