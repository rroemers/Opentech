import turtle
x=10
	
for _ in range(10):
	turtle.forward(x)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()
	x = x + 2

turtle.exitonclick()