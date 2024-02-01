import time

import pandas
import turtle
from turtle import *


def write_text(data):
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.goto(data.x.values[0], data.y.values[0])
    text.write(str(data.state.values[0]), False, "center", ("Arial", 8, "normal"))


screen = Screen()
screen.title("U.S. State Game")
screen.tracer(0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")

game_is_on = True
guesses = list[str]()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    state = turtle.textinput(f"Guess a state! {len(guesses)}/50 correct", "What's another state's name?")
    data_found = states[states.state == state]
    if not data_found.empty:
        guesses.append(data_found.state.item)
        write_text(data_found)
    elif state == "Exit":
        for item in states.state.to_list():
            if not item in guesses:
                write_text(states[states["state"] == item])
                game_is_on = False

screen.exitonclick()
