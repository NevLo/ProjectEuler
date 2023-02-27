# Project Euler problem 10

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import PE3

def sumPrimes(num):
    sum = 0
    for i in range(2,num):
        if(PE3.isPrime(i)):
            sum += i
    return sum

if __name__ == "__main__":  
    print(f"the sum of all primes below 10 is {sumPrimes(10)}")
    print(f"the sum of all primes below 2 million is {sumPrimes(2000000)}")   
