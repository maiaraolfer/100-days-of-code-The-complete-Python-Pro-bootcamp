#a list is a data structure, a way to organize data in python
#fruit = ["cherry","apple"] #between brackets and items separated by comma

#state1 = "Delaware"
#state2 = "Pennsylvania"

states_of_america = ["Delaware", "Pennsylvania"]
# the order in which they are stored might be important.
# you can use a list to store pieces of data

print(states_of_america[0]) #access the first item of the list
# the first item is in position 0

print(states_of_america[-1]) #access the first item from backwards
#meaning, the last item.

#if you want to change an item:
states_of_america[-1] = "Pensilvania"
print(states_of_america) #new list


#you can add a new name at the end of a list
states_of_america.append("Maryland")
print(states_of_america)

#see documentation for other functions.