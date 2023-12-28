print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input('Choose the direction "left" or "right"? \n').lower()
if choice_1 == "left":
    print("Great! You chose the right direction!")
    choice_2 = input(
        'Let\'s continue. Now you are in the front of the rive. What do you choose "swim" or "wait" for a boat? \n'
    ).lower()
    if choice_2 == "wait":
        print("You chose the right choice! You are safe.")
        choice_3 = input(
            'You are in front of three doors. Which door do you choose red, yellow, or green? \n'
        ).lower()
        if choice_3 == "red":
            print("Sorry! Wrong door! Game over!")
        elif choice_3 == "yellow":
            print("You are a winner! You found the treasure!")
        elif choice_3 == "green":
            print("Sorry! Wrong door! Game over!")
        else:
            print("Sorry! Wrong direction! Game over!")

    else:
        print("You made a wrong decision. Game over!")

else:
    print("Oh no! You chose the wrong direction... Game over")

  