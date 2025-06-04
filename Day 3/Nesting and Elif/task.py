print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=(int(input("What is your age? ")))
    if age <=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")

# with multiple conditions, use elif:

#let's say we have three scenarios for the ticket prices:
# Under age 12 - pay $5
# between 12 and 18 - pay $7
# over 18 - pay $12

#instead of using if/else with one condition, you can add as  many elif
#conditions you want, for example:

#if condition1:
#    do A
#elif condition2:
#    do B
#else:
#     do C

if height >= 120:
    print("You can ride the rollercoaster")
    age=(int(input("What is your age? ")))
    if age <=12: # are you under 12?
        print("Please pay $5") #Yes: pay $5 or No: go to next condition.
    elif age <=18: # You are not under 12, but are you under 18?
        print("Please pay $7") # Yes: pay $7 or No: go to next condition.
    else: # You are not under 18. Pay $12.
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")