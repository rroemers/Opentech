import turtle
import math
turtle.shape("turtle")
turtle.color('green')
side = 50
roof = math.sqrt(side**2 + side**2)
anglebase = 20
square_angle = 90

#draw base
turtle.forward(side)
turtle.left(square_angle)
turtle.forward(side)
turtle.left(square_angle)
turtle.forward(side)
turtle.left(square_angle)
turtle.forward(side)
turtle.left(square_angle)

#rotate diagonal up and move to right top

turtle.left(45)
turtle.forward(75)

#draw roof

turtle.left(square_angle)
turtle.forward(roof)
turtle.left(square_angle)
turtle.forward(roof)
turtle.left(square_angle)
turtle.forward(roof)
turtle.left(square_angle)


turtle.exitonclick()