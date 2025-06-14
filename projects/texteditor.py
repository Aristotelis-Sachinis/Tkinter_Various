import sys,os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename



window = Tk()
window.geometry("700x500")
def New(event=0):
    Main_textbox.delete(1.0,END)
    Title_textbox.delete(1.0,END)
def Done(event=0):
    sys.exit()
def Save(event=0):
    file_path_to_save = asksaveasfilename(
        defaultextension="txt",
        filetypes= [("Text_files", "*txt*"), ("All Files","*.*")]

    )
    if not file_path_to_save:
        return
    with open(file_path_to_save,"w") as output_file:
        text = Main_textbox.get(1.0,END)
        output_file.write(text)
def Old_Save(event=0):
    global FileName
    Title = Title_textbox.get("1.0", "end-1c")
    FileName = str(Title + ".txt")
    TextFile = open(FileName, "w")
    TextFile.write(Main_textbox.get("1.0", "end-1c"))
def Load(event=0):
    filepathing = askopenfilename(

        filetypes= [("Text_files", "*txt*"), ("All Files","*.*")]
    )
    if not filepathing:
        return
    Main_textbox.delete(1.0,END)
    with open(filepathing,"r") as input_file:
        text_from_loaded_file = input_file.read()
        Main_textbox.insert(END,text_from_loaded_file)

    Title_textbox.delete(1.0,END)
    path = f"Simple Text Editor - {filepathing}"
    Title_textbox.insert(END,os.path.basename(path).split('/')[-1])

#textbox

Main_textbox = Text(window, width=87, height=29)
Main_textbox.place(x=0, y=25)

Title_textbox = Text(window, width=87, height=1)
Title_textbox.place(x=0, y=0)

#Comboboxes

#Menu

# create a menubar
menubar = Menu(window)
window.config(menu=menubar)

# create the file_menu
file_menu = Menu(menubar,tearoff=0)

# add menu items to the File menu
file_menu.add_command(label='Save',command=Save)
file_menu.add_command(label='Save as',command=Old_Save)
file_menu.add_separator()
file_menu.add_command(label='Load',command=Load)
file_menu.add_separator()
file_menu.add_command(label="New",command=New)
file_menu.add_command(label="Exit",command=Done)

# add the File menu to the menubar
menubar.add_cascade(label="File",menu=file_menu)

window.title("Notepad but good")
window.mainloop()
