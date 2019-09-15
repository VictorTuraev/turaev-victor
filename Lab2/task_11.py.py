import turtle
import math
r=50
n=10
turtle.speed(0)
turtle.right(90)
for i in range(n):
    turtle.circle(r)
    turtle.right(0.5)
    for i in range(360):
        turtle.forward(r*math.sin(math.pi/180))
        turtle.right(1)
    turtle.right(0.5)
    r=r+20
    
        
        
    
    
    
    
    
