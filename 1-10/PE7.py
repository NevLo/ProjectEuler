# Project Euler problem 7

# By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime?
import PE3

def findNthPrime(number):
    inc = 0
    i = 2
    while(True):
        if(PE3.isPrime(i)):
            #print(f"{inc}: {i}")
            inc += 1
            if(inc == number):
                return i
        i += 1

if __name__ == "__main__":  
    print(f"The 6th prime is: {findNthPrime(6)}")
    print(f"The 10001st prime is: {findNthPrime(10001)}")