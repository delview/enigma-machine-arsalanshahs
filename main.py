# Enigma Machine with Atbash Cipher

# Import the time module for the sleep function to make the code look more interactive
import time


# Create a dictionary
cipher = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a", "1": "0", "2": "9", "3": "8", "4": "7", "5": "6", "6": "5", "7": "4", "8": "3", "9": "2", "0": "1", " ": " ", ".": ".", ",": ",", "!": "!", "?": "?", "'": "'", '"': '"', ":": ":", ";": ";", "(": ")", ")": "(", "[": "]", "]": "[", "{": "}", "}": "{", "<": ">", ">": "<", "/": "\\", "\\": "/", "|": "|", "@": "@", "#": "#", "$": "$", "%": "%", "^": "^", "&": "&", "*": "*", "-": "-", "_": "_", "+": "+", "=": "=", "~": "~", "`": "`"}

# Create a Function that encrypts/decrypts message
def encrypt(message):
    """This function encrypts the message using the Atbash Cipher, it takes in the list of the messages, swaps each letter, then returns it."""
    encrypted_message = ""
    for letter in message:
        if letter in cipher:
            encrypted_message += cipher[letter]
    return encrypted_message

    
    
# Greet user and explain what an enigma machine is

print("Welcome to the Enigma Machine!")
time.sleep(0.5)
print("The Enigma Machine is a device used to encrypt and decrypt messages during World War II.")
time.sleep(0.5)
print("This program uses the Atbash Cipher.")
time.sleep(0.5)
print("The Atbash Cipher is a substitution cipher where the letters of the alphabet are reversed.")
time.sleep(0.5)
print("For example, the letter 'a' would be 'z', the letter 'b' would be 'y', and so on.")
time.sleep(0.5)
print("Let's get started!") 
time.sleep(0.5)


# Ask user if they want to encrypt, decrypt, or quit
time.sleep(0.5)
print("Please choose one of the options below:")
time.sleep(0.5)

while True:
# Give the user options to encrypt, decrypt, or quit
    options = input("(1) Encrypt a message (2) Decrypt a message (3) Quit: ").strip()
    time.sleep(0.5)
    # If they want to encrypt, ask for a message
    if options == "1":
        message = input("Enter a message: ").strip().lower()
        print(encrypt(message))
     # If they want to decrypt, ask for a message 
    elif options == "2":
        message = input("Enter a message: ").strip().lower()
        print(encrypt(message))
    # If they want to quit. say goodbye
    elif options == "3":   
        print("Goodbye!")
        break
    # If they enter an invalid input, ask them to enter 1, 2, or 3
    else:
        print("Invalid input, please enter 1, 2, or 3.")
