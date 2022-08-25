from turtle import Turtle
FONT = ('Arial', 12, 'bold')
ALIGNMENT = "center"


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def draw_line(self,y_position):
        self.setposition(-350, y_position)
        self.color("white")
        self.pendown()
        self.speed(0)
        self.forward(700)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Level {self.score}", align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.l_score < self.r_score:
            self.setposition(0, 0)
            self.write(f"Game over!\n Player 2 wins!", align=ALIGNMENT, font=FONT)

        elif self.l_score > self.r_score:
            self.setposition(0, 0)
            self.write(f"Game over!\n Player 1 wins!", align=ALIGNMENT, font=FONT)