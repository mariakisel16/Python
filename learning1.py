import random
print("Welcome to the guessing game!")
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
print("You have 6 attempts to choose the word")
attempt = 6
display = []
for _ in range(len(chosen_word)):
  display += "_"
print(display)

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter 
  
  if guess not in chosen_word:
    attempt -= 1
    if attempt == 0:
      end_of_game = True
      print("You lose")
  print(display)
   
  if "_" not in display:
    end_of_game = True
    print("You win.")
