## Note

#Install

''' Install the module gtts,pymsgbox,playsound,pyautogui,tkinter'''

###Control

#With Computer

'''Arrow up and down '''

#With friend

'''For player 1- W and X
   For player 2- Arrow up and Down '''


##Error

'''Please do contact me=gsayantan01@gmail.com'''






import time,os,winsound,tkinter.messagebox,random,pyautogui,pymsgbox
from gtts import gTTS
from playsound import playsound
from tkinter import *
import tkinter as k

####Global##
c=0
c2=0
var=1
var2=0
path = os.path.dirname(os.path.realpath(__file__))
s2=0

#######sound##################


def sound(s):
    global path
    if(s=="Helloworld"):
        p=path+"\\test.wav"
        winsound.PlaySound(p, winsound.SND_ASYNC | winsound.SND_ALIAS )
    if(s=="Despacito"):
        p=path+"\\Despacito.wav"
        winsound.PlaySound(p, winsound.SND_ASYNC | winsound.SND_ALIAS )
    if(s=="Cartoon"):
        p=path+"\\Cartoon.wav"
        winsound.PlaySound(p, winsound.SND_ASYNC | winsound.SND_ALIAS )
    if(s=="Thanks"):
        p=path+"\\Thank.wav"
        winsound.PlaySound(p, winsound.SND_ASYNC | winsound.SND_ALIAS )
    if(s=="credits"):
        p=path+"\\credits.wav"
        winsound.PlaySound(p, winsound.SND_ASYNC | winsound.SND_ALIAS)
    if(s=="allthebest"):
        print(s)
        p=path+"\\allthebest.wav"
        playsound(p)
        
        
    return
########################                       #################Ball Single###############      ######################################
class BallS:                             
    def __init__(self,canvas,color,paddle,paddle2):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,232,170)
        self.canvas_height=self.canvas.winfo_height()  #window size height
        self.canvas_width=self.canvas.winfo_width()    #window size width

        start=[-3,3]
        self.x=random.choice(start)
        self.y=-3
        self.paddle=paddle
        self.paddle2=paddle2
        self.c=0
        selfc2=0

    def hitpaddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if(pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]):
           if(pos[0]>=paddle_pos[0]and pos[0]<=paddle_pos[2]):
              return True#return array[x1,y1,x2,y2]
           return False
    def hitpaddle2(self,pos):
        paddle_pos=self.canvas.coords(self.paddle2.id)
        if(pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]):
           if(pos[2]>=paddle_pos[0]and pos[2]<=paddle_pos[2]):
              return True#return array[x1,y1,x2,y2]
           return False
    def paddleauto(self):
        
        if(self.y>0):
            (self.paddle.y)=(abs(self.y)*2)-2
        else:
            (self.paddle.y)=(-abs(self.y) *2)+2

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)#return array[x1,y1,x2,y2]
        #print(pos)
        self.paddleauto()
        self.paddle.draw()
        self.paddle.movep2()
        sp=[2,3,4,5]
        sm=[-2,-3,-3,-4]

        if pos[1]<=0:      #top
            self.y=random.choice(sp)
            
        if pos[3]>=self.canvas_height:  #bottom
            self.y=random.choice(sm)

        if pos[0]<=0:
            self.x=random.choice(sp)
            self.score("c",self.canvas)

        if pos[2]>=self.canvas_width:
           self.x=-2
           self.score("m",self.canvas)
        if self.hitpaddle(pos)==True:
            self.x=random.choice(sp)
        if self.hitpaddle2(pos)==True:
            self.x=-2
    def score(self,val,canvas):
        global c
        global c2
        global s2
        

        if(val=="m"):
            a=self.canvas.create_text(125,40,text=c,font=("Arial",60),fill="White")
            canvas.itemconfig(a,fill="black")
            c+=1
            a=self.canvas.create_text(125,40,text=c,font=("Arial",60),fill="White")
        if(val=="c"):
            a=self.canvas.create_text(350,40,text=c2,font=("Arial",60),fill="White")
            canvas.itemconfig(a,fill="black")
            c2+=1
            a=self.canvas.create_text(350,40,text=c2,font=("Arial",60),fill="White")
        print(str(c)+"\t"+str(c2))




#######################          #################Paddle   Single######################################################


            
class PaddleS:
    def __init__(self,canvas,color,e):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,150,20,250,fill=color)
        self.canvas.move(self.id,0,0)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        

    def draw(self):
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:   #left
            self.y=+5
        if pos[3]>=self.canvas_height:   #right
            self.y=-5
    
    def movep2(self):
        self.canvas.move(self.id,0,self.y)


################################          #################Ball Multi############################################################

class BallM:
    def __init__(self,canvas,color,paddle,paddle2):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,232,170)
        self.canvas_height=self.canvas.winfo_height()  #window size height
        self.canvas_width=self.canvas.winfo_width()    #window size width

        start=[-3,3]
        self.x=random.choice(start)
        self.y=-3
        self.paddle=paddle
        self.paddle2=paddle2
        self.c=0
        selfc2=0

    def hitpaddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if(pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]):
           if(pos[0]>=paddle_pos[0]and pos[0]<=paddle_pos[2]):
              return True#return array[x1,y1,x2,y2]
           return False
    def hitpaddle2(self,pos):
        paddle_pos=self.canvas.coords(self.paddle2.id)
        if(pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]):
           if(pos[2]>=paddle_pos[0]and pos[2]<=paddle_pos[2]):
              return True#return array[x1,y1,x2,y2]
           return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)#return array[x1,y1,x2,y2]
        #print(pos)
        sp=[2,3,4,5]
        sm=[-2,-3,-4,-5]

        if pos[1]<=0:      #top
            self.y=random.choice(sp)
            
        if pos[3]>=self.canvas_height:  #bottom
            self.y=random.choice(sm)

        if pos[0]<=0:
            self.x=random.choice(sp)
            self.score("c",self.canvas)

        if pos[2]>=self.canvas_width:
           self.x=random.choice(sm)
           self.score("m",self.canvas)
        if self.hitpaddle(pos)==True:
            self.x=random.choice(sp)
        if self.hitpaddle2(pos)==True:
            self.x=random.choice(sm)
            

    def score(self,val,canvas):
        global c
        global c2
        

        if(val=="m"):
            a=self.canvas.create_text(125,40,text=c,font=("Arial",60),fill="White")
            canvas.itemconfig(a,fill="black")
            c+=1
            a=self.canvas.create_text(125,40,text=c,font=("Arial",60),fill="White")
        if(val=="c"):
            a=self.canvas.create_text(350,40,text=c2,font=("Arial",60),fill="White")
            canvas.itemconfig(a,fill="black")
            c2+=1
            a=self.canvas.create_text(350,40,text=c2,font=("Arial",60),fill="White")


#####################################      #################Paddle Single##################################################################


            
class PaddleM:
    def __init__(self,canvas,color,e):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,150,20,250,fill=color)
        self.canvas.move(self.id,0,0)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        e.bind("<w>",self.up)
        e.bind("<x>",self.down)
        
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]==0:   #left
            self.y=0
        if pos[1]<0:
            self.y=3
        if pos[3]==self.canvas_height:   #right
            self.y=0
        if pos[3]>self.canvas_height:
            self.y=-3
        
    def up(self,event):
        self.y=-3
    def down(self,event):
        self.y=3
#######################################################Common Paddle########################################################################
    
class Paddle2:
    def __init__(self,canvas,color,e):
        self.canvas=canvas
        self.id=canvas.create_rectangle(480,150,500,250,fill=color)
        self.canvas.move(self.id,0,0)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        e.bind("<Up>",self.up)
        e.bind("<Down>",self.down)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]==0:   #left
            self.y=0
        if pos[1]<0:
            self.y=3
        if pos[3]==self.canvas_height:   #right
            self.y=0
        if pos[3]>self.canvas_height:
            self.y=-3


    def up(self,event):
        self.y=-3
    def down(self,event):
        self.y=3


##################################################################        Display                   ###############################################################
def click(e):
    x=e.winfo_x()
    y=e.winfo_y()
    pyautogui.click(x,y)

######################Object Creation##########################

def gameboard(s):
    e=Tk()
    e.title("Pong")
    e.resizable(0,0)
    e.wm_attributes("-topmost",1)
    canvas=Canvas(e,width=500,height=400,border=0,highlightthickness=0)
    canvas.config(bg="black")
    canvas.create_line(250,0,250,400,fill="yellow")
    canvas.pack()
    e.focus()
    e.update()
    click(e)
    time.sleep(3)
    paddle2=Paddle2(canvas,"Blue",e)
    p=s

    if(s=="single"):
        paddle=PaddleS(canvas,"Yellow",e)
        ball=BallS(canvas,"Orange",paddle,paddle2)
        play(ball,paddle,paddle2,p,e)
    else:
        paddlem=PaddleM(canvas,"Yellow",e)
        ballm=BallM(canvas,"Orange",paddlem,paddle2)
        play(ballm,paddlem,paddle2,p,e)




######################         Object Call      &&&&  SCORE    ##########################

        
def play(b,p,p2,s,e):
    global c
    global c2
    global s2
    while True:
        if(c==20):
            c=0
            c2=0
            if(s=="single"):
                e.wm_attributes("-topmost",0)
                i=pymsgbox.confirm(text='Better Luck Next Time...', title='Looser', buttons=['Play Again', 'Bye'])
            else:
                e.wm_attributes("-topmost",0)
                i=pymsgbox.confirm(text='Congratulation!! \n Player one is the winner', title='Winner', buttons=['Play Again', 'Bye'])
            if i=='Play Again':
                e.destroy()
                winsound.PlaySound(None, winsound.SND_PURGE)
                welcome()
            else:
                e.destroy()
                winsound.PlaySound(None, winsound.SND_PURGE)
                sound("Thanks")
                sys.exit()
                
            break
        if(c2==20):
            c=0
            c2=0
            if(s=="single"):
                e.wm_attributes("-topmost",0)
                i=pymsgbox.confirm(text='Congratulation!! \n You are the winner', title='Winner', buttons=['Play Again', 'Bye'])
            
            else:
                e.wm_attributes("-topmost",0)
                i=pymsgbox.confirm(text='Congratulation!! \n Player one is the winner', title='Winner', buttons=['Play Again', 'Bye'])
            if i=='Play Again':
                e.destroy()
                winsound.PlaySound(None, winsound.SND_PURGE)
                welcome()
            else:
                e.destroy()
                winsound.PlaySound(None, winsound.SND_PURGE)
                sound("Thanks")
                sys.exit()
            break
        p.draw()
        p2.draw()
        b.draw()
        e.update()
        #w.update_idletasks()
        time.sleep(0.02)
    
############Check for mode of game################
    
def game(w):
    w.destroy()
    global var
    global var2
    sound("allthebest")
    #time.sleep(3)
    if(var==1):
        sound("Despacito")
        gameboard("single")
    else:
        sound("Cartoon")
        gameboard("multi")

def eg(s,m):
    global var
    global var2
    if(s==0):
        var=0
        var2=1
    elif(m==0):
        var=1
        var2=0

def bye(w):
    sound("Thanks")
    w.destroy()
    sys.exit()
    quit()
###############Wellcome#################
def welcome():
    w=Tk()
    uname=None
    uname2=None
    w.title("Pong")
    w.geometry("500x180")
    w.configure(background='black')
    w.resizable(0,0)
    w.wm_attributes("-topmost",1)
    mainMenu=Menu(w)
    subMenu=Menu(mainMenu)
    mainMenu.add_cascade(label="Credits",command=lambda:sound("credits"))
    mainMenu.add_cascade(label="Bye",command=lambda:bye(w))
    w.config(menu=mainMenu)
    h1=Label(w,text="Game is Fun",font=("Arial",30),fg="Yellow",bg="Black")
    h1.grid(column=2,row=1,columnspan=1)
    #h2=Label(w,text="Player1",font=("Arial",15),fg="White",bg="Black")
    #h3=Label(w,text="Player2",font=("Arial",15),fg="White",bg="Black")
    rs=Radiobutton(w,text="With Computer",fg='White',bg="Black",selectcolor="red",padx=10,pady=19,value=1,command=lambda:eg(1,0))
    rm=Radiobutton(w,text="With Friend",fg='White',bg="Black",selectcolor="red",highlightbackground="Yellow",pady=19,value=2,command=lambda:eg(0,1))
    submits=Button(w,text="Ready!",command=lambda:game(w))
    rs.grid(column=1,row=3)
    #u1=Entry(w,variable=uname)
    #u2=Entry(w,variable=uname2)
    #h2.grid(column=1,row=2)
    #h3.grid(column=3,row=2)
    #u1.grid(column=2,row=2)
    #u1.focus_set()
    #u2.grid(column=4,row=2)
    rm.grid(column=3,row=3)
    submits.grid(column=2,row=5,columnspan=1)
    sound("Helloworld")
    rs.select()
    rm.deselect()
    w.mainloop()
if __name__=="__main__":
    welcome()

