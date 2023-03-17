# Project Euler problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
# that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def isAbundantNumber(num):
    sum = 0
    for i in range(1,(num//2)+1):
        if(num % i == 0):
            sum += i
    return sum > num

def findAbundantSums(nums):
    sums = []
    for i in range(len(nums)):
        #print(f"starting range: i = {i} total range: {len(nums)}")
        if i == len(nums):
            break
        for j in range(len(nums)):

            temp = nums[i] + nums[j] 
            if(temp > 28123):
                del nums[-1]
                break
            else:
                if temp not in sums:
                    #print(f"Appending: {temp} to sums")
                    sums.append(temp)
    return sums



if __name__ == "__main__":
    sum = 0
    abundantNums = []
    for i in range(12, 28124):
        if(isAbundantNumber(i)):
            abundantNums.append(i)
    print(f"length of abundantNums = {len(abundantNums)}")
    sums = findAbundantSums(abundantNums)
    print(sums)
    sums.sort()
    for i in range(sums[-1]):
        if(i not in sums):
            sum += i
    print(sums)       
    print(f"The sum of all abundant numbers is: {sum}")