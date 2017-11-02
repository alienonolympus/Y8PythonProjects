#Import everything
from turtle import *
from time import sleep

#Move without drawing
def move(x, y):
	up()
	goto(x, y)
	down()

#Draw two circles
def two_circles(x, y, size, pen, colour):
	for count in range(2):
		color(colour, 'beige')
		pensize(pen)
		move(x + 80 * count, y)
		circle(size)

#Polygon
def polygon(sides, length, amount):
	for count in range(amount):
		right(360 / amount)
		for count in range(sides):
			forward(length)
			left(360 / sides)

#Draw a smiley face
def smiley():
	#Setup
	hideturtle()
	color('black', 'beige')
	pensize(5)
	
	#Face
	move(0, -100)
	begin_fill()
	circle(100)
	end_fill()

	#Eyes
	two_circles(-40, 30, 5, 15, 'black')
	two_circles(-35, 35, 1, 5, 'white')

	#Nose
	color('black', 'beige')
	move(0, 20)
	goto(-3, -20)
	goto(3, -16)

	#Mouth
	move(-15, -70)
	right(10)
	circle(57.2957795, 75)

	#Cheek
	move(45, -20)
	right(140)
	for count in range(20): #For slower speed
		forward(1)
		left(4)

#Bounce
def bounce(height, rise):
	if(rise):
		#Rise
		setheading(90)
		count = 1.2 + height / -120
		while(ycor() < height):
			sleep(0.0005)
			forward(12 / count)
			count = count + 1.2 / (0.00012 - height)
	
	#Fall
	setheading(270)
	count = 0
	while(ycor() > -325):
		forward(0.012 * count * count)
		sleep(0.0005)
		count = count + 0.5
		
#Animation
def animation():
	#Setup
	color('green')
	clear()
	shape('circle')
	setheading(270)
	
	#Quickly draw line
	speed(300)
	pensize(50)
	move(-400, -350)
	setheading(0)
	forward(800)
	up()
	color('black', 'black')
	showturtle()
	
	#Fall
	goto(0, 275)
	speed(10)
	bounce(0, False)
	
	#Bouncing
	bounce(-25, True)
	bounce(-175, True)
	bounce(-250, True)
	bounce(-300, True)
	bounce(-312.5, True)
	bounce(-318.75, True)
	bounce(-320, True)
		
#Letters
def it(x, y, bottom):
	move(x, y)
	goto(x + 20, y)
	goto(x + 10, y)
	goto(x + 10, y - 40)
	if(bottom):
		goto(x, y - 40)
		goto(x + 20, y - 40)

def l(x, y):
	move(x, y)
	goto(x, y - 40)
	goto(x + 20, y - 40)

def u(x, y):
	move(x, y)
	goto(x, y - 40)
	goto(x + 20, y - 40)
	goto(x + 20, y)

def mna(x, y, middle, across):
	move(x, y)
	goto(x, y - 40)
	goto(x, y)
	goto(x + 20, y)
	goto(x + 20, y - 40)
	if(middle):
		move(x + 10, y)
		goto(x + 10, y - 40)
	if(across):
		move(x, y - 20)
		goto(x + 20, y - 20)

def cod(x, y, right, diag):
	move(x, y)
	goto(x, y - 40)
	if(diag):
		goto(x + 10, y - 40)
	else:
		goto(x + 20, y - 40)
		
	move(x, y)
	goto(x + 20, y)
	
	if(right or diag):
		goto(x + 20, y - 30)
		if(diag):
			goto(x + 10, y - 40)
		else:
			goto(x + 20, y - 40)

def efr(x, y, e, r):
	move(x, y)
	goto(x, y - 40)
	move(x, y)
	goto(x + 20, y)
	move(x + 20, y - 20)
	goto(x, y - 20)
	if(e):
		move(x, y - 40)
		goto(x + 20, y - 40)
	if(r):
		goto(x + 20, y - 40)
		move(x + 20, y)
		goto(x + 20, y - 20)

#Illuminati confirmed
def illuminati():
	#Setup
	pensize(5)
	hideturtle()
	color('black', 'light green')
	clear()
	move(-100, -80)
	setheading(0)

	#Triangle
	begin_fill()
	polygon(3, 200, 1)
	end_fill()
	
	#The All-Knowing-Eye (white)
	color('black', 'white')
	begin_fill()
	move(-53, -5)
	setheading(60)
	circle(-63.5, 120)
	setheading(240)
	circle(-63.5, 120)
	end_fill()
	
	#The missing eyeball
	move(1.99,-31.25)
	setheading(0)
	color('black', 'black')
	begin_fill()
	circle(25)
	end_fill()
	
	#Illuminati
	it(-145, 200, True)
	l(-115, 200)
	l(-85, 200)
	u(-55, 200)
	mna(-25, 200, True, False)
	it(5, 200, True)
	mna(35, 200, False, False)
	mna(65, 200, False, True)
	it(95, 200, False)
	it(125, 200, True)
	
	#Confirmed
	cod(-130, -180, False, False)
	cod(-100, -180, True, False)
	mna(-70, -180, False, False)
	efr(-40, -180, False, False)
	it(-10, -180, True)
	efr(20, -180, False, True)
	mna(50, -180, True, False)
	efr(80, -180, True, False)
	cod(110, -180, False, True)

#Main driver function
def main():
	#Draw!
	smiley()

	#Wait for it
	sleep(1)

	#Ball
	animation()

	#Wait for it (again)
	sleep(1)

	#Illuminati Confirmed!!!
	illuminati()

	#Done!
	done()
	
main()
