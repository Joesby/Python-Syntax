#Task 1: Value Swapping
x = 3
y = 5

#Swap values
tempValue = y
y = x
x = tempValue

#Compare variables to check that they have been swapped
if y != x and y != tempValue:
    print("X is now ", x)
    print("Y is now ", y)
    print("The values have been swapped.")