# Given list
numbers = [10, 501, 22, 37, 100, 99, 87, 351]

# Empty list to store prime numbers
prime_numbers = []

# Loop through each number in the list
for num in numbers:
    if num > 1:  # Prime numbers start from 2
        is_prime = True  
        # Assume the number is prime
        for i in range(2, int(num ** 0.5) + 1):  # Check divisibility
            if num % i == 0:
                is_prime = False  # If divisible, it's not prime
                break
        if is_prime:  # If still prime, add to the list
            prime_numbers.append(num)

# Counting prime numbers
prime_count = len(prime_numbers)

# Printing the results
print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", prime_count)