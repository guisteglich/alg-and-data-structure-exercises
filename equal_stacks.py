'''
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. 
You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 
This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.
'''

def equalStacks(h1, h2, h3):
    # Write your code here
    sum_h1, sum_h2, sum_h3 = sum(h1), sum(h2), sum(h3)
    i, j, k = 0, 0, 0
    while (sum_h1 != sum_h2 or sum_h2 != sum_h3 or sum_h3 != sum_h1):
        if sum_h1 >= sum_h2 and sum_h1 >= sum_h3:
            sum_h1 -= h1[i]
            i +=1
        elif (sum_h2 >= sum_h1 and sum_h2 >= sum_h3):
            sum_h2 -=h2[j]
            j +=1
        elif (sum_h3 >= sum_h1 and sum_h3 >= sum_h2):
            sum_h3 -= h3[k]
            k +=1
    return sum_h1

h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

print(equalStacks(h1, h2, h3))

h4 = [2, 1, 1, 1, 1]
h5 = [3, 2]
h6 = [1, 3, 1]

print(equalStacks(h4, h5, h6))