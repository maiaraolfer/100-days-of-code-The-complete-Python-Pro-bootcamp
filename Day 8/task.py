# Functions with Inputs

# Create a function called greet()
# write 3 print statements inside the function
# call greet() function and run your code

def greet(): #def keyword + name of the function + parenthesis + colon ':'
    print("Hello.")
    print("My name is Maiara.")
    print("Nice to meet you.")
    
greet() # call the function by the name and parenthesis
#notice that every time we call the function the lines of code are the same
#it would be nice though if we could say Hello someone (using their name) instead of just Hello.
#how can we achieve this kind of functionality?

# we can add a variable inside the parenthesis if we want
# for example:

#def function(variable):
    #do this
    #then do this
    #finally do that
    
#function(123) # in this case variable = 123, and the code would run considering this.

# functions that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}.")
    print(f"How do you do {name}?")

greet_with_name("Billie") # everytime the function is executed it is modified by the input


# "Angela" or "123" is the argument
#the argument is the actual piece of data that will be passed over to the function when its being called

# variable = parameters
#the parameter is the name of that data and we use it inside the functions to refer and to do things with it.

# Positional vs Keyword arguments

# Functions with more than one inputs

def greet(name, location):
    print(f"Hello {name}.")
    print(f"How is life in {location}?")
greet("Maiara", "Mogi Guacu")

greet(name = "Ana", location = "Sao Paulo")
greet( location = "Uberlandia", name = "Natalia")

# the order of the arguments is important; the position of the data must follow the function parameters order
# if you dont use the equal sign/ keyword arguments.
# Example:
# def function(a,b,c)
      # do this
      
#function(1,2,3) >> a=1, b=2, c=3
# if you use keyword arguments (ex. name = "ana"), you would not have a problem if the order is different.

