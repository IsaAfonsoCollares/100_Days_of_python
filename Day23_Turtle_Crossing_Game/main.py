from turtle import Screen
from car import Car
from scoreboard import Line, Scoreboard
from player import Player
from time import sleep

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


player = Player()

scoreboard = Scoreboard()

car = Car()

screen.onkey(player.move, "Up")

game_on = True
screen.update()

while game_on:
    screen.update()
    sleep(0.1)
    car.move()
    if player.ycor() > 240:
        scoreboard.point()
        player.reset_position()





screen.exitonclick()