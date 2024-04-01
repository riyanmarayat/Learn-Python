# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
sisa = number % 2
if sisa == 1:
  print("This is an odd number.")
elif sisa == 0:
  print("This is an even number.")
else:
  print("Anda tidak memasukkan bilangan bulat")