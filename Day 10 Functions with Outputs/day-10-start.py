#Part 100 Functions with Outputs
#Functions with Inputs
# def my_function(something):
#     Do this something
#     Then do this
#     Finally do this
#
# my_function(123)

#Functions with Outputs
# def my_function():
#     result = 3 * 2
#     return result
#
# output = my_function()

#Functions with Outputs
# def format_name(first_name, last_name):
#     formated_first_name = first_name.title()
#     formated_last_name = last_name.title()

#     return f"{formated_first_name} {formated_last_name}"

# formated_string = format_name("riyan", "martin")
# print(formated_string)


#Part 101 Multiple return values
# Functions with Outputs
# def format_name(first_name, last_name):
#     if first_name == "" or last_name == "":
#         return "You did'n provide valid inputs."
#     formated_first_name = first_name.title()
#     formated_last_name = last_name.title()

#     return f"{formated_first_name} {formated_last_name}"

# formated_string = format_name(input("What is your first name? "), input("What is your last name? "))
# print(formated_string)


#Part 103 Docstrings
#Already used functions with outputs.
length = len(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    retutn f"Result: {formated_f_name} {formated_l_name}"

