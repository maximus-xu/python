import random

length = int(input("Password length: "))
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890'
password = ''
for i in range(length):
    password += random.choice(characters)

print(password)