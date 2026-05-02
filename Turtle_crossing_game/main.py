# create the screen
# create the turtle player
# To make the player move up
# To detect turtle reaches the end
# To create cars


from turtle import Screen
from player import Player
from score import Scores
from car import Cars
import time

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("white")
sc.title("TURTLE CROSSING GAME")
sc.tracer(0)

player = Player()
score = Scores()
car = Cars()

sc.listen()
sc.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    sc.update()
    car.create_car()
    car.move_cars()

    #check if the turtle crosses the road
    if player.ycor() > 280:
        player.collision()
        score.increment_level()
        car.increase_speed()

    #check if the turtle hits the car
    for c in car.all_cars:
        if player.distance(c) < 20:
            game_is_on = False
            score.game_over()
        


sc.exitonclick()