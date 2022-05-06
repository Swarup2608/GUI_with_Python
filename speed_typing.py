from tkinter import *
import time
import threading
import random

class TypeSpeedGui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Typing Speed Tester")
        self.root.geometry("800x600")
        
        self.texts = open("texts.txt","r").read().split("\n")

        self.frame = Frame(self.root)

        self.sample_label = Label(self.frame,text=random.choice(self.texts),font="Helvetica 18")
        self.sample_label.grid(row=0,column=0,columnspan=2,padx=2,pady=5)

        self.input_entry  = Entry(self.frame,width=40,font="Helvetica 24")
        self.input_entry.grid(row=1,column=0,columnspan=2,padx=2,pady=10)
        self.input_entry.bind("<KeyRelease>",self.start)

        self.speed_label = Label(self.frame,text="Speed: \n 0.00 CPS \n 0.00 CPM \n  0.00 WPS \n 0.00 WPM",font="Helvetica 18")
        self.speed_label.grid(row=2,column=0,columnspan=2,padx=2,pady=5)

        self.reset_button = Button(self.frame,text="Reset",font="Helvetica 24",command=self.reset)
        self.reset_button.grid(row=3,column=0,columnspan=2,padx=5,pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.started = False

        self.root.mainloop()

    def start(self,event):
        if not self.started:
            if not event.keycode in [50,62,64,113,37,109]:
                self.started = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == self.sample_label.cget('text'):
            self.started = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.started:
            time.sleep(0.1)
            self.counter+=0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps*60
            wps = len(self.input_entry.get().split()) / self.counter
            wpm = wps*60
            self.speed_label.config(text="Speed: \n{:.2f} CPS \n {:.2f} CPM \n {:.2f} WPS \n {:.2f} WPM".format(cps,cpm,wps,wpm))
     
    def reset(self):
        self.started = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n 0.00 CPS \n 0.00 CPM \n  0.00 WPS \n 0.00 WPM")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0,END)
    
TypeSpeedGui()