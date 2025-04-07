# create a list for given numbers
numbers = [10, 20, 30, 9]

# assign the target value
target = 59

# initial set a as false to check each numbers
a = False

# Check all triplets using for loop
# check one by one in numbers

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):

            # sum of numbers equal to target value
            if numbers[i] + numbers[j] + numbers[k] == target:

                # print the output where a is true
                print("Triplet found:", numbers[i], numbers[j], numbers[k])
                a = True
                
# else print the below statement
if not a:
    print("No triplet found with sum =", target)
