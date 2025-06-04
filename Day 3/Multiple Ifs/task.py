print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child's tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth's tickets are $7.")
        bill = 7
    else:
        print("Adult's tickets are $12.")
        bill = 12
    wants_photo = input("Do you want you photo taken? Type y for Yes and n for No")
    if wants_photo == "y":
        # add 3$ to the bill.
        bill = bill + 3 # or bill += 3
    #else is not needed because there is no action if customer does not want a photo
    print (f"your bill is ${bill}")
    #remember: f" denotes a f-string and the curly braces have their values inserted into the string
else:
    print("Sorry you have to grow taller before you can ride.")
