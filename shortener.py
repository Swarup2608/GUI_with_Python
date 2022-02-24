import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("URL Shortener")
root.configure(bg="#bfdfff")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladd=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladd)
    url_address.set(url_short)

def copy():
    url_short = url_address.get()
    pyperclip.copy(url_short)

title = Label(root,text="URL Shortner",bd=5,relief=GROOVE,font=("Helvatica",30,"bold"),bg="#ffbfbf",fg="#004cff")
title.pack(side=TOP,fill=X)
Entry(root,textvariable=url,font=("Helvatica",15,"bold"),bd=3,relief=GROOVE).pack(pady=10)
Button(root, text="Generate short url",command=urlshortener).pack(pady=10)
Entry(root,textvariable=url_address,font=("Helvatica",15,"bold"),bd=3,relief=GROOVE).pack(pady=10)
Button(root,text="Copy URL",command=copy).pack(pady=10)

root.mainloop()