import turtle
from turtle import Turtle, Screen
import random

# PART 166 Understanding Turtle Graphics and How to use the Documentation
# timmy_the_turle = Turtle()
# timmy_the_turle.shape("turtle")
# timmy_the_turle.color("red")
# timmy_the_turle.forward(100)
# timmy_the_turle.right(90)
#
#
# screen = Screen()
# screen.exitonclick()

# Part 167 Turtle Challenge 1 - Draw a Square

# kura = Turtle()
# for i in range(4):
#     kura.forward(100)
#     kura.right(90)

# Part 168 Importing Modules, Installing Packages, and Working with Aliases
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()
#
# import heroes
# print(heroes.gen())

# Part 169 Turtle Challenge 2 - Draw a Dashed Line
# kura = Turtle()
# for i in range(50):
#     kura.forward(2)
#     kura.penup()
#     kura.forward(2)
#     kura.pendown()

# Part 170 Turtle Challenge 3 - Drawing Different Shapes
# kura = Turtle()
# color = ["AliceBlue", "bisque", "black", "blue", "brown", "chocolate", "cyan"]
# sisi = 3
# for i in range (7):
#     sisi += i
#     kura.color(color[i])
#     sudut = 360 / (sisi)
#     for j in range(sisi):
#         kura.forward(50)
#         kura.right(sudut)
# Screen().exitonclick()

# Part 171 Turtle Challenge 4 - Generate a Random Walk
# kura = Turtle()
# color = ["black", "blue", "brown", "cyan", "gold", "gray", "green", "magenta", "maroon", "navy", "orange", "pink",
#          "purple", "red", "snow", "violet", "yellow"]
# arah = [0, 90, 180, 270]
# len_arah = len(arah)
# len_color = len(color)
# for count in range(300):
#     kura.speed(random.randint(1,10))
#     kura.color(color[random.randint(0, len_color-1)])
#     kura.pensize(random.randint(1, 10))
#     kura.setheading(arah[random.randint(0, len_arah-1)])
#     kura.forward(30)
# Screen().exitonclick()

# Part 172 Python Tuples and How to Generate Random RGB Colours
# kura = Turtle()
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# arah = [0, 90, 180, 270]
# len_arah = len(arah)
# for count in range(300):
#     kura.speed(random.randint(1, 10))
#     kura.color((random_color()))
#     kura.pensize(random.randint(1, 10))
#     kura.setheading(arah[random.randint(0, len_arah - 1)])
#     kura.forward(30)
# Screen().exitonclick()

# Part 173 Turtle Challenge 5 - Draw a Spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
kura = Turtle()
turtle.colormode(255)
direction = 0
kura.speed("fastest")
perulangan = 46
for i in range(perulangan):
    kura.color((random_color()))
    kura.setheading(direction)
    kura.circle(100)
    direction += 360 / perulangan
Screen().exitonclick()
