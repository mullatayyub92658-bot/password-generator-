import random

letters = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@$%#&"

characters = letters + uppercase + numbers + symbols

length = int(input(" Enter password length:"))

password = ""

for i in range(length):
    password += random.choice(characters)

print("your password is:", password)