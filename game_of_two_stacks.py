def twoStacks(maxSum, a, b):
    # Write your code here
    sum_mov, i, j = 0, 0, 0
    while sum_mov < maxSum:
        if ((a[i] + sum_mov) < maxSum) and len(a) > i:
            sum_mov += a[i]
            i+=1
        elif ((b[j] + sum_mov) < maxSum) and len(b) > j:
            sum_mov += b[j]
            j +=1
        else:
            break
    return i + j
        

A = [4, 2, 4, 6, 1]
B = [2, 1, 8, 5]

C = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0]
D = [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]

print(twoStacks(10, A, B))

print(twoStacks(12, C, D))