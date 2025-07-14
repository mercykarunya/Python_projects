# TODO: To draw a random line

from turtle import Turtle, Screen
import random

#color_lst = ['medium blue','gray','lime green','dark goldenrod','tomato', 'light coral','purple','plum','indigo','dark slate blue','lavender','sienna']
directions = [0,90,120,270]

td = Turtle()
sc = Screen()
sc.colormode(255) # Here we are setting the colormode so that color could be given in numbers the return statement work because of it

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    r_c = (r, b, g)
    return r_c

td.pensize(7) #for the bigger pen size
td.speed(0) # To speed up the process '0' is the fastest
for i in range(50):
    td.forward(30)
    td.color(random_colors())
    td.setheading(random.choice(directions))
    

sc.exitonclick()


