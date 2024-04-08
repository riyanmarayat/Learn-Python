# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
nilai_tertinggi = 0
for nilai in student_scores:
    if nilai > nilai_tertinggi:
        nilai_tertinggi = nilai
print(f"The highest score in the class is: {nilai_tertinggi}")