
from math import ceil
# Input a Python list of student heights
print("Input student's heights")
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum_list = 0
for i in range(len(student_heights)):
  sum_list += student_heights[i]
average_height = sum_list/len(student_heights)
print(student_heights)
print(ceil(average_height))