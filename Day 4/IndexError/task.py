states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
#print(states_of_america[49])  # This will print "Hawaii", the last state in the list
#print(states_of_america[50])  # running the line would raise an IndexError because the list has only 50 elements (0-49)

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
               "Pears", "Tomatoes", "Celery", "Potatoes"]
#note that the list has fruits and vegetables. we can separate them into two lists using nested list

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
#print(dirty_dozen)  # Note that there is two brackets, one for the list of fruits and one for the list of vegetables
print(dirty_dozen[1][1]) # This will print "Kale", the second vegetable in the second list, in this case the vegetables
print(dirty_dozen[0][2]) # This will print "Apples", the third fruit in the list of fruits
#the first bracket is for the list of fruits and vegetables, the second bracket is for the item of the list
