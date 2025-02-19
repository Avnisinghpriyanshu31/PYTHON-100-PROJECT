import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1,2,3,4,5,6,7,8,9]
symbols = ['~', '!', '@', '#', '$', '%', '^', '*', '_', '-', '+', '/', '\\']

print("welcome to pyPassword generator!")
nr_letters = int(input("how many letters do you want in your password?\n"))
nr_numbers = int(input("how many number would you like?\n"))
nr_symbols= int(input("how many symblos would you like?\n "))
password = []
for letter in range(0, nr_letters):
    password.append(str(random.choice(letters)))
for number in range(0, nr_numbers):
    password.append(str(random.choice(numbers)))
for symbol in range(0, nr_symbols):
    password.append(str(random.choice(symbols)))

print(password)
random.shuffle(password)
print(password)

new_password = " "
for letter in password:
    new_password += letter

print(f"your password is: {new_password}")


           