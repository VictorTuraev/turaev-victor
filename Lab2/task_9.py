import turtle
import math
n=10
k=3
r=50*3**(-0.5)
l=10

for i in range(n):
    for i in range(k):
        turtle.left(180-(90-360/k/2))
        turtle.forward(r)
        turtle.right(90-360/k/2)
    k=k+1
    r=r+l
    turtle.penup()
    turtle.forward(l)
    turtle.pendown()
    
        
        
    
    
    
    
    
