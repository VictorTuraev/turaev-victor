from tkinter import *
from random import randrange as rnd, choice
import time
k=0
root = Tk()
root.geometry('800x600')
l = Label(root, bg='black', fg='white', width=20)
l.pack()
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
colors = ['red','orange','yellow','green','blue','brown']
u=False
x1 = rnd(100,700)
y1= rnd(100,500)
x2 = rnd(100,700)
y2= rnd(100,500)
x3 = rnd(100,700)
y3= rnd(100,500)
r= rnd(30,50)
c1 = canv.create_oval(x1-r,y1-r,x1+r,y1+r,fill = choice(colors), width=0)
c2 = canv.create_oval(x2-r,y2-r,x2+r,y2+r,fill = choice(colors), width=0)
c3 = canv.create_oval(x3-r,y3-r,x3+r,y3+r,fill = choice(colors), width=0)
dx1 = rnd(-3,3)
dx2 = rnd(-3,3)
dx3 = rnd(-3,3)
dy1 = rnd(-3,3)
dy2 = rnd(-3,3)
dy3 = rnd(-3,3)


def new_ball():
	global x1, x2, x3, y1, y2, y3, r, dx1, dx2, dx3, dy1, dy2, dy3
	global u
	u=False
	x1=x1+dx1
	x2=x2+dx2
	x3=x3+dx3
	y1=y1+dy1
	y2=y2+dy2
	y3=y3+dy3
	canv.move(c1, dx1, dy1)
	canv.move(c2, dx2, dy2)
	canv.move(c3, dx3, dy3)
	if ((800-r<=x1) or(r>=x1)):
		dx1=-dx1
	
	if ((800-r<=x2) or(r>=x2)):
		dx2=-dx2
	
	if ((800-r<=x3) or(r>=x3)):
		dx3=-dx3
	
	if ((590-r<=y1) or(r>=y1)):
		dy1=-dy1
	
	if ((590-r<=y2) or(r>=y2)):
		dy2=-dy2
	
	if ((590-r<=y3) or(r>=y3)):
		dy3=-dy3
	
	root.after(10,new_ball)
		

def click(event):
	global k, x1, x2, x3, y1, y2, y3, r, c1, c2, c3, dx1, dx2, dx3, dy1, dy2, dy3
	global u
	click_x=event.x
	click_y=event.y
	ro1 = (click_x-x1)**2+(click_y-y1)**2
	ro2 = (click_x-x2)**2+(click_y-y2)**2
	ro3 = (click_x-x3)**2+(click_y-y3)**2
	ro = min(ro1, ro2, ro3)
	if ro<=r**2 and u==False:
		print('click')
		k=k+1
		l['text']=str(k)
		

		if ro==ro1:
			canv.delete(c1)
			x1 = rnd(100,700)
			y1= rnd(100,500)
			dx1 = rnd(-3,3)
			dy1 = rnd(-3,3)
			c1 = canv.create_oval(x1-r,y1-r,x1+r,y1+r,fill = choice(colors), width=0)
			u=False
		
		if ro==ro2:
			canv.delete(c2)
			x2 = rnd(100,700)
			y2 = rnd(100,500)
			dx2 = rnd(-3,3)
			dy2 = rnd(-3,3)
			c2 = canv.create_oval(x2-r,y2-r,x2+r,y2+r,fill = choice(colors), width=0)
			u=False

		if ro==ro3:
			canv.delete(c3)
			x3 = rnd(100,700)
			y3 = rnd(100,500)
			dx3 = rnd(-3,3)
			dy3 = rnd(-3,3)
			c3 = canv.create_oval(x3-r,y3-r,x3+r,y3+r,fill = choice(colors), width=0)
			u=False


			
	
	



new_ball()
canv.bind('<Button-1>', click)
mainloop()

