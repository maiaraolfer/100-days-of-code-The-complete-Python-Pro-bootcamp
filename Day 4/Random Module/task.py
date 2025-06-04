import random
#random_integer = random.randint(1,10)
#print(random_integer)

#random_number_0_to_1 = random.random()*10
#print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

# solution Heads or Tails

random_number = random.randint(1,100)
print(random_number)
if random_number % 2 == 0: #if random number is even = heads
    print("Heads")
else: print("Tails")

# OR

random_number2 = random.randint(0,1)
print(random_number2)
if random_number2 == 0:
    print("Heads")
else: print("Tails")