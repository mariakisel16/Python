alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:


  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def encrypt(text, shift):
    cipher_string = ""
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift
      if new_position > 25:
        new_position = new_position - 26
      new_letter = alphabet[new_position]
      cipher_string += new_letter
    print(cipher_string)


  def decrypt(cipher_string, shift):
    word = ""
    for letter in cipher_string:
      position = alphabet.index(letter)
      new_position = position - shift
      if new_position < 0:
        new_position = 26 + new_position 
      new_letter = alphabet[new_position]
      word += new_letter
    print(word)

  if direction == "encode":
    encrypt(text, shift)
  elif direction == "decode":
    decrypt(text, shift)
  else:
    print("Write correct direction")

  result = input('Type "yes" if you want to continue. Otherwise, type "no" \n' ).lower()
  if result == "no":
    should_continue = False
    print("Goodbuy")