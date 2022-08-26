import pandas as pd
from turtle import Screen
from states import State

states = []
score = 0


screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.tracer(0)

states_data = pd.DataFrame(pd.read_csv("50_states.csv"))
states_names = states_data["state"].tolist()
states_xcor = states_data["x"].tolist()
states_ycor = states_data["y"].tolist()

for i in range(0, 50):
    new_state = State()
    new_state.create_state(states_names[i], states_xcor[i], states_ycor[
        i])
    states.append(new_state)

game_on = True

while game_on:
    user_guess = (screen.textinput(title=f"State name! {score}/50",
                                   prompt="What is your guess?")).lower()
    for state in states:
        if state.name.lower() == user_guess:
            state.found()
            score += 1
    if user_guess == "exit":
        game_on = False
    if score == 50:
        game_on = False

screen.exitonclick()
