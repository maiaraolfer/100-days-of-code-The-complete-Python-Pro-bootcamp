import random
stages = [ 
          '''
        _______
     |/    |
     |    (_)
     |    \|/
     |     | 
     |    / \ 
     |
    _|___]
    '''
    =========
    '''
        _______
     |/    |
     |    (_)
     |    \|/
     |     | 
     |    /| 
     |
    _|___]
    '''
    =========
    '''
        _______
     |/    |
     |    (_)
     |    \|/
     |     
     |     
     |
    _|___]
    '''
    =========
    '''
        _______
     |/    |
     |    (_)
     |    \|
     |     
     |    
     |
    _|___]
    '''
    =========
    '''
        _______
     |/    |
     |    (_)
     |    
     |      
     |     
     |
    _|___]
    '''
    =========
    '''
        _______
     |/    |
     |    
     |    
     |      
     |     
     |
    _|___]
    ''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

