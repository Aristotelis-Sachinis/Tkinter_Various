from tkinter import Tk, Canvas, NW
from PIL import ImageTk

win = Tk()

photoimage = ImageTk.PhotoImage(file="projects/logo.png")

width, height = photoimage.width(), photoimage.height()
canvas = Canvas(win, bg="blue", width=width, height=height)
canvas.pack()

canvas.create_image(0, 0, image=photoimage, anchor=NW)

win.mainloop()