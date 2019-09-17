import turtle
turtle.left(90)
for i in range(10)
    turtle.circle(50+i*20)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100+2*i*20)
    turtle.circle(50+i*20)
    turtle.backward(100+2*i*20)
    turtle.left(90)
    
