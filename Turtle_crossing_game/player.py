from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0,-270)
        self.setheading(90)
        self.move_y = 10

    def move(self):
        move_player = self.ycor() + self.move_y
        self.goto(self.xcor(), move_player)

    def collision(self):
        self.goto(0,-270)

        
