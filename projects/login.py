from tkinter import *
import tkinter.messagebox as tm
import time

win = Tk()
win.title("Yo")
win.geometry("300x90")


def done():
    name = entrName.get()
    pw = entrPass.get()
    email = entrEmail.get()
    lblName.destroy()
    lblPass.destroy()
    lblEmail.destroy()
    entrName.destroy()
    entrPass.destroy()
    entrEmail.destroy()
    btnDone.destroy()
    lblDone = Label(win, text="Signing up as"+name)
    lblDone.grid(padx=10, pady=10)
    time.sleep(1)
    lblDone.configure(text="Signing up as "+name+".")
    lblDone.update()
    time.sleep(1)
    lblDone.configure(text="Signing up as "+name+"..")
    lblDone.update()
    time.sleep(1)
    lblDone.configure(text="Signing up as "+name+"...")
    lblDone.update()
    time.sleep(2)
    lblDone.destroy()
    lblSignedUp = Label(win, text="Signed Up Successfully!", font=15)
    lblSignedUp.pack()
    lblSignedUp2 = Label(win, text="Returning to Sign In page")
    lblSignedUp2.pack()
    lblSignedUp.update()
    lblSignedUp2.update()
    time.sleep(4)
    lblSignedUp.destroy()
    lblSignedUp2.destroy()
    signin(name, pw, email)


def signin(username, password, email):
    def button_pressed():
        mail = entrSEmail.get()
        pw = entrSPass.get()

        if email == mail:
            if password == pw:
                tm.showinfo("Login Info", "Welcome " + username)
                win.destroy()
                quit()
            else:
                tm.showerror("Login Error", "Wrong Password!")
        else:
            tm.showerror("Login Error", "Email not found.")

    lblSEmail = Label(win, text="Email:")
    lblSEmail.grid(column=0, row=0)
    lblSPass = Label(win, text="Password:")
    lblSPass.grid(column=0, row=1)

    entrSEmail = Entry(win)
    entrSEmail.grid(column=1, row=0)
    entrSPass = Entry(win, show="*")
    entrSPass.grid(column=1, row=1)

    btnSdone = Button(win, width=10, height=2, relief="groove", text="Done", command=button_pressed)
    btnSdone.grid(column=2, row=0, padx=20)


lblName = Label(win, text="Username:")
lblName.grid(column=0, row=0)
lblPass = Label(win, text="Password:")
lblPass.grid(column=0, row=1)
lblEmail = Label(win, text="Email:")
lblEmail.grid(column=0, row=2)

entrName = Entry(win)
entrName.grid(column=1, row=0)
entrPass = Entry(win, show="*")
entrPass.grid(column=1, row=1)
entrEmail = Entry(win)
entrEmail.grid(column=1, row=2)

btnDone = Button(win, width=10, height=2, relief="groove", text="Done", command=done)
btnDone.grid(column=2, row=1, padx=20)

win.mainloop()
