# Project Euler problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# example paths of 20x20:
# [rrrrrrrrrrdddddddddd] 10r10d
# [rddddddddddrrrrrrrrr] 10r10d
# [rdrdrdrdrdrdrdrdrdrd] 10r10d
# always have 10 of each.
# formula = n! /

def startArray(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if (i * j == 0):
                array[i][j] = 1
            else:
                array[i][j] = 0
    return array
def print2d(array):
    for i in range(len(array)):
        print(array[i])

if __name__ == "__main__":
    array = [0]*21
    for i in range(21):
        array[i] = [0]*21
    array = startArray(array)

    for i in range(1, len(array)):
        for j in range(1, len(array[i])):
            array[i][j] = array[i-1][j] + array[i][j-1]

    print(f"the number of paths to get from the top left to the bottom right is {array[20][20]}")
    print2d(array)

    
    