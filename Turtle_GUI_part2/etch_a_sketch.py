# To sketch up using the keys in the keyboards using the event listner menthod
# w = forward
# s = backward
# a = counter-clockwise
# d = clockwise
# c = clear drawing
from turtle import Turtle, Screen

tim = Turtle()
s = Screen()
s.listen()

# for forward
def forward():
    tim.forward(30)
#for backward
def backward():
    tim.backward(30)
#for right
def right():
    tim.right(45)
#for left
def left():
    tim.left(45)
#circle
def circle():
    tim.circle(50)
#clear drawing
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

s.onkey(forward,"f")
s.onkey(backward,"b")
s.onkey(right,"r")
s.onkey(left,"l")
s.onkey(circle,"c")
s.onkey(clear_drawing,"space")

s.exitonclick()
