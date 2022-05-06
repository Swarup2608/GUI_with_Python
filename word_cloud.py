from tkinter import *
from tkinter import messagebox
import sys
import numpy as np
from PIL import Image
from wordcloud import WordCloud,STOPWORDS
import nltk
from nltk.corpus import wordnet
import wikipedia

def word():
    opt = e2.get()
    to = e1.get()
    
    try:
        if opt == 'syn':
            syno = [0]
            for syn in wordnet.synsets(to):
                for lemma in syn.lemmas():
                    syno.append(lemma.name())
            syno.remove(0)
            text = " "
            for i in syno:
                text+=i+" "
        else:
            title  = wikipedia.search(to)[0]
            page = wikipedia.page(title)
            text = page.content
        bg = np.array(Image.open('1.jpg'))
        unwanted_words = set(STOPWORDS)
        wordclo = WordCloud(background_color='black',max_words=400,mask=bg,stopwords=unwanted_words)
        wordclo.generate(text)
        wordclo.to_file('sample.png')
        messagebox.showinfo('Saved Successfully')
        root.destroy()
    except Exception as e:
        messagebox.showerror('Unknown Error occured, try again')
root = Tk()
root.title('Word Cloud Builder')
root.geometry("250x150")
global e1
global e2
Label(root,text="To Search: ").place(x=10,y=10)
Label(root,text="Create From: ").place(x=10,y=40)
e1 = Entry(root)
e1.place(x=100,y=10)
e2 = Entry(root)
e2.place(x=100,y=40)
Button(root,text="Create",command=word,height=1,width=13).place(x=70,y=100)
root.mainloop()