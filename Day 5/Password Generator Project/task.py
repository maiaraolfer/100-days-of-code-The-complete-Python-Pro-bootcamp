letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy level - no randomization between letter symbols and numbers
import random

password = random.choices(letters, k=nr_letters)+random.choices(symbols, k = nr_symbols)+random.choices(numbers,k=nr_numbers)
str_password = ''.join(password) #turning it into a string instead of printing a list.
print(f"Your password is {str_password}")

#hard level - randomization bettwen letter, symbols and numbers

password = random.sample(letters,k=nr_letters)+random.sample(symbols,nr_symbols)+random.sample(numbers, nr_numbers)
random.shuffle(password) #do not assign it to a variable. shuffle returns None, it just shuffles the original list
password_str = ''.join(password) # turning it into string
print(f"Your password is {password_str}") #printing the password


## using for loop - easy level
password = ""
for character in range(0,nr_letters): 
    password += random.choice(letters)

for character in range(1,nr_symbols+1):
    password += random.choice(symbols)
    
for character in range(0,nr_numbers):
    password += random.choice(numbers)

print(password)

# using loop  - hard level
password = []
for character in range(0,nr_letters): 
    password.append(random.choice(letters))

for character in range(1,nr_symbols+1):
    password.append(random.choice(symbols))
    
for character in range(0,nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
password = ''.join(password)
print(password)