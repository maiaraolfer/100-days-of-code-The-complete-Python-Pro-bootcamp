friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
#option 1
print(random.choice(friends)) #chooses randomly from a sequence
                              #in this case the list friends

# option 2
random_index = random.randint(0,4)
print(friends[random_index]) #chooses a random index from 0 to 4
                              #and prints the friend at that index