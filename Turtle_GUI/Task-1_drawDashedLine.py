from turtle import Turtle, Screen

tim = Turtle()

# TODO: To draw the dashed line
for _ in range(15):
    tim.fd(8)
    # penup() -> No drawing will happen when the turtle moves
    tim.penup()
    tim.fd(8)
    # pendown() -> The turtle will draw as it moves
    tim.pendown()

sc = Screen()
sc.exitonclick()