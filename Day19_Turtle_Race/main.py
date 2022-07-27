import turtle as t
from random import randint

is_race_on = False
y_positions = [160, 80, 0, -80, -160]
colors = ["blue", "red", "green", "yellow", "purple"]
screen = t.Screen()
screen.setup(width=500, height=400)
all_turtles = []
for turtle_index in range(0, 5):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.setposition(-225, y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which Teenage Ninja Turtle will win? "
                                                          "Type the color: ")
if user_bet:
    is_race_on = True

while is_race_on :
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner")
            else:
                print(f"You've lost! The {winning_color} is the winner")
        turtle.forward(randint(0,10))




screen.exitonclick()
