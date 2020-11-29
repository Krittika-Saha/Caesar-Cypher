#variables, lists and inputs
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Encrypt Function
def encrypt(text, shift):
  encoded_list = []
  for i in text:
    encoded_list.append(alphabet[alphabet.index(i)+shift])
  encoded_text = ''.join(encoded_list)
  print(f"Result: {encoded_text}")


# Code which helps in running
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to exit:\n")
  if direction == 'exit':
    print("Bye!")
    break
  elif direction == 'encode' or direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number(integer):\n"))
    if direction == 'encode':
      encrypt(text, shift)
    elif direction == 'decode':
      encrypt(text, -shift)
    else:
      print("Sorry, I don't understand.")
  else:
    print("Sorry, I don't understand.")
