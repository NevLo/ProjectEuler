# Project Euler Problem 4

#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
    strnum = str(number)
    for i in range(len(strnum)):
        if(strnum[i] != strnum[len(strnum)-1-i]):
            return False
    return True

if __name__ == "__main__":  
    maxPalindrome = 0
    palinI = 0
    palinJ = 0
    for i in range(100,1000):
        for j in range(100,1000):
            test = i * j
            if(isPalindrome(test) and test > maxPalindrome):
                maxPalindrome = test
                palinI = i
                palinJ = j
    print("The maximum palindrome of a product of two 3-digit numbers is :")
    print(f"{palinI} * {palinJ} = {maxPalindrome}")
