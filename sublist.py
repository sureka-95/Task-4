#create a list for given numbers
numbers = [4, 2, -3, 1, 6]

# declare the condition to find  sum of sublist  is 0
condition = False

# Loop to check all sublists
for i in range(len(numbers)):
    sum = 0
    for j in range(i, len(numbers)):
        sum += numbers[j]

        #if the sum is true then print
        if sum == 0:
            print("Sublist with sum 0 condition:", numbers[i:j+1])
            condition= True
            break

    if condition:
        break
#if not met the condition
if not condition:
    print("No sublist with sum 0 found.")

