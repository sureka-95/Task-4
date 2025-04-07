# Get user input
a= int(input("Enter an integer: "))

# Extract the last digit using modular operator
last_digit = a % 10

# Find the first digit using a loop
first_digit = a
while first_digit >= 10:
    first_digit //= 10  # Remove last digit until only first digit remains
    # Here floor division  by 10 is done

# Calculate the sum
sum_digits = first_digit + last_digit

# Print the result
print("First digit:", first_digit)
print("Last digit:", last_digit)
print("Sum of first and last digit:", sum_digits)