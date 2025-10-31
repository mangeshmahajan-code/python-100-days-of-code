import pandas
import turtle
import csv

#   setting the data in csv file as a list and dic
data = pandas.read_csv("india_states_coordinates.csv")
state_list = data["state"].tolist()
print(state_list)

#   The setup of the blank indian map
screen = turtle.Screen()
screen.setup(width=700, height=700)
image = "india_outline_map.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("indian state game ")
turtle.shape(image)

#   The main logic of the game
total_state = len(state_list)
state_guess_correctly =0
state_turtle = []
game_is_on = True
while game_is_on :
#   user input as pop up
    user_input = screen.textinput(title=f"{state_guess_correctly}/{total_state } Correct Guess state", prompt="What's another state name ?")
    capitalize_input  = user_input.title()

    # Checking the user input and state list if correct reflect on the map
    if capitalize_input  in state_list :
        new_state = turtle.Turtle()
        new_state.penup()
        new_state.hideturtle()
        state_data = data[data.state == capitalize_input]
        new_state.goto(state_data.x.item(),state_data.y.item())
        new_state.write(user_input, font=("Arial", 10, "bold"))
        state_turtle.append(new_state)
        state_guess_correctly += 1

    # If user press cancel
    if user_input is None :
        break

    # after all state guess by the user the game ends
    if state_guess_correctly == total_state :
        game_is_on = False


screen.exitonclick()

