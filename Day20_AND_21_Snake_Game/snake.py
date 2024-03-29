from turtle import Turtle
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        new_part = Turtle("square")
        new_part.penup()
        new_part.color("white")
        new_part.setposition(position)
        self.body.append(new_part)

    def extend(self):
        self.add_part(self.body[-1].position())

    def move(self):
        for part in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part - 1].xcor()
            new_y = self.body[part - 1].ycor()
            self.body[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset_snake(self):
        for body_part in self.body:
            body_part.goto(1000, 1000)

        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

