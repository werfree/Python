from tkinter import *
from random import*
import sys
w=Tk()
w.title("Catch Me")
gameover=False
def jump(event):
    b1.place(relx=random(),rely=random())
    return 
def p(w):
    global gameover
    if gameover==False:
        print("You are FASTER")
        gameover=True
    sys.exit()
    w.destroy()
while True:
    frame=Frame(w)
    w.geometry("300x300")
    frame.pack()
    if gameover==False:
        b1=Button(w,text="Click here",bg="Black",fg="Yellow",command=lambda:p(w))
        b1.bind("<Enter>",jump)
        b1.pack()
        w.mainloop()
    else:
        break

