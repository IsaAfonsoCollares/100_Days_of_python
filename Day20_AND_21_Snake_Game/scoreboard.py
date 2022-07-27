from turtle import Turtle

FONT = ('Arial', 12, 'bold')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.setposition(0, 280)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

