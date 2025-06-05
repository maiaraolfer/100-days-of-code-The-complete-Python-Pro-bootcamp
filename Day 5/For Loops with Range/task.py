# Range function

#for number in range(a,b):
#    print(number)
# range function doesnt do anything by itself

for number in range (1,10):
    print(number) #notice that range does not include the upper bound (no. 10 is out!)
    #if you want to include number 10, you need to use "range(1,11)"

for number in range(1,11):
    print(number)
    
#there is another argument to the function that estipulates a step:

for number in range (1,11,3): #range from 1 to 11, step by 3.
    print(number)
    
#Task: how can we add up all numbers from 1 to 100?
sum = 0
for number in range (1,101): #all numbers 1 to 100. No step because we want all numbers.
    sum += number

print(sum)