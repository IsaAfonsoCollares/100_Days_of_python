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
        self.setposition(270, randint(-270, 270))
        self.move_speed = 0.1

    def move(self):
        self.forward(5)
