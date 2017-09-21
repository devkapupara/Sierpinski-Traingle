import turtle
import random

col = ["red","mediumseagreen","yellow","magenta","orange","purple","dodgerblue","springgreen"]

def drawMain():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.setpos(-200,-150)
    t.pendown()
    for i in range(3):
        t.forward(400)
        t.left(120)
    t.penup()

def drawSmall(depth,initx,inity,side):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    if depth == 0:
        t.penup()
    else:
        t.penup()
        x,y = midpoint(initx, inity, initx + side, inity)
        t.setpos(x,y)
        t.pendown()
        t.color(col[random.randint(0,len(col)-1)])
        t.begin_fill()
        t.left(60)
        t.forward(side/2)
        for i in range(2):
            t.left(120)
            t.forward(side/2)
        t.end_fill()
        drawSmall(depth-1,initx,inity,side/2)
        drawSmall(depth-1,x,y,side/2)
        drawSmall(depth-1,(4*initx + side)/4,(4*inity+(3**0.5)*side)/4,side/2)

def midpoint(x1,y1,x2,y2):
    return((x1+x2)/2,(y1+y2)/2)

def Sierpinski(depth):
    turtle.bgcolor("lightgrey")
    drawMain()
    drawSmall(depth,-200,-150,400)

if __name__ == "__main__":
    depth = int(input("Enter Depth: "))
    Sierpinski(depth)
        
        
