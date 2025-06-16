# STEP 1
word_list = ["aardvark", "baboon", "camel"] #tip: animals

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
import random
chosen_word = random.choice(word_list)
print(chosen_word)  # You can uncomment this line for debugging, then comment it out for the real game

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please, choose a letter!").lower()
#print(f"{guess}") # uncomment for debugging

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

#if guess in chosen_word:
#    print("Right")
#else:
#    print("Wrong")

#OR

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")