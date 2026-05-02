#Pong Game is a Arcade game
#Workflow of this project will be
#1. Create the screen
#2. create and move a paddle
#3. create another paddle
#4. create the ball and make it move
#5. detect collision with wall and bounce
#6. detect collision with paddle
#7. detect when paddle misses
#8. Keep score

from turtle import Screen
import time
from Paddle import create_paddle
from Ball import create_ball
from scoreboard import Scoreboard

screen  = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = create_paddle((350,0))
l_paddle = create_paddle((-350,0))
ball = create_ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecs collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detect collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    #detect collsion with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect if right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #detect of left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()