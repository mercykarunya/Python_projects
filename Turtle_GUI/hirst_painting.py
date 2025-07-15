# colorgram.py is a Python library that lets you extract colors from images
# import colorgram
# colors = colorgram.extract(r"C:\Users\mercy karunya\OneDrive\Desktop\PythonProjects\Turtle_GUI\image.jpg", 30)
# lst_of_colors = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     lst_of_colors.append(new_color)

# print(lst_of_colors

# After extrcting colors using colorgram need to create a list 
from turtle import Turtle, Screen
import random
t = Turtle()
s = Screen()
s.colormode(255)
t.speed(0)
t.penup()
t.hideturtle
color_lst = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)] 


t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_counts = 100

for dot_count in range(1, number_of_counts+1):
    t.dot(20,random.choice(color_lst))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

s.exitonclick()