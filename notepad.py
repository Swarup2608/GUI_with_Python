from tkinter import *
from tkinter.filedialog import *
# Functions
def openFile():
    file = askopenfile(mode="r",filetype=[('text files','*.txt')])
    entry.delete(1.0,END)
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content)

def saveFile():
    new_file = asksaveasfile(mode="w",filetype=[('text files','.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0,END))
    new_file.write(text)
    new_file.close()

def clearFile():
    entry.delete(1.0,END)


root = Tk()
root.geometry("400x600")
root.title("Own Notepad")
root.config(bg="white")

top = Frame(root)
top.pack(padx=10,pady=5,anchor="nw")

open_btn = Button(root,text="Open",bg="#006aff",fg="white",command= openFile)
open_btn.pack(in_=top,side=LEFT)

save_btn = Button(root,text="Save",bg="#006aff",fg="white",command= saveFile)
save_btn.pack(in_=top,side=LEFT)

clear_btn = Button(root,text="Clear",bg="#006aff",fg="white",command= clearFile)
clear_btn.pack(in_=top,side=LEFT)

exit_btn = Button(root,text="Exit",bg="#006aff",fg="white",command= exit )
exit_btn.pack(in_=top,side=LEFT)

entry = Text(root,wrap=WORD,bg="#a6deff",font="Poppins 15 bold")
entry.pack(padx=10,pady=5,expand=TRUE,fill=BOTH)

root.mainloop()