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
        self.y_move = 10

    def move(self):
        self.forward(40)

