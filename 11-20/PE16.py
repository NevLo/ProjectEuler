# Project Euler problem 16

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


if __name__ == "__main__":
    numberString = str(2**1000)
    sum = 0
    for i in range(len(numberString)):
        sum += int(numberString[i])

    print(f"The answer of 2^1000 is {numberString}")
    print(f"The sum of the digits of the number 2^1000 is {sum}")