from turtle import Screen
from scoreboard import Scoreboard, Player, Line
from paddle import Paddle
from pongball import Ball
import time


screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.listen()
screen.tracer(0)

line = Line()

paddle_1 = Paddle(-330)
paddle_2 = Paddle(320)

ball = Ball()

player1 = Player("Player 1", -300)
player2 = Player("Player 2", 300)

scoreboard = Scoreboard()

screen.onkey(paddle_1.move_up, "w")
screen.onkey(paddle_1.move_down, "s")
screen.onkey(paddle_2.move_up, "Up")
screen.onkey(paddle_2.move_down, "Down")

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # Detect collusion with wall
    if ball.ycor() > 240 or ball.ycor() < - 280:
        ball.bounce_y()

    # Detect collusion with paddle_1
    if paddle_1.distance(ball) < 20 or paddle_2.distance(ball) < 20:
        ball.bounce_x()
        ball.bounce_y()

    # Detect Score PLayer 1
    if ball.xcor() > 340:
        scoreboard.l_point()
        ball.reset_position()

    # Detect Score PLayer 2
    elif ball.xcor() < -340:
        scoreboard.r_point()
        ball.reset_position()

    if scoreboard.r_score == 5 or scoreboard.l_score == 5:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
