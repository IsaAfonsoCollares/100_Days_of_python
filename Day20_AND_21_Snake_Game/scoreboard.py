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
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


