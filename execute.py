#Import from file and libraries
from input_values import line
from math import *
from turtle import *

#Set up global variables
(gradient, intercept, data_x, data_y, x_average, y_average, correlation) = line()

#Find a nice number to be the last number of the graph
last_value = max(max(data_x), max(data_y))
digits = len(str(int(last_value)))
last_value = last_value + 10 ** (digits - 2)
last_value = int(round(last_value, 2 - digits))
while last_value % 10 != 0:
	last_value = last_value + 1
scale = 250.0 / last_value

#Make coordinates easier to manage
setworldcoordinates(-30, -30, 300, 300)


#Moving to somewhere
def move(xcoord, ycoord):
	up()
	goto(xcoord, ycoord)
	down()

#Correlation coefficient
def correlation_coefficient():
	print("")
	print("The correlation coefficient is: " + str(correlation))
	if -1 <= correlation < -0.65:
		print("As a result, the data has strong negative correlation")
	elif -0.65 <= correlation < -0.35:
		print("As a result, the data has weak negative correlation")
	elif -0.35 <= correlation < 0.35:
		print("As a result, the data has no obvious correlation")
	elif 0.35 <= correlation < 0.65:
		print("As a result, the data has weak positive correlation")
	elif 0.65 <= correlation <= 1:
		print("As a result, the data has strong positive correlation")
	else:
		print("This is unreachable. Something is wrong with this program.")

#Graph
def graph():
	#Setup
	color('black')
	speed(0)
	hideturtle()
	pensize(5)

	#Y Axis
	move(0, -5)
	goto(0, 290)
	move(-5, 285)
	goto(0, 290)
	goto(5, 285)

	#X Axis
	move(-5, 0)
	goto(290, 0)
	move(285, -5)
	goto(290, 0)
	goto(285, 5)
	
	#Grid
	pensize(1)
	for count in range(1, 12):
		move(25 * count, 0)
		goto(25 * count, 290)
		move(0, 25 * count)
		goto(290, 25 * count)
		
	#Origin
	move(-5, -12)
	write("0", False, align="center", font=("Arial", 16, "bold"))

#Write numbers
def label():
	for count in range(25, 276, 25):
		move(count, -15)
		write(str(last_value * (count / 25)  / 10), False, align="center", font=("Arial", 16, "bold"))
		move(-15, count - 8)
		write(str(last_value * (count / 25)  / 10), False, align="center", font=("Arial", 16, "bold"))

def plot():
	color('red')
	pensize(2)
	for count in range(0, len(data_x)):
		move(data_x[count] * scale - 0.2, data_y[count] * scale - 2.5)
		begin_fill()
		circle(3)
		end_fill()

def draw_line():
	#Setup
	color('black')
	pensize(2)
	
	#Starting point
	move(0, intercept * scale)
	
	#Gradient
	setheading((360 / (2 * pi)) * atan(gradient))
	if ycor() >= 0:
		back(5)
		forward(5)
	
	while (xcor() < 290.0):
		up()
		if -5.0 < ycor() < 290.0:
			down()
		forward(2)
		
	move(0, 0)

#Draw it
def main():
	correlation_coefficient()
	graph()
	label()
	plot()
	draw_line()
	done()

main()
