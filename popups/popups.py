from tkinter import messagebox

messagebox.showinfo('Info Popup', 'Show info message with no response.')

messagebox.showwarning("Warning Popup", "Show warning message with no response.")

messagebox.showerror('Error Popup', 'Show error message with no response.')

res = messagebox.askquestion('Question Popup', 'Show Question message with yes/no response.')
print(res)

res = messagebox.askyesno('Yes/No Popup', "Show Yes/No message with true/false")
print(res)

res = messagebox.askyesnocancel("Yes/No/Cancel Popup", 'Show Yes/No/Cancel message with true/false/none response.')
print(res)

res = messagebox.askokcancel('Ok/Cancel Popup', "Show Ok/Cancel message with true/false response.")
print(res)

res = messagebox.askretrycancel("Retry/Cancel Popup", "Show Retry/Cancel message with true/false response.")
print(res)