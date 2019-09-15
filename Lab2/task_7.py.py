import turtle
import math
turtle.speed(0)
r=3
d=1
turtle.forward(r)
n=100000000
s=2*math.pi/360
for i in range(n):
    l=r**2+(r+d)**2-2*r*(r+d)*math.cos(s)
    c=180/math.pi*math.acos((r**2+l**2-(r+d)**2)/(2*r*l))
    turtle.left(c)
    r=r+d
    turtle.forward(l)
    turtle.right(c-s*180/math.pi)
    
    
    
    
