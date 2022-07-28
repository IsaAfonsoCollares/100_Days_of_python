from turtle import Turtle
FONT = ('Arial', 12, 'bold')
ALIGNMENT = "center"


class Player(Turtle):
    def __init__(self, player_name, x_position):
        super().__init__()
        self.speed(10)
        self.score = 0
        self.penup()
        self.setposition(x_position, 280)
        self.hideturtle()
        self.color("white")
        self.write(f"{player_name}", align=ALIGNMENT, font=FONT)


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(-350, 260)
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
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-320, 262)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(320, 262)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.l_score < self.r_score:
            self.setposition(0, 0)
            self.write(f"Game over!\n Player 2 wins!", align=ALIGNMENT, font=FONT)

        elif self.l_score > self.r_score:
            self.setposition(0, 0)
            self.write(f"Game over!\n Player 1 wins!", align=ALIGNMENT, font=FONT)