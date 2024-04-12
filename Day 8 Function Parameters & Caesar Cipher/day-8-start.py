# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#    print("Selamat Datang")
#    print("Silahkan Masuk")
#    print("Terima Kasih")

# greet()


#Part 82 Functions with Inputs
#Functions
# def my_function():
#   Do this
#   Then do this
#   Finally do this
# my_function()

#Functions with Inputs
# def my_function(something):
#    Do this something
#    Then do this
#    Finally do this
# my_function(123)

#Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
# greet_with_name("Budi")


#Part 83 Positional vs. Keyword Arguments
#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Riyan", "Indramayu")

#Functions with keyword arguments
greet_with(name="Riyan", location="Indramayu")