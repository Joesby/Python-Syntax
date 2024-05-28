#Task 1: Validating Calculations
x = 35
y = 5
z = 2
answer1 = 0
answer2 = 0

#Perform calculation without parentheses
answer1 = x / y + z
print(answer1)

#Perform calculation with parentheses
answer2 = x / (y + z)
print(answer2)

#Compare answers
if answer1 != answer2:
    print("Parentheses matters a lot.")
else:
    print("Something is wrong.")


#Task 2: Mix and Match
if (z + y) > y and (z + y) == 7:
    print("Success")
else:
    print("Try again")