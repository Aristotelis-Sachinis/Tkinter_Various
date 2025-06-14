from tkinter import *
from tkinter.ttk import *

win = Tk()
win.title = "E-Shop"
win.geometry("350x300")
l = [0, 0, 0, 0]

class OrderBox:
    def __init__(self, category, model1, model2, model3, model4, clmn):
        self.category = category
        self.model1 = model1
        self.model2 = model2
        self.model3 = model3
        self.model4 = model4
        self.clmn = clmn

    def BoxCr(self):
        self.btn = Button(win, text="Order", command=self.Order)
        self.btn.grid(column=0, columnspan=4, row=6)

        self.catlbl = Label(text=self.category)
        self.catlbl.grid(column=self.clmn, row=0)

        self.rb = StringVar()
        self.rad1 = Radiobutton(win, text=self.model1, value=self.model1, var=self.rb, command= lambda : self.GetItem())
        self.rad2 = Radiobutton(win, text=self.model2, value=self.model2, var=self.rb, command= lambda : self.GetItem())
        self.rad3 = Radiobutton(win, text=self.model3, value=self.model3, var=self.rb, command= lambda : self.GetItem())
        self.rad4 = Radiobutton(win, text=self.model4, value=self.model4, var=self.rb, command= lambda : self.GetItem())
        self.rad1.grid(column=self.clmn, row=1)
        self.rad2.grid(column=self.clmn, row=2)
        self.rad3.grid(column=self.clmn, row=3)
        self.rad4.grid(column=self.clmn, row=4)

        self.lbl2 = Label(win, text="")
        self.lbl2.grid(column=0, columnspan=4, row=7)

    def GetItem(self):
        if self.category == "GPU":
            l[0] = self.rb.get()
        elif self.category == "CPU":
            l[1] = self.rb.get()
        elif self.category == "RAM":
            l[2] = self.rb.get()
        else:
            l[3] = self.rb.get()

    def Order(self):
        lFinal = []
        for i in l:
            if type(i) is str:
                lFinal.append(i)
        self.lbl2.config(text="You have ordered: " + ", ".join(lFinal))


OrderBox(category="GPU", model1="GT 1030", model2="GTX 1660", model3="RTX 2070", model4="RTX 3060",
         clmn=0).BoxCr()
OrderBox(category="CPU", model1="i3", model2="ryzen 5", model3="i7", model4="ryzen 9", clmn=1).BoxCr()
OrderBox(category="RAM", model1="1x4", model2="1x8", model3="2x8", model4="2x16", clmn=2).BoxCr()
OrderBox(category="SSD", model1="250GB", model2="500GB", model3="1T", model4="2T", clmn=3).BoxCr()

win.mainloop()