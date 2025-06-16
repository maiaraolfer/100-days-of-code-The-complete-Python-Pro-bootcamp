# STEP 2

# TODO 1
placeholder = "" #empty string
for position in range(len(chosen_word)):
    placeholder += '_'

print(placeholder)

# TODO 2
display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
        
print(display)
