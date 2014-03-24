import turtle

side_l = 50 #side lenght
side_s = 6 #side number
side_a = 60 #side angle

shape_n = 3 #number of shapes

def draw_side():
	turtle.forward(side_l)
	turtle.left(side_a)

for n in range(shape_n):
	for h in range(side_s):
		draw_side()
	turtle.forward(side_l)

turtle.exitonclick()