student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_exame_score = sum(student_scores)
print(total_exame_score)

sum = 0  #using a loop to calculate the sum
for score in student_scores:
    sum += score
print(sum)

print(max(student_scores)) #gets the highest score

#replicating the max function using a loop
max = 0
for score in student_scores:
    if score > max: #se o score da iteracao for maior que max, 
        max = score #o objeto max recebe o score.
print(max)  #prints the highest score

