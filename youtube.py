# https://www.youtube.com/watch?v=4CKFAb1FNns

from cProfile import label
from tkinter import *
from pyparsing import col
import pytube
from pytube import YouTube
from tkinter import filedialog, messagebox

def createWidgets():
    link_label = Label(root,text="Youtube URL :",bg="#E8D579").grid(row=1,column=0,pady=5,padx=5)
    root_link = Entry(root,width=60,textvariable=video_link).grid(row=1,column=1,pady=5,padx=5)
    des_label = Label(root,text="Destination Label :",bg="#E8D579").grid(row=2,column=0,pady=5,padx=5)
    root_des = Entry(root,width=45,textvariable=des_sor).grid(row=2,column=1,pady=3,padx=3)
    browse_but = Button(root,text="Browse",command=browse,width=10,bg="#05e8e0").grid(row=2,column=2,pady=1,padx=1)
    download_but = Button(root,text="Download",command=download,width=25,bg="#05e8e0").grid(row=3,column=1,padx=3,pady=3)

def browse():
    down_dir = filedialog.askdirectory(initialdir="Your Directory Path")
    des_sor.set(down_dir)

def download():
    url = video_link.get()
    folder = des_sor.get()
    get_vid = YouTube(url)
    yt = get_vid.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    yt.download(folder)
    messagebox.showinfo("Success","Successfully Downloaded the image!!")

root = Tk()
root.geometry("600x120")
root.resizable(False,False)
root.title("Pytube")
root.configure(background="#000000")
video_link = StringVar()
des_sor = StringVar()
createWidgets()



root.mainloop()