alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def encrypt(text, shift):
  encoded_list = []
  for i in text:
    encoded_list.append(alphabet[alphabet.index(i)+shift])
  encoded_text = ''.join(encoded_list)
  print(f"Encoded text: {encoded_text}")


if direction == 'encode':
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number(integer):\n"))
  encrypt(text, shift)
else:
  print("Function coming soon.")
