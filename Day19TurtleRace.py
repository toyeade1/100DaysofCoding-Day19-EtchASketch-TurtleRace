import random
from turtle import Turtle, Screen
from random import choice, randint
screen = Screen()
screen.setup(width = 500, height= 400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            race_is_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print('Congratulations!! You won.')
            else:
                print(f'Sorry, you lost. {winning_color} was the winner')
        turtles.forward(random.randint(0, 10))



screen.exitonclick()
