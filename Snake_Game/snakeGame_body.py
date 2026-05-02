# Snake Game Project
# The steps need to be done to complete the snake game project
# 1. Create a Snake body
# 2. Move the Snake
# 3. Create Snake Food
# 4. Detect collision with food
# 5. Create a scorecard
# 6. Detect collision with wall
# 7. Detect collision with tail

from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Score import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black") # To create a black screen
screen.title("My Snake Game") # This title will show up in the turtle screen
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    
    #To detect the collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increaseScore()
        snake.extent_body()

    #To detect the collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 280 or snake.head.ycor() < -270:
        game_is_on = False
        score.game_over()

    #To detect the collision with the tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()
        
screen.exitonclick()