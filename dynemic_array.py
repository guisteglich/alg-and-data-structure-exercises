#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    
    # Here we use List Comprehension instead of writing arr = [[]]*n
    arr = [[] for i in range(n)]
    lastAnswer = 0
    result = []
    
    for q in queries:
        if q[0] == 1:
            index = (q[1] ^ lastAnswer) % n
            arr[index].append(q[2])
            
        else:
            index = ((q[1] ^ lastAnswer) % n)
            index_of_internal_list = q[2] % len(arr[index % n])
            
            lastAnswer = arr[index][index_of_internal_list]
            result.append(lastAnswer)
            
    return result
    
    # Write your code here

print(dynamicArray(2, ['105', '117', '103', '210', '211']))
