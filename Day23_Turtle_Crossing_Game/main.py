from turtle import Screen
from car import Car
from scoreboard import Line, Scoreboard
from player import Player
from time import sleep
from random import choice

y_positions = [20, 60, 100, 140, 180, 220, -20, -60, -100, -140, -180, -220]
cars = []

screen = Screen()
screen.screensize(600, 560)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

for position in range(0, 320, 40):
    line1 = Line()
    y_position = position
    line1.draw_line(y_position)
    line2 = Line()
    y_position = - y_position
    line2.draw_line(y_position)


for i in range(1, 29):
    car = Car()
    car.initial_position(choice(y_positions))
    cars.append(car)

player = Player()

scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_on = True
screen.update()

while game_on:
    screen.update()
    sleep(0.1)
    for car in cars:
        car.move()
        if car.xcor() < -320:
            car.reset_position()
# Detect collusion with car
        if car.distance(player) < 30:
            game_on = False
    if player.ycor() > 240:
        scoreboard.point()
        player.reset_position()
        for car in cars:
            car.y_move +=2


scoreboard.game_over()




screen.exitonclick()