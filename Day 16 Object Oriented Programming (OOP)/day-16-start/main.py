"""PART 148 Constructing Objects and Accessing their Attributes and Methods"""
# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
#
# timmy = Turtle()  # object.Class
# print(timmy)
# timmy.shape("turtle")  # object.method
# timmy.color("LavenderBlush3")  # object.method
# timmy.forward(100)  # object.method
#
# my_screen = Screen()
# print(my_screen.canvheight)  # object.attribute
# my_screen.exitonclick()  # object.method


"""PART 149 How to Add Python Packages and use PyPi"""
# import prettytable


"""PART 150 Practice Modifying Object Attributes and Calling Methods"""
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
