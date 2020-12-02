from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser (start_text, shift_number, choice):
    new_text = ''
    for letter in start_text:       
        if letter in alphabet:
            position = alphabet.index(letter)
            if choice == 'encode':
                new_text += alphabet[position + shift_number]
            elif choice == 'decode':
                new_text += alphabet[position - shift_number]
        else:
            new_text += letter
    print(f'The {choice}d text is {new_text}')

print(logo)
start = "yes"
while start == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        shift = shift % 25

    ceaser(text, shift, direction)

    start = input('Type "yes" if you want to go again. Otherwise, type "no"\n').lower()
    
Print("Goodbye!")

    

