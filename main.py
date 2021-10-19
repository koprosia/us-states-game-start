import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

score = 0
game_is_on = True
correct_guesses = []

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What is another state name?")
    title_answer_state = answer_state.title()
    if title_answer_state == "Exit":
        break
    for state in states:
        if state == title_answer_state:
            if title_answer_state not in correct_guesses:
                new_turtle = turtle.Turtle()
                new_turtle.hideturtle()
                new_turtle.penup()
                new_turtle.goto(x=int(data[data.state == title_answer_state].x),
                                y=int(data[data.state == title_answer_state].y))
                new_turtle.write(state)
                correct_guesses.append(title_answer_state)
                score += 1

not_guessed_states = []
for state in states:
    if state not in correct_guesses:
        not_guessed_states.append(state)

not_guessed_states_data = pandas.DataFrame(not_guessed_states)
not_guessed_states_data.to_csv("snot_guessed_states_data.csv")
