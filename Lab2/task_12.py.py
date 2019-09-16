import turtle
import math
r=50
t=10
n=10
turtle.left(90)
turtle.speed(0)
for i in range(n):
    for i in range(180):
        turtle.forward(r*math.sin(math.pi/180))
        turtle.right(1)
    turtle.right(0.5)
    for i in range(180):
        turtle.forward(t*math.sin(math.pi/180))
        turtle.right(1)
    turtle.right(0.5)
    
    
    



    
        
        
    
    
    
    
    
