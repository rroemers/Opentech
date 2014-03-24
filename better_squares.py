import turtle
side = 50		#Define base of square
s_angle = 90	#Define angle for square
t_angle = 20	#Define twist
cubes = 30		#Number of iterations

for c in range(cubes):	#Tilt the arrow
	turtle.right(t_angle)

	for s in range(4): #Draw one square
		turtle.forward(side)
		turtle.left(s_angle)
	
turtle.exitonclick()