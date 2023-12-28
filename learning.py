import random
import math

num_computer = random.randint(1, 100)
print("Добро пожаловать в угадайку!")

print("Введите число от 1 до 100")


def is_valid(x):
    if x.isdigit() and 1 <= int(x) <= 100:
        return True
    else:
        return "А может быть все-таки введем целое число от 1 до 100?"





while True:
      num = input("Введите целое число от 1 до 100: ")
      is_valid(num)
      
      if int(num) < num_computer:
        print("Ваше число меньше загаданного, попробуйте еще разок")
      elif int(num) > num_computer:
        print('Ваше число больше загаданного, попробуйте еще разок')
      else:
        print("Вы угадали число!")
        break
        







