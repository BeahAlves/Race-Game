import turtle
from turtle import Turtle, Screen
import random

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()

screen = Screen()
screen.setup(500, 400)
winner = screen.textinput("Winner", "Which color you choose? (Blue, red, green, yellow, orange or purple). ")


# Colors
t1.color('blue'), t1.shape('turtle')
t2.color('red'), t2.shape('turtle')
t3.color('green'), t3.shape('turtle')
t4.color('yellow'), t4.shape('turtle')
t5.color('orange'), t5.shape('turtle')
t6.color('purple'), t6.shape('turtle')

# Position
t1.penup(), t2.penup(), t3.penup(), t4.penup(), t5.penup(), t6.penup()
t1.setpos(-240, 150)
t2.setpos(-240, 100)
t3.setpos(-240, 50)
t4.setpos(-240, 0)
t5.setpos(-240, -50)
t6.setpos(-240, -100)

# Destination
speed = [3, 5, 7, 10]
race_on = True
t1amount = t2amount = t3amount = t4amount = t5amount = t6amount = 0
t1list = []
t2list = []
t3list = []
t4list = []
t5list = []
t6list = []


while True:
    t1amount = random.choice(speed)
    t2amount = random.choice(speed)
    t3amount = random.choice(speed)
    t4amount = random.choice(speed)
    t5amount = random.choice(speed)
    t6amount = random.choice(speed)

    t1.fd(t1amount)
    t2.fd(t2amount)
    t3.fd(t3amount)
    t4.fd(t4amount)
    t5.fd(t5amount)
    t6.fd(t6amount)

    # SAVING THE RANDOM RESULTS
    t1list.append(t1amount)
    t2list.append(t2amount)
    t3list.append(t3amount)
    t4list.append(t4amount)
    t5list.append(t5amount)
    t6list.append(t6amount)

    t1_sum = sum(t1list)
    t2_sum = sum(t2list)
    t3_sum = sum(t3list)
    t4_sum = sum(t4list)
    t5_sum = sum(t5list)
    t6_sum = sum(t6list)

    #Winner

    if t1_sum >= 470:
        print("Blue wins")
        if winner == 'blue':
            print('You won! ')
        else:
            print("You lost")
        break

    elif t2_sum >= 470:
        print("Red wins")
        if winner == 'red':
            print('Congratulations! ')
        else:
            print("You lost")
        break

    elif t3_sum >= 470:
        print("Green wins")
        if winner == 'green':
            print('Congratulations! ')
        else:
            print("You lost")
        break

    elif t4_sum >= 470:
        print("Yellow wins")
        if winner == 'yellow':
            print('Congratulations! ')
        else:
            print("You lost")
        break

    elif t5_sum >= 470:
        print("Orange wins")
        if winner == 'orange':
            print('Congratulations! ')
        else:
            print("You lost")
        break

    elif t6_sum >= 470:
        print("Purple wins")
        if winner == 'purple':
            print('Congratulations! ')
        else:
            print("You lost")
        break

screen.exitonclick()
