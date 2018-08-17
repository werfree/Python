import turtle
from turtle import *
import random,time

speed(0)
penup()
goto(-180,140)
w=turtle.Screen()
w.title("Turtle Race")
time.sleep(5)
for i in range(21):
    write(i, align="center")
    right(90)
    forward(10)
    pendown()
    forward(180)
    penup()
    backward(190)
    left(90)
    forward(20)
    
rT=Turtle()
rT.color("red")
rT.shape("turtle")
rT.penup()
rT.goto(-180,100)
bT=Turtle()
bT.color("Blue")
bT.shape("turtle")
bT.penup()
bT.goto(-180,60)
gT=Turtle()
gT.color("green")
gT.shape("turtle")
gT.penup()
gT.goto(-180,20)
yT=Turtle()
yT.color("purple")
yT.shape("turtle")
yT.penup()
yT.goto(-180,-20)
rT.pendown()
bT.pendown()
gT.pendown()
yT.pendown()
a=[1,2,3,4,5]
def p(x,y):
    rT.goto(-180,100)
    bT.goto(-180,60)
    gT.goto(-180,20)
    yT.goto(-180,-20)
    for i in range (132):
        
        '''rT.forward(random.randint(1,5))
        bT.forward(random.randint(1,5))
        gT.forward(random.randint(1,5))
        yT.forward(random.randint(1,5))'''
        rT.penup()
        bT.penup()
        gT.penup()
        yT.penup()
        rT.forward(random.choice(a))
        bT.forward(random.choice(a))
        gT.forward(random.choice(a))
        yT.forward(random.choice(a))
    r=rT.xcor()
    b=bT.xcor()
    g=gT.xcor()
    y=yT.xcor()
    s=[]
    s.append(r)
    s.append(b)
    s.append(g)
    s.append(y)
    s.sort(reverse=True)
    k=["FIRST","SECOND","THIRD","FORTH"]
    print(s)
    for i in range(4):
        if s[i]==r:
            m="  RED TURTLE"
        elif s[i]==b:
            m="  BLUE TURTLE"
        elif s[i]==g:
            m="  GREEN TURTLE"
        elif s[i]==y:
            m="  PURPLE TURTLE"
        print("{}:{}".format(k[i],m))
w.onclick(p)
