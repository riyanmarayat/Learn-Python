line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
position_row = position[1]
position_column = position[0]

if position_row == "1":
    if position_column.lower() == "a":
        map[0][0] = "X"
    elif position_column.lower() == "b":
        map[0][1] = "X"
    elif position_column.lower() == "c":
        map[0][2] = "X"
elif position_row == "2":
    if position_column.lower() == "a":
        map[1][0] = "X"
    elif position_column.lower() == "b":
        map[1][1] = "X"
    elif position_column.lower() == "c":
        map[1][2] = "X"
elif position_row == "3":
    if position_column.lower() == "a":
        map[2][0] = "X"
    elif position_column.lower() == "b":
        map[2][1] = "X"
    elif position_column.lower() == "c":
        map[2][2] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")