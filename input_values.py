#Returns user input in a dictionary
def data_retrieve():
	print(">>>LINE OF BEST FIT OF DATA<<<")
	print("==============================")
	print("")
	print("HELP:")
	print("=====")
	print("     e         > exit")
	print("     r         > remove")
	print("     [nothing] > next")
	print("")
	print("NOTE:")
	print("=====")
	print("It is recommended to put")
	print("the numbers on a similar")
	print("scale (largest number is")
	print("not completely different")
	print(") because I am not smart")
	print("")
	print("")
	print("==============================")
	
	#Data lists (dictionaries won't work because there maybe multple xs with the same value)
	data_x = []
	data_y = []
	
	#Temporary storage of input
	temp = ""
	
	#Input until user exits
	while temp != "e":
		x = input("X: ") + 0.0
		y = input("Y: ") + 0.0
		data_x.append(x)
		data_y.append(y)
		temp = "wait until input"
		while temp != "e" and temp != "r" and temp != "":
			temp = raw_input(">  ")
			print temp
			if temp == "r":
				data_x.pop()
				data_y.pop()
			if temp == "e" and len(data_x) == 1:
				print("Insufficient data")
				temp = "wait until input"
		
	#Return it
	return (data_x, data_y)

#The line of best fit thingy
def line():
	#Get the data
	(data_x, data_y) = data_retrieve()
	
	#Set up averages
	x_average = 0.0
	y_average = 0.0
	
	#Iterate through the lists
	for count in range(0, len(data_x)):
		x_average = x_average + data_x[count]
		y_average = y_average + data_y[count]
	
	#Average it out
	x_average = x_average / len(data_x)
	y_average = y_average / len(data_y)
	
	#Set up sums
	sum1 = 0.0
	sum2 = 0.0
	sum3 = 0.0
	
	for count in range(0, len(data_x)):
		sum1 = sum1 + (data_x[count] - x_average) * (data_y[count] - y_average)
		sum2 = sum2 + (data_x[count] - x_average) * (data_x[count] - x_average)
		sum3 = sum3 + (data_y[count] - y_average) * (data_y[count] - y_average)
	
	#Setup correlation coefficient
	correlation = 0.0
	correlation = sum1 / ((sum2 ** 0.5) * (sum3 ** 0.5))
	
	#Calculate Gradient and intercept
	gradient = sum1 / sum2
	intercept = y_average - gradient * x_average
	
	#Print the equation
	print(" ")
	print("The equation is:")
	if intercept > 0:
		print("y = " + str(gradient) + "x" + " + " + str(intercept))
	elif intercept == 0:
		print("y = " + str(gradient) + "x")
	else:
		print("y = " + str(gradient) + "x " + " - " + str(abs(intercept)))
		
	return (gradient, intercept, data_x, data_y, x_average, y_average, correlation)
