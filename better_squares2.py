import turtle
side = 50		#Define base of square
s_angle = 90	#Define angle for square
t_angle = 20	#Define twist
cubes = 5		#Number of iterations

def draw_line():
	turtle.forward(side)
	turtle.left(s_angle)

def draw_cube():
	for count in range(4):
		draw_line()

for c in range(cubes):	#Tilt the arrow
	turtle.right(t_angle)
	draw_cube()

turtle.exitonclick()