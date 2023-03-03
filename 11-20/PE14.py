# Project Euler problem 14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.



def collatz(num):
    if(num == 1):
        return 1 
    if(num % 2 == 0):
        return 1 + collatz(int(num/2))
    else:
        return 1 + collatz((num * 3) + 1)

if __name__ == "__main__":
    max = 0
    maxi = 0
    for i in range(1,1000000):
        num = collatz(i)
        if(num > max):
            max = num
            maxi = i
    
    print(f"The starting number with the longest collatz chain under 1million is {maxi} with a length of {max}")
