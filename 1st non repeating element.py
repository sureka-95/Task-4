
# Get user input
input_str = input("Enter numbers separated by spaces: ")

# Convert the input string to a list of integers
numbers = []
for item in input_str.split():
    numbers.append(int(item))

# Find the first non-repeating element

# count the number a how many time it present
a = False
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j] and i != j:
            count += 1

    # the count of a number which is zero is the non repeated one
    if count == 0:

        #print the output

        print("First non-repeating element is:", numbers[i])

        # when a is true then its break the loop
        a = True
        break

# if none of number count will be zero then print the output
if not a:
    print("No non-repeating element found.")
