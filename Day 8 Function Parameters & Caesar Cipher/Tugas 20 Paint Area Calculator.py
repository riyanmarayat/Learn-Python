# Write your code below this line 👇
def paint_calc(height, width, cover):

  number_of_cans = int(height * width / cover) + (((height*width) % cover) > 0)
  print(f"You\'ll need {number_of_cans} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
