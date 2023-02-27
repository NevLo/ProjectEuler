# Project Euler problem 5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

def findSmallestFromRange(rge):
    inc = 1
    while(True):
        for i in range(1,rge+1):
            if(inc%i != 0):
                break
        else:
            return inc
        inc += 1

if __name__ == "__main__":  
    print(f"The smallest number that is divided by the range 1-10 is : {findSmallestFromRange(10)}\n")
    start = time.time()
    print(f"The smallest number that is divided by the range 1-20 is : {findSmallestFromRange(20)}")
    end = time.time()
    print(f"total time to calc range 1-20 was {str(end-start)}")
    #this is a really slow implementation (took ~58 seconds to run)
    #there is probably a math function that would do this simpler.
