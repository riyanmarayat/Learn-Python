fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs wihtout crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")
#
# make_pie(4)

# Solution:
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)