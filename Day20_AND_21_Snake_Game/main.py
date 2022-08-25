from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase()

    # Detect collusion with wall
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or \
            snake.head.ycor() < - 288:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with tail
        for part in snake.body[1:]:
            if snake.head.distance(part) < 10:
                scoreboard.reset_score()

screen.exitonclick()
