#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

acak = 0
total_input = nr_letters + nr_symbols + nr_numbers
password = ""
for i in range(1, total_input + 1):
    if nr_letters > 0 and nr_symbols > 0 and nr_numbers > 0:
        acak = random.randint(1, 3)
        if acak == 1:
            acak = random.randint(0, len(letters) - 1)
            password += letters[acak]
            nr_letters -= 1
        elif acak == 2:
            acak = random.randint(0, len(numbers) - 1)
            password += numbers[acak]
            nr_numbers -= 1
        elif acak == 3:
            acak = random.randint(0, len(symbols) - 1)
            password += symbols[acak]
            nr_symbols -= 1
    elif nr_letters > 0 and nr_numbers > 0:
        acak = random.randint(1, 2)
        if acak == 1:
            acak = random.randint(0, len(letters) - 1)
            password += letters[acak]
            nr_letters -= 1
        elif acak == 2:
            acak = random.randint(0, len(numbers) - 1)
            password += numbers[acak]
            nr_numbers -= 1
    elif nr_letters > 0 and nr_symbols > 0:
        acak = random.randint(1, 2)
        if acak == 1:
            acak = random.randint(0, len(letters) - 1)
            password += letters[acak]
            nr_letters -= 1
        elif acak == 2:
            acak = random.randint(0, len(symbols) - 1)
            password += symbols[acak]
            nr_symbols -= 1
    elif nr_numbers > 0 and nr_symbols > 0:
        acak = random.randint(1, 2)
        if acak == 1:
            acak = random.randint(0, len(numbers) - 1)
            password += numbers[acak]
            nr_numbers -= 1
        elif acak == 2:
            acak = random.randint(0, len(symbols) - 1)
            password += symbols[acak]
            nr_symbols -= 1
    elif nr_letters > 0:
        acak = random.randint(0, len(letters) - 1)
        password += letters[acak]
        nr_letters -= 1
    elif nr_numbers > 0:
        acak = random.randint(0, len(numbers) - 1)
        password += numbers[acak]
        nr_numbers -= 1
    elif nr_symbols > 0:
        acak = random.randint(0, len(symbols) - 1)
        password += symbols[acak]
        nr_symbols -= 1

print(f"Your password is: {password}")