# create 3 list
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 4, 8, 9, 3]

# create a empty list to store common number
common = []

# for loop checks if i in list 1 then check for list 2
# then check for list 3 also

for i in list1:
    if i in list2 and i in list3:

        # if common number present all the 3 list then add a number(i)
        #  then check if is already in the common list
        #  if it not in the common list the add by using append(i)

        if i not in common:
            common.append(i)

# print the output
print("Duplicates in all three lists:", common)
