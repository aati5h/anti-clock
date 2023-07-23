from turtle import *
from datetime import datetime

t = Turtle()
wn = Screen()
myobj=datetime.now()
h=myobj.hour
m=myobj.minute
s=myobj.second

wn.title("Anti-Clock")
wn.bgcolor("#F7A1C4")
wn.setup(600, 600)
t.speed(1000)
t.pensize(3)
#t.hideturtle()
#w.tracer(0)

def draw_clock(t,h,m,s):
    t.penup()
    t.goto(0,210)
    t.setheading(180)
    t.pencolor('#DF2935')
    t.pendown()
    t.circle(210)

    t.penup()
    t.goto(0,0)
    t.setheading(90)

    for _ in range (12):
        t.forward(190)
        t.pendown()
        t.fd(20)
        t.penup()
        t.goto(0,0)
        t.right(30)

    t.penup()
    t.goto(0,0)
    t.setheading(90)
        
    for _ in range (60):
            t.forward(200)
            t.pendown()
            t.fd(10)
            t.penup()
            t.goto(0,0)
            t.right(6)

    #11
    t.goto(0,0)
    t.setheading(65)
    t.fd(145)
    t.setheading(0)
    t.fd(20)
    t.write("11",move=False,align="left",font=('Arial',20,'normal'))

    #10
    t.goto(0,0)
    t.setheading(35)
    t.fd(142)
    t.setheading(0)
    t.fd(23)
    t.write("10",move=False,align="left",font=('Arial',20,'normal'))
    
    #9
    t.goto(0,0)
    t.setheading(0)
    t.fd(145)
    t.setheading(0)
    t.fd(20)
    t.write("9",move=False,align="left",font=('Arial',20,'normal'))
  
    #8
    t.goto(0,0)
    t.setheading(320)
    t.fd(160)
    t.setheading(0)
    t.fd(20)
    t.write("8",move=False,align="left",font=('Arial',20,'normal'))

    #7
    t.goto(0,0)
    t.setheading(295)
    t.fd(180)
    t.setheading(0)
    t.fd(4)
    t.write("7",move=False,align="left",font=('Arial',20,'normal'))
    
    #6
    t.goto(0,0)
    t.setheading(262)
    t.fd(180)
    t.setheading(0)
    t.fd(20)
    t.write("6",move=False,align="left",font=('Arial',20,'normal'))
    
    #5
    t.goto(0,0)
    t.setheading(235)
    t.fd(188)
    t.setheading(0)
    t.fd(20)
    t.write("5",move=False,align="left",font=('Arial',20,'normal'))

    #4
    t.goto(0,0)
    t.setheading(210)
    t.fd(193)
    t.setheading(0)
    t.fd(20)
    t.write("4",move=False,align="left",font=('Arial',20,'normal'))

    #3
    t.goto(0,0)
    t.setheading(183)
    t.fd(190)
    t.setheading(0)
    t.fd(20)
    t.write("3",move=False,align="left",font=('Arial',20,'normal'))
    
    #2
    t.goto(0,0)
    t.setheading(157)
    t.fd(184)
    t.setheading(0)
    t.fd(20)
    t.write("2",move=False,align="left",font=('Arial',20,'normal'))

    #1
    t.goto(0,0)
    t.setheading(130)
    t.fd(180)
    t.setheading(0)
    t.fd(20)
    t.write("1",move=False,align="left",font=('Arial',20,'normal'))

    #12
    t.goto(0,0)
    t.setheading(100)
    t.fd(170)
    t.setheading(0)
    t.fd(20)
    t.write("12",move=False,align="left",font=('Arial',20,'normal'))
    
    t.goto(0,0)
    t.setheading(90)
    t.pendown()

    t.pu()
    t.goto(0,0)
    t.pencolor('red')
    t.setheading(90)
    angle=((12-h)/12)*360
    t.right(angle)
    t.pendown()
    t.fd(60)
    
    t.pu()
    t.goto(0,0)
    t.pencolor('blue')
    t.setheading(90)
    angle=((60-m)/60)*360
    t.right(angle)
    t.pendown()
    t.fd(80)

    t.pu()
    t.goto(0,0)
    t.pencolor('green')
    t.setheading(90)
    angle=((60-s)/60)*360
    t.right(angle)
    t.pendown()
    t.fd(100)
    
    mainloop()

draw_clock(t,h,m,s)
