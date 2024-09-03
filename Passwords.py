import random

def generate_password(length, chars):
    password = random.choices(chars, k=length)
    random.shuffle(password)
    return ''.join(password)

num_passwords = int(input("How many passwords would you like to generate? "))
length = int(input("Enter the length of each password: "))
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

chars = ''
if use_lower:
    chars += 'abcdefghijklmnopqrstuvwxyz'
if use_upper:
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if use_digits:
    chars += '0123456789'
if use_symbols:
    chars += '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
c
if not chars:
    print("You must select at least one character set!")
else:
    for _ in range(num_passwords):
        print(generate_password(length, chars))