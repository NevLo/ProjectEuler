# Project Euler problem 9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import math


def pythagTripletCheck(a,b):
    return math.sqrt(a**2 + b**2) % 1 == 0
        
def pythagAdd(a,b,c):
    return ((a + b + c) == 1000)


def findTriple():
    a = 3
    b = 0
    c = 0
    while(a < 500):
        b = a+1
        while(b < 500):
            if(pythagTripletCheck(a,b)):
                c = int(math.sqrt(a**2 + b**2))
                print(f"Found pythagorean triple: {a}, {b}, {c}")
                if(pythagAdd(a,b,c)):
                    print("Previous triple satisfied condition a + b + c = 1000")
                    return [a,b,c]
            b += 1
        a += 1
    return [-1,-1,-1]

if __name__ == "__main__":  
    arr = [0,0,0]
    arr = findTriple()

    product = arr[0] * arr[1] * arr[2]

    print(f"the product of the pythagorean triple where a + b + c = 1000 is : {product}")





