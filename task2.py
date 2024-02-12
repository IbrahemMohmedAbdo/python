# Initialize sum to zero
sum_of_numbers = 0

# Take 10 integers from the user
for i in range(10):
    num = int(input("Enter an integer: "))
    sum_of_numbers += num

# Calculate average
average = sum_of_numbers / 10

# Print the average
print("Average:", average)

# Accept number from the user
n = int(input("Enter a number: "))

# Calculate the sum
sum_of_numbers = sum(range(1, n + 1))

# Print the sum
print("Sum of numbers from 1 to", n, "is:", sum_of_numbers)

# Given list
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# Iterate the list
for num in list1:
    # Check if the number is divisible by 5
    if num % 5 == 0:
        print(num, "is divisible by 5")
    
    # Check if the number is greater than 150
    if num > 150:
        break

# Display Fibonacci series up to 10 terms
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
