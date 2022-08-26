from turtle import Turtle

ALIGNMENT = "Center"
FONT = ["Arial", "12", "bold"]


class State(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.name = ""
        self.color("black")

    def create_state(self, name, x_position, y_position):
        self.name = name
        self.goto(x_position,y_position)

    def found(self):
        self.write(self.name, align=ALIGNMENT, font=FONT)
