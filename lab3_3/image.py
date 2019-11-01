import graphics as gr
import math
win = gr.GraphWin("mayatnik", 500, 500)
dt = 10
a = 0
v = 0.01
r = 20
l=200
x=250
y=10+l*math.cos(a)

nit = gr.Line(gr.Point(250, 10), gr.Point(x, y))
nit.draw(win)
circle = gr.Circle(gr.Point(x, y), r)
circle.setFill("black")
circle.draw(win)


def change():
	global a, v
	a=a+v*dt/r
	v=v-0.01*math.sin(a)
	return a

	
def mv(a):
	global nit, circle, x, y, l
	a = change()
	x=l*math.sin(a)+250
	y=l*math.cos(a)+10
	nit.undraw()
	circle.undraw()
	circle.move(x, y)
	
	nit = gr.Line(gr.Point(250, 10), gr.Point(x, y))
	nit.draw(win)
	
	
	circle = gr.Circle(gr.Point(x, y), r)
	circle.setFill("black")
	circle.draw(win)
	
def main():
	for i in range(500):
		change()
		mv(a)
		gr.time.sleep(0.1)
main()


