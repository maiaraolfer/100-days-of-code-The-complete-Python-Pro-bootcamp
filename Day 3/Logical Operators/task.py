#logical operators

# A and B - both have to be true
# C or D - either one has to be true
# not E - reverses the condition; True becomes False and F becomes T;

#ex. a=12
# not a<0: is a less than 0? False. with not in front, it becomes True.


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <=55: # another syntax: 45 <= age >= 55
        print("Have a free ride on us!")
        bill = 0 #bill does not need to change in this case.
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
