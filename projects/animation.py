from tkinter import *
import time

win = Tk()
win.geometry('1000x1000')

def Animation(variable, xpos, ypos, endx, endy):
    for i in range(0,75,1):
        xchange = (endx-xpos)/15
        xpos += xchange
        ychange = (endy-ypos)/15
        ypos += ychange
        variable.place(x=xpos, y=ypos)
        variable.update()
        time.sleep(0.01)
    variable.place(x=endx, y=endy)


homebtncg = Button(win, bg="red", width=2, command= lambda: Animation(homebtncg, 100, 500, 100, 300))
homebtncg.place(x=100, y=500)

win.mainloop()