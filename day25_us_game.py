import turtle
import pandas


if __name__ == "__main__":
    IMAGE = "day25_blank_states_img.gif"

    screen = turtle.Screen()
    screen.title("US States Game")
    screen.addshape(IMAGE)

    turtle.shape(IMAGE)

    data = pandas.read_csv("day25_50_states.csv")
    states = data.state.to_list()
    states_coordinates = {}

    for state_name in states:
        state_row = data[data.state == state_name]
        x_cor = int(state_row.x.iloc[0])
        y_cor = int(state_row.y.iloc[0])
        states_coordinates[state_name] = (x_cor,y_cor)

    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()

    already_guessed = []

    while len(already_guessed) < 50:
        score = len(already_guessed)
        answer_state = screen.textinput(f"{score}/50 States Correct","What's another state's name?").title()
        
        if answer_state == "Exit":
            missing_states = [state_name for state_name in states if state_name not in already_guessed]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("day25_states_to_learn.csv")
            break

        if answer_state in states and answer_state not in already_guessed:
            already_guessed.append(answer_state)
            writer.goto(states_coordinates[answer_state])
            writer.write(answer_state)
