#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

kata_terpilih = random.choice(word_list)
user_huruf = input("Masukkan huruf yang anda pilih: ")
for huruf in kata_terpilih:
  if huruf == user_huruf.lower():
    print("Benar")
  elif huruf != user_huruf.lower():
    print("Salah")