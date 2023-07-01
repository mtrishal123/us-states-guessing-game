import turtle
import pandas

screen = turtle.Screen()

image_name = "blank_states_img.gif"
screen.addshape(image_name)
turtle.shape(image_name)

data = pandas.read_csv("50_states.csv")
all_state_data = data.state.to_list()
correct_answers = []
while len(correct_answers) < len(all_state_data):
    answer_state = screen.textinput(title=f"{len(correct_answers)} / 50 states correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_state_data:
        if answer_state not in correct_answers:
            correct_answers.append(answer_state)
            all_state_data.remove(answer_state)
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.ht()
            state_data = data[data.state == answer_state]
            new_turtle.goto(int(state_data.x), int(state_data.y))
            new_turtle.write(arg=state_data.state.item(), align="center")
        else:
            pass

if len(all_state_data) != 0:
    for item in all_state_data:
        new_turtle = turtle.Turtle()
        new_turtle.ht()
        new_turtle.penup()
        state_data = data[data.state == item]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(arg=state_data.state.item(), align="center")
#
# screen.exitonclick()
