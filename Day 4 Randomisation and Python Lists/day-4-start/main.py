#Part 42
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
# print(my_module.pi)

#0.000000 - 0.9999999...
random_float = random.random() * 5
print(random_float)

# random_float * 5
# 0.0000 - 4.99999999

love_score = random.randint(1, 100)
print(f"Youre love score is {love_score}")