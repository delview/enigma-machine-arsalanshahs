# Enigma Machine with Atbash Cipher

# Import the time module
import time


# Create a dictionary
sipher = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"}
sipher2 = {"z": "a", "y": "b", "x": "c", "w": "d", "v": "e", "u": "f", "t": "g", "s": "h", "r": "i", "q": "j", "p": "k", "o": "l", "n": "m", "m": "n", "l": "o", "k": "p", "j": "q", "i": "r", "h": "s", "g": "t", "f": "u", "e": "v", "d": "w", "c": "x", "b": "y", "a": "z"}

# Create a Function that encrypts the message
def encrypt(messages: list):
    enter = input("Enter a message: ").strip().lower()
    for letter in enter:
        if letter in sipher:
            messages.append(sipher[letter])
    return messages

# Create a Function that decrypts the message
def decrypt(messages: list, message: str):
    enter = input("Enter a message: ").strip().lower()
    for letter in enter:
        if letter in sipher2:
            message += sipher2[letter]
    messages.append(message)
    return messages

messages = []

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
print("Please choose one of the options below:")
time.sleep(0.5)
options = int(input("1. Encrypt a message 2. Decrypt a message 3. Quit: ")).strip().lower()
time.sleep(0.5)
if options == 1:
    encrypt(messages)
    print(messages)
elif options == 2:
    pass
elif options == 3:   
    print("Goodbye!")
    time.sleep(0.5)

# If they want to encrypt, ask for a message


# If they want to decrypt, ask for a message 


# If they want to quit. say goodbye