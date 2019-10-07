import graphics as gr
import math
win=gr.GraphWin("rm", 500, 500)
dt=0.01
a=0
v=50
def may(x, y, r):
	nit=gr.Line(gr.Point(250, 10), gr.Point(x, y))
	nit.draw(win)
	circle=gr.Circle(gr.Point(x, y), r)
	circle.setFill("black")
	circle.draw(win)

def change(a, v, r)
	k=v*dt/r
	b=-g*math.sin(a)
	a=a+k
	v=v+b
def mv(r):
	x=r*math.sin(a)+250
	y=r*math.cos(a)+10
	nit.undraw
	circle.Move(x, y)
	nit.draw(gr.point(250, 10), gr.point(x, y)
win.getMouse()
win.close

