import webbrowser
import urllib.request
import time
import os
from bs4 import *
import tkinter as k
import sys
q = k.Tk()
q.title("Calculation @SAyantan")
q.geometry("500x100")

w = k.Tk()
w.title("Result @SAyantan")
w.geometry("800x150")

# Function

def evaluate():
    ex = str(e1.get())
    try:
        k=(eval(ex))
    except:
        k="Please enter a vaid expression..String not allow"
    return(k)

def integrationcal():
    ex = str(e1.get())
    ex = (ex.replace("+", "%2B"))
    url = "https://m.wolframalpha.com/input/?i=integration+of+" + ex
    s = out(url)
    return s

def diffrentiationcal():
    ex = str(e1.get())
    
    ex = (ex.replace("+", "%2B"))
    url = "https://m.wolframalpha.com/input/?i=derivative+of+" + ex
    s = out(url)
    return s

def integration():
    greet =integrationcal()
    # TEXT FIELD
    t1 = k.Text(master=w, height=2, width=120)
    t1.pack()
    t1.insert(k.END, greet)
    q.mainloop()
    
def diffrentiation():
    greet =diffrentiationcal()
    # TEXT FIELD
    t1 = k.Text(master=w,height=2, width=120)
    t1.pack()
    t1.insert(k.END, greet)
    q.mainloop()
def evalu():
    s=evaluate()
    t1 = k.Text(master=w, height=2, width=120)
    t1.pack()

    #t1.grid(column=3, row=2)
    t1.insert(k.END,s)
    q.mainloop()
def exits():
    w.destroy()
    q.destroy()
    print("Thank Yor Using The Application @SAyantan \n Feedback=gsayantan02@gmail.com")
def out(url):
    try:
        a = 0
        p = 0
        c = 0
        s = urllib.request.urlopen(url).read()
        s = s.decode("utf-8")
        soup = BeautifulSoup(s, "html.parser")
        # print(soup)
        soups = soup.findAll("div", {"class": "output pnt"})
        k = str(soups)
        # print(k)
        j = k.index('alt')
        k = k[j:]
        kj = ""
        for i in k:
            if(i == '"'):
                a = a + 1
            if(i == '\\'):
                continue
            if(a == 1):
                kj = kj + i
            if(a == 2):
                break
        if(kj==""):
            kj="Sorry!!Please enter a valid expression"
        return kj
    except:
        kj="PLEASE do CHECK your internet connection and try again..Or enter a valid input"
        return kj
    



# Label
tit=k.Label(w,text="Answer:",font=("Times New Roman", 15))
tit.pack()
l1 = k.Label(text="Calculation is Fun With Me", font=("Times New Roman", 15))
#l1.grid(column=1, row=0)
l1.grid(columnspan=4)

l2 = k.Label(text="Enter your Expression:", font=("Times New Roman", 12))
l2.grid(column=0, row=1)


# Entry
e1 = k.Entry()
e1.grid(column=1, row=1)

# Button
i = k.Button(text="∫",fg="Blue", command=integration)
i.grid(column=0, row=2)
d = k.Button(text="d/dx",fg="Blue",command=diffrentiation)
d.grid(column=2, row=2)
eq = k.Button(text="=",fg="Green", command=evalu)
eq.grid(column=1,row=2)
#i.grid(column=3, row=2)
i = k.Button(text="Good Bye",fg="Red", command=exits)
i.grid(column=1,row=3)
#i.grid(column=3, row=2)
w.mainloop()

