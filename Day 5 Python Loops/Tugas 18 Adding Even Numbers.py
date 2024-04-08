target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

total = 0
for angka in range(1, target + 1):
    if angka % 2 == 0:
        total += angka
print(total)