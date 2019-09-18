import turtle
import math
f=1
k=1
n=1000
for i in range(n):
    turtle.goto(k*f*math.cos(f),k*f*math.sin(f))
    f=f+2/(k*f)

    
    
    
    
