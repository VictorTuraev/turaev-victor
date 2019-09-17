import turtle
for i in range(11):
    a=10/2**0.5
    turtle.right(135)
    turtle.penup()
    turtle.forward(10)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(50+2*i*a)
    turtle.right(90)
    turtle.forward(50+2*i*a)
    turtle.right(90)
    turtle.forward(50+2*i*a)
    turtle.right(90)
    turtle.forward(50+2*i*a)
    turtle.right(180)
input()
