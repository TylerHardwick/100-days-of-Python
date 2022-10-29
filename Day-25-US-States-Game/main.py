import turtle
import pandas


screen = turtle.Screen()
screen.title("Tyler's Guess the State Game")
image = "blank_states_img.gif"
screen.setup(725, 491)
screen.addshape(image)
turtle.shape(image)
guessed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

input_title = "Guess the State"
prompt_input = "Enter a state name."


def print_state(state, coords):
    print_turtle = turtle.Turtle()
    print_turtle.penup()
    print_turtle.hideturtle()
    print_turtle.goto(coords)
    print_turtle.write(arg=f"{state}", font=("Ariel", 8, "normal"), align="center")


while len(guessed_states) < 50:
    answer_state = screen.textinput (title=input_title, prompt=prompt_input).title()
    # Checks if State is in CSV and updates score.
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in guessed_states:
        prompt_input = f"You have already guessed {answer_state}, try again."
    elif answer_state in all_states:
            prompt_input = "Enter a state name."
            current_state = data[data.state == answer_state]
            guessed_states.append(answer_state)
            print_state(answer_state, (int(current_state.x), int(current_state.y)))
            input_title = f"{len(guessed_states)}/50 States Correct"
    else:
        prompt_input = "Enter a state name."

turtle.mainloop()