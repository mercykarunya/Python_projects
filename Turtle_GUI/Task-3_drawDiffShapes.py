from turtle import Turtle, Screen
import random

# TODO: To draw diff shapes like triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
t = Turtle()
color_lst = ['medium blue','gray','lime green','dark goldenrod','tomato', 'light coral','purple','plum','indigo','dark slate blue','lavender','sienna']

for i in range(3,11):
    t.color(random.choice(color_lst))
    for j in range(0,i):
        t.forward(100)
        t.right(360/i)

s = Screen()
s.exitonclick()