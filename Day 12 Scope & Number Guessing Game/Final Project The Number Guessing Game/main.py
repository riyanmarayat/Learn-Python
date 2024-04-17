#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

from art import logo

def game_guess_number(player_health, the_guess_number):
    """Fungsi untuk memanggil game guess number"""
    while player_health > 0:
        player_number = int(input(f"You have {player_health} attempts remaining to guess the number.\nMake a guess: "))
        if player_number == the_guess_number:
            print(f"You got it! The answer was {player_number}")
            return player_health
        elif player_number > the_guess_number:
            print("Too high.")
            player_health -= 1
        else:
            print("Too low.")
            player_health -= 1
        if player_health == 0:
            print(f"You lose! The answer was {the_guess_number}")
            return player_health
        else:
            print("Guess again.")

def pick_from_2_choice(statement, option1, option2, statement_option1 = "", statement_option2 = ""):
    """'Statement'. Type 'option1' 'statement_option1'or 'option2''statement_option2': """
    choice = input(f"{statement}. Type '{option1}' {statement_option1}or '{option2}''{statement_option2}: ").lower()
    if choice == option1.lower() or choice == option2.lower():
        return choice
    else:
        print(f"Your input is invalid. Please input correct answer '{option1}' or '{option2}'!")
        pick_from_2_choice(statement, option1, option2, statement_option1, statement_option2)
    
player_health = None
is_playing = True
while is_playing:
    number = random.randint(1, 100)
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = pick_from_2_choice("Choose a difficulty", "easy", "hard")
    if difficulty == "easy":
        player_health = 10
    elif difficulty == "hard":
        player_health = 5
    game_guess_number(player_health, number)
    playing = pick_from_2_choice("Do you want to play again?", "y", "n", "to continue play ", " to end the game")
    if playing == "n":
        is_playing = False
    print("\033[2J\033[H", end="", flush=True) #clear console