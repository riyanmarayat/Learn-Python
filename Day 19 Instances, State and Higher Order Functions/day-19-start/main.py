from turtle import Turtle, Screen

# Part 178 Python Higher Order Functions & Event Listeners
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
