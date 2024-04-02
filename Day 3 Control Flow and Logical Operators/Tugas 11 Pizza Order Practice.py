print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

#Ubah input nama menjadi lower case semua
name1_lower = name1.lower()
name2_lower = name2.lower()
name_gabungan = name1_lower + name2_lower
true_count = 0
love_count = 0

#Cek nama 1
true_count += int(name_gabungan.count("t"))
true_count += int(name_gabungan.count("r"))
true_count += int(name_gabungan.count("u"))
true_count += int(name_gabungan.count("e"))

love_count += int(name_gabungan.count("l"))
love_count += int(name_gabungan.count("o"))
love_count += int(name_gabungan.count("v"))
love_count += int(name_gabungan.count("e"))

love_score = str(true_count) + str(love_count)
love_score_int = int(love_score)

if love_score_int < 10 or love_score_int > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score_int >= 40 and love_score_int <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")