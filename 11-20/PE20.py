# Project Euler problem 20

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

if __name__ == "__main__":
    fact = 1
    for i in range(1,101):
        fact *= i
    print(f" 100! == {fact}")
    strfact = str(fact)
    sum = 0
    for i in range(len(strfact)):
        sum += int(strfact[i])
    
    print(f"The sum of the digits of 100! == {sum}")