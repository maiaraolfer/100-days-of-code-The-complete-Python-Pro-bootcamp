# Defining and Calling Python functions

#built-in functions - len(), int(), print(), range() etc

print() #name followed by
#functions work pretty much the same

print("Hello")
num_char = len("Hello")
print(num_char)

# how to make our own function?

def my_function(): # def = defining; my_function = name of the function followed by parenthesis.
    #everything beyond ':' is related to the function itself
    print("Hello") #do this
    print("Bye") #finally do this
    #instructions for the function are always indented
    
#calling the function:
my_function()

# Indentation - idented means shift to the right.
# it's like opening a folder in a computer, everything that is inside the folder is indented.

# you can use wither tabs or spaces to indent a line
# python resources suggests spaces are preferred and 4 spaces are needed for an indentation

# While loop
while something_is_true:
    #do something repeatedly

#the loop will work as long as something_is_true is TRUE. When FALSE, it will stop.

# example with Hurdles race
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump() #execute the function jump() created in reeborg's world
    number_of_hurdles -= 1 #number of hurdles minus 1;
    print(number_of_hurdles)

#when to use for or while loop?
#for loop are particularly good for iterating through a list and do something to the items of the list
#while is used when you dont care for the list and the iteration, just for the condition you set.
#while you continue running until the condition is met.. this can lead to an infinite loop.

# Reeborgs hurdles 4 - variable heights

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()
    
       
while not at_goal():
    if right_is_clear():
        jump()
    elif front_is_clear():
        move()
    else:
        turn_left()