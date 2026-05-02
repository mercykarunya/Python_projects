from turtle import Turtle

class Scores(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-260,280)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"LEVEL = {self.level}", align="center", font=("Courier", 10, "bold"))
    
    def increment_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 20, "bold"))

    

        
