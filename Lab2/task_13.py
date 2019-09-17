import turtle
import math
turtle.speed(0)
turtle.left(90)
def face():
    turtle.circle(100)
def eyes():
    turtle.penup()
    turtle.goto(-45,50)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(-145,50)
    turtle.pendown()
    turtle.circle(5)
def nose():
    turtle.penup()
    turtle.goto(-100,-10)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
def smile():
    turtle.goto(-75,-50)
    turtle.right(180)
    r=25
    turtle.pendown()
    for i in range(180):
        turtle.forward(r*math.sin(math.pi/180))
        turtle.right(1)

    
        
        
    
    
    
    
    
