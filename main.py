import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.setup(width=800, height=400)
screen.title("Turtle Race ")

# Colors for turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Get user's guess
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (Enter a color): ")

# Create turtles
all_turtles = []
for i in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-370, y=y_positions[i])
    all_turtles.append(new_turtle)

# Start race
race_on = True if user_bet else False

while race_on:
    for turtle_ in all_turtles:
        if turtle_.xcor() > 370:
            race_on = False
            winning_color = turtle_.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle won.")
        turtle_.forward(random.randint(0, 10))

screen.exitonclick()
