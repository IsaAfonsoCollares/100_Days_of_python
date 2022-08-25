from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.score = 0
        self.color("purple")
        self.setheading(90)
        self.penup()
        self.setposition(0, -260)

    def move(self):
        self.forward(40)

    def reset_position(self):
        self.goto(0, -260)
