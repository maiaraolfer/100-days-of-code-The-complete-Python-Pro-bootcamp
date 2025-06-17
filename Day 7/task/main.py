import random

stages = [ '''
        _______
     |/    |
     |    (_)
     |    \|/
     |     | 
     |    / \ 
     |
    _|_________
    '''
    ,
    '''
        _______
     |/    |
     |    (_)
     |    \|/
     |     | 
     |    / 
     |
    _|_________
    '''
    ,
    '''
        _______
     |/    |
     |    (_)
     |    \|/
     |     |
     |     
     |
    _|_________
    '''
    ,
    '''
        _______
     |/    |
     |    (_)
     |    \|/
     |     
     |    
     |
    _|_________
    '''
   ,
    '''
        _______
     |/    |
     |    (_)
     |    \|
     |      
     |     
     |
    _|_________
    '''
    ,
    '''
        _______
     |/    |
     |    (_)
     |    
     |      
     |     
     |
    _|_________
    '''
    ,
    '''
        _______
     |/    |
     |    
     |    
     |      
     |     
     |
    _|_________
    '''
    ]
word_list = ["aardvark", "baboon", "camel"] #tip: animals

chosen_word = random.choice(word_list)
print(chosen_word)  # You can uncomment this line for debugging, then comment it out for the real game

placeholder = "" #empty string
for position in range(len(chosen_word)):
    placeholder += '_'

print(placeholder)
lives = 6 # chances for user to figure out the word
game_over = False #this will stop the while loop when it become True
correct_letters = [] #empty list that stores the correct letters guessed by user

while not game_over: #while game_over is False, keep asking the user for a letter
    
    guess = input("Guess a letter:").lower() #user will guess a letter
    display = "" # string empty at first iteration
    
    for letter in chosen_word:
        if letter == guess: #if letter guessed is in the word
            display += letter # add this letter to the display
            correct_letters.append(guess) #add this letter to the correct letter list
        elif letter in correct_letters: #if the guessed letter is in the correct letter list
            display += letter #write it in display
        else: # if the letter is not in the word and is not in the corrected list, write underscore indicating a blank space
            display += "_"
            print(f"You guessed letter '{guess}', that is not in the word. You lost a life.")
     
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You lost. The word was '{chosen_word}' ")
    
    print(stages[lives]) 
              
    if "_" not in display: #condition to turn game_over into True and stop the while loop.
        game_over = True
        print("You won!")
        