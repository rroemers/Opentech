import turtle

def line_without_moving():
		turtle.forward(50)
		turtle.backward(50)

for i in range(10):
	line_without_moving()

turtle.exitonclick()