#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
tagihan = input("What was the total bill? $")
while True:
  tip = input("How much tip would you like to give? 10, 12, or 15? ")
  if(tip == "10" or tip == "12" or tip == "15"):
    break
  else:
    continue
orang = input("How many people to split the bill? ")

tagihan_float = float(tagihan)
tip_int = int(tip)
orang_int = int(orang)
total_tagihan_perorang =  (tagihan_float + tip_int) / orang_int
print(f"Each person should pay: ${total_tagihan_perorang:.2f}")