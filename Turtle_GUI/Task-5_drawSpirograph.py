# TODO: To draw a Spirograph
from turtle import Turtle, Screen
import random

tim = Turtle()
sc = Screen()
sc.colormode(255)
tim.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    r_c = (r, g, b)
    return r_c


def draw_spirograp(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100) # To draw a circle this 100 is the width or circumference
        tim.setheading(tim.heading()+ size_of_gap) # heading is used to return the current angle of the turle
        # By using setheading we can change the angle

draw_spirograp(3)

sc.exitonclick()