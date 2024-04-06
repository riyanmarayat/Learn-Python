rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_input = input("Selamat datang dalam game kertas gunting batu. Anda diharuskan untuk memilih salah satu dari 3 pilihan berikut: kertas, gunting, batu.\nPilihan anda adalah: ")

komputer_nomor_acak = random.randint(0,2)
tipe = ["kertas", "gunting", "batu"]
pilihan = [player_input.lower(), tipe[komputer_nomor_acak]]

if pilihan[0] == "kertas" and pilihan[1] == "kertas":
  print(f"Kamu memilih\n\n\n{paper}\n\n\nKomputer memilih\n\n\n{paper}\n\n\nHasilnya seri!")
elif pilihan[0] == "gunting" and pilihan[1] == "gunting":
  print(f"Kamu memilih\n\n\n{scissors}\n\n\nKomputer memilih\n\n\n{scissors}\n\n\nHasilnya seri!")
elif pilihan[0] == "batu" and pilihan[1] == "batu":
  print(f"Kamu memilih\n\n\n{rock}\n\n\nKomputer memilih\n\n\n{rock}\n\n\nHasilnya seri!")
elif (pilihan[0] == "kertas" and pilihan[1] == "gunting") or (pilihan[0] == "gunting" and pilihan[1] == "kertas"):
  if pilihan[0] == "gunting":
    print(f"Kamu memilih\n\n\n{scissors}\n\n\nKomputer memilih\n\n\n{paper}\n\n\nKamu menang!")
  else:
    print(f"Kamu memilih\n\n\n{paper}\n\n\nKomputer memilih\n\n\n{scissors}\n\n\nKomputer menang!")
elif (pilihan[0] == "kertas" and pilihan[1] == "batu") or (pilihan[0] == "batu" and pilihan[1] == "kertas"):
  if pilihan[0] == "kertas":
    print(f"Kamu memilih\n\n\n{paper}\n\n\nKomputer memilih\n\n\n{rock}\n\n\nKamu menang!")
  else:
    print(f"Kamu memilih\n\n\n{rock}\n\n\nKomputer memilih\n\n\n{paper}\n\n\nKomputer menang!")
elif (pilihan[0] == "gunting" and pilihan[1] == "batu") or (pilihan[0] == "batu" and pilihan[1] == "gunting"):
  if pilihan[0] == "batu":
    print(f"Kamu memilih\n\n\n{rock}\n\n\nKomputer memilih\n\n\n{scissors}\n\n\nKamu menang!")
  else:
    print(f"Kamu memilih\n\n\n{scissors}\n\n\nKomputer memilih\n\n\n{rock}\n\n\nKomputer menang!")
else:
  print("ERORR: Mohon masukkan input yang benar! (kertas, gunting, batu)")