import turtle

side_l = 50 #side lenght
side_s = 6 #side number
side_a = 60 #side angle

shape_n = 1 #number of shapes

def draw_side():
	turtle.forward(side_l)
	turtle.left(side_a)

for h in range(side_s):
	draw_side()

turtle.exitonclick()