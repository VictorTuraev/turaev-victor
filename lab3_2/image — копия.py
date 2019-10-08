import graphics as gr
import math
win = gr.GraphWin("mayatnik", 500, 500)
dt = 0.01
a = 0
v = 50
r = 20
x=250
y=10+r*math.cos(a)
def may(x, y):
	nit = gr.Line(gr.Point(250, 10), gr.Point(x, y))
	nit.draw(win)
	circle = gr.Circle(gr.Point(x, y), r)
	circle.setFill("black")
	circle.draw(win)
may(250, 20)
win.getMouse()
win.close()



