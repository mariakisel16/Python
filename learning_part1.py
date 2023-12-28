from functools import reduce


list1 = [-1, 3, 7, 99, 0]
print(reduce(max, list1))

list1 = [3, 2, 8, 5, 10, 6]
max_number = max(list1)
print("Наибольшее число:", max_number)
