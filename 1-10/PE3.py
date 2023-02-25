# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600,851,475,143 ?
import math

def isPrime(num):
    if(num <= 1):
        return False
    for i in range (2, int(math.sqrt(num))):
        if(num % i == 0):
            return False
    return True

def findHighestPrimeFactor(number):
    testPrime = 2

    while(number > 1):
        if(number % testPrime == 0):
            number /= testPrime
            continue
        else:
            testPrime += 1
            while(not isPrime(testPrime)):
                testPrime += 1
    return testPrime

print("Highest prime factor of 12: ")
print(findHighestPrimeFactor(12))
print("Highest prime factor of 13195: ")
print(findHighestPrimeFactor(13195))
print("Highest prime factor of 600851475143: ")
print(findHighestPrimeFactor(600851475143))
print()
