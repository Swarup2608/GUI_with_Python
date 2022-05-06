from tkinter import *

OPT = {
    "Afghani" : 1.23,
    "US Dollar" : 0.013,
    "Euro" : 0.012,
    "Brazilian Real" : 0.067,
    "Australian Dollar" : 0.019,
    "Canadian Dollar" : 0.017,
    "Rupiah" : 192.05,
}

def converter():
    rup = rupees_entry.get()
    to = var.get()
    opt = OPT[to]
    converted = float(opt) * float(rup)
    result.delete(1.0,END)
    converted = str(round(converted, 3))
    result.insert(INSERT,"Price in ",INSERT,to,INSERT," = ",INSERT,converted)

root = Tk()

frames = Frame(root)
root.title("Currency Converter (Indian to others)")

title = Label(frames,text="Currency Converter",font="Helvatica 24 bold underline",fg="#03adfc")
title.grid(row=0,column=3,columnspan=4,padx=5,pady=10)

result = Text(frames,height=5,width=50,font="Helvatica 24 bold",bd=5)
result.grid(row=1,column=0,columnspan=10,padx=5,pady=10)

rupees = Label(frames,text="Indian Rupees : ",font="Helvatica 24 bold underline",fg="#03adfc")
rupees.grid(row=2,column=0,columnspan=3,padx=5,pady=10)

rupees_entry = Entry(frames,font="Helvatica 24 bold")
rupees_entry.grid(row=2,column=3,columnspan=7,padx=5,pady=10)

choice = Label(frames,text="Choose the country : ",font="Helvatica 24 bold underline",fg="#03adfc")
choice.grid(row=3,column=0,columnspan=3,padx=5,pady=10)

var = StringVar()
var.set(None)

opt = OptionMenu(frames,var,*OPT)
opt.grid(row=3,column=3,columnspan=7,padx=5,pady=10,sticky="ew")

btn = Button(frames,text="Convert",fg="green",font="Helvatica 24 bold",bg="powder blue",command=converter)
btn.grid(row=4,column=3,columnspan=4,padx=5,pady=10)

frames.pack(expand=True)

root.mainloop()