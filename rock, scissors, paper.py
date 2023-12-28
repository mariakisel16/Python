import random

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
game_images = [rock, scissors, paper]
choice_list = ["Rock", "Scissors", "Paper"]

print("Welcome to the game Rock, Scissors, Paper")
user_choice = int(input(
    "Make your choice: type 0 for Rock, type 1 for Scissors, type 2 for Paper\n"))
print(f"You choose: {choice_list[user_choice]}")
print(game_images[user_choice])
# choice_made = choice_list[choice]
computer_choice = random.randint(0, 2)
print(f"Computer choose: {choice_list[computer_choice]}")
print(game_images[computer_choice])
if user_choice == 0 and computer_choice == 1:
    print("You win")
elif user_choice == 0 and computer_choice == 2:
    print("You lose")
elif user_choice == 1 and computer_choice == 0:
    print("You lose")
elif user_choice == 1 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("You win")
elif user_choice == 2 and computer_choice == 1:
    print("You lose")

else:
    print("Draw")
