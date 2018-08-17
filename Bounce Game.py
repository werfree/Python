from tkinter import *
import tkinter.messagebox
import time ,os
import random
from gtts import gTTS
from playsound import playsound
import winsound
w=Tk()
w.title("Bounce@SAyantan")
w.resizable(0,0)   #to fixed window size
w.wm_attributes("-topmost",1)  #to display the window on top of ever other window
canvas=Canvas(w,width=550,height=550,bd=0,highlightthickness=0)
canvas.config(bg="black")
canvas.grid() #print
w.configure(background='black')
w.update()
x1=0
x2=0
y1=0
y2=0
b=0


'''#sound
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
t=gTTS(text="Hello World.I am Pong Welcome to my game.",lang='en-us')
t.save("test.mp3")
dir_path=(dir_path+"\\test.mp3")
playsound(dir_path)
#playsound(,True)
winsound.PlaySound("C:\\Users\\sayantan\\Desktop\\01 Baby Ko Bass Pasand Hai - Sultan (Badshah) 190Kbps.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
os.remove(dir_path)
#end'''




class Ball:
    def __init__(self,canvas,paddle,color,c):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,240,225)
        start=[-3,-2,-1,1,2,3]
        self.x=random.choice(start)
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()  #window size height
        self.canvas_width=self.canvas.winfo_width()    #window size width
        self.hit_bottom=c
        self.point=0

    def box(self,pos):
        k=0
        global b
        global x2
        global x1
        global y1
        global y2
        if b==0:
            color=['snow', 'gainsboro', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2']
            c=random.choice(color)
            a=canvas.create_rectangle(x1,y1,x2,y2,fill=c)
            canvas.itemconfig(a,fill="black")
            x1=random.randint(0,410)
            x2=x1+90
            y1=random.randint(0,235)
            y2=y1+15
            a=canvas.create_rectangle(x1,y1,x2,y2,fill=c)
            
            b+=1
        if(pos[2]>=x1 and pos[0]<=x2):
            if(pos[1]<=y2 and pos[1]>=y1):
                self.y=3
                b=0
                self.point+=10
            elif(pos[3]>=y1 and pos[3]<=y2):
                self.y=-3
                b=0
                self.point+=10
        if self.point==0:
            r="00"
        else :
            r=self.point
        l1=Label(w,text=r,font=("Arial",20))
        l1.grid(column=0,row=505)

    def hit(self,pos):                                 #if ball hit the paddle
        paddle_pos=self.canvas.coords(self.paddle.id)
        if(pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]):
           if(pos[3]>=paddle_pos[1]and pos[3]<=paddle_pos[3]):
               return True#return array[x1,y1,x2,y2]
           return False
              



    def draw(self,c,p):#TO draw the ball move
        
        self.hit_bottom=c
        self.point=p
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)#return array[x1,y1,x2,y2]
        #print(pos)
        self.box(pos)

        if pos[1]<=0:      #top
            self.y=3
            
        if pos[3]>=self.canvas_height:  #bottom
            self.hit_bottom='t'
            a=[-1,-2,-3]
            self.y=random.choice(a)
        if pos[0]<=0:   #left
            self.x=3
        if pos[2]>=self.canvas_height:   #right
            self.x=-3
        if self.hit(pos)==True:   #BALL HIT THE PADDLE OR NOT
            a=[-1,-2,-3]
            self.y=random.choice(a)
    
class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(200,490,300,500,fill=color)
        self.canvas.move(self.id,0,0)
        self.x=0
        self.i=0
        self.canvas_height=self.canvas.winfo_height()  #window size height
        self.canvas_width=self.canvas.winfo_width()    #window size width
        w.bind("<Right>",self.right)
        w.bind("<Left>",self.left)
    def left(self,event):
        self.x=-(2+(int(self.i/10)))
    def right(self,event):
        self.x=(2+(int(self.i/10)))

    def draw(self,p):
        self.i=p
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:   #left
            self.x=0
        if pos[2]>=self.canvas_height:   #right
            self.x=0
        
    



paddle=Paddle(canvas,"Red")
        
ball=Ball(canvas,paddle,"Blue",'f')   #F FOR GAME OVER ENTER RESTART

def call():
    k=ball.point
    ball.draw('f',k)
    paddle.draw(k)
def calls():
    ball.draw('f',0)
    paddle.draw(0)
while True:
    if(ball.hit_bottom=='f'):
        call()
    else:
        s="Game Over \n points="+str(ball.point)+"\n Do you wanna retry?"
        a=tkinter.messagebox.askquestion("Score",s)
        if a=='yes':
            calls()
        else:
            w.destroy()
            quit()
            break
    w.update_idletasks()  #to update the idle
    w.update()#to update canvas window
    time.sleep(0.01)
