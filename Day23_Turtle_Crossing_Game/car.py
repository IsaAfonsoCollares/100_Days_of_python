from turtle import Turtle
from random import randint, choice


colors = ["white", "green", "blue", "red", "pink", "yellow"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        color_choice = choice(colors)
        self.color(color_choice)
        self.penup()
        self.setheading(180)
        self.y_position = 0
        self.y_move = 2

    def initial_position(self, y_position):
        self.y_position = y_position
        self.setposition(randint(-250, 350), self.y_position)

    def move(self):
        self.forward(self.y_move)

    def reset_position(self):
        color_choice = choice(colors)
        self.color(color_choice)
        self.goto(300, self.y_position)
