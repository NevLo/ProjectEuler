# Project Euler problem 6.

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 +... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sumSquareDifference(num):
    sumSquare = 0
    for i in range (0, num+1):
        sumSquare += i ** 2
    squareSum = ((num * (num + 1))/2)**2

    return squareSum - sumSquare

if __name__ == "__main__":  
    print(f"The sum square difference of the first ten natural numbers is: {sumSquareDifference(10)}")
    print(f"The sum square difference of the first hundred natural numbers is: {sumSquareDifference(100)}")