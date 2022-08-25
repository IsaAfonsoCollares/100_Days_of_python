from turtle import Turtle
FONT = ('Arial', 12, 'bold')
FONT2 = ('Arial', 24, 'bold')
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
        self.write(f"Level {self.score}", align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0, 0)
        self.color("white")
        self.write(f"Game Over! Level {self.score}", align=ALIGNMENT, font=FONT2)
