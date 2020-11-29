#variables, lists, imports and inputs
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Encrypt Function
def caesar(text, shift, direction):
  encoded_list = []
  for i in text:
    if i in alphabet:
      encoded_list.append(alphabet[alphabet.index(i)+shift])
    else:
      encoded_list.append(i)
  encoded_text = ''.join(encoded_list)
  print(f"{direction}d Text: {encoded_text}")


# Code which helps in running
print(logo)
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to exit:\n")
  if direction == 'exit':
    print("Bye!")
    break
  elif direction == 'encode' or direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number(integer):\n"))
    if direction == 'encode':
      if shift >= 25:
        caesar(text, shift%25, 'encode')
      else:
        caesar(text, shift, 'encode')
    elif direction == 'decode':
      if shift >= 25:
        caesar(text, -shift%25, 'decode')
      else:
        caesar(text, -shift, 'decode')
    else:
      print("Sorry, I don't understand.")
  else:
    print("Sorry, I don't understand.")
