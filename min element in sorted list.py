# Get user input
input_str = input("Enter numbers (space separated): ")

# Convert to list of integers
# and store in the list a
a = []
for item in input_str.split():
    a.append(int(item))

# Assume the first number is the minimum
min_element = a[0]

# Loop to find the minimum
# check every number with the previous one stored in the min_element
for i in a:
    if i < min_element:
        min_element = i

        # when the min_element and i is equal
        # then print the output

print("Minimum element is:", min_element)
