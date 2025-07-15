from turtle import Turtle, Screen
import random

s = Screen()
is_race_start = False
s.setup(width=600,height=500) #To set the size of the screen
#To show the popup on the screen
user_bet = s.textinput(title="Make a bet",prompt="which Turtle is going to win? what color do you want?")
colors = ['red', 'green', 'orange', 'yellow', 'purple', 'blue']
y_pos = [-100, -60, -20, 20, 60, 100]
all_turtle = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x= -270, y=y_pos[index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_start = True

while is_race_start:

    for tur in all_turtle:
        if tur.xcor()>260:
            is_race_start = False
            winning_color = tur.pencolor()
            if winning_color==user_bet:
                print(f"You got winnn!!, The {winning_color} Turtle is a winner")
            else:
                print(f"You lost, The {winning_color} Turtle is a winner")
        distance = random.randint(0,10)
        tur.forward(distance)


s.exitonclick()