# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Looping through the list and printing each element
print("Printing elements of the list:")
for number in numbers:
    print(number)

# Summing up the elements of the list using a loop
sum_result = 0
for number in numbers:
    sum_result += number
print("\nSum of elements in the list:", sum_result)

# Using a loop to create a new list with squared elements
squared_numbers = []
for number in numbers:
    squared_numbers.append(number ** 4)
print("\nSquared elements of the list:", squared_numbers)
