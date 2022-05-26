from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput('Winning color', 'Which color you bet is going to win? ')

pos = [[-240, 150], [-240, 100], [-240, 50], [-240, 0], [-240, -50], [-240, -100]]
color = ['blue', 'red', 'green', 'purple', 'yellow', 'orange']
all_turtles = []

for turtle in range(0, 6):
    t = Turtle(shape='turtle')
    t.penup()
    t.color(color[turtle])
    t.setpos(pos[turtle])
    all_turtles.append(t)

while True:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            break
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()