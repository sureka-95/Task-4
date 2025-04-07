# assign a value of 10 rs
amount = 10

# checks howmany 10 rs coins are used to make the amount 10
for ten in range(0, amount // 10 + 1):

    # checks howmany 5 rs coins are used to make the amount 10
    for five in range(0, (amount- 10*ten) // 5 + 1):
        
        # checks howmany 2 rs coins are used to make the amount 10
        for two in range(0, (amount - 10*ten - 5*five) // 2 + 1):

            # checks howmany 1 rs coins are used to make the amount 10
            for one in range(0, (amount - 10*ten - 5*five - 2*two) + 1):

                #check the total of the combination give the amount rs 10
                if 10*ten + 5*five + 2*two + one == amount:

                    #if  yes print the output
                    print("All combination for making 10rs:")
                    
                    print(f"Rs.10 x {ten}, Rs.5 x {five}, Rs.2 x {two}, Rs.1 x {one}")
