# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_siswa = 0
total_tinggi = 0
for student_height in student_heights:
    total_tinggi += student_height
    total_siswa += 1
average_student_heights = total_tinggi / total_siswa
print(f"total height = {total_tinggi}\nnumber of students = {total_siswa}\naverage height ={average_student_heights: .0f}")