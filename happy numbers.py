#create a list of numbers
a = [10,501,22,37,100,999,87,351]

# create a empty list for happy numbers
happy_numbers = []

# if num is in a then it assign in n
for num in a:
    n = num
    #create  emptylist which store the value of n
    b = []

    #
    while n != 1 and n not in b:
        b.append(n)
        sum_of_squares = 0
        while n > 0:
            digit = n % 10
            sum_of_squares += digit * digit
            n = n // 10
        n = sum_of_squares

    if n == 1:
        happy_numbers.append(num)

print("Happy numbers in the list:", happy_numbers)
