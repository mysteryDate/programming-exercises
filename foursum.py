# Given an array A of size N, find all combination of four elements in the array whose sum is equal to a given value K.
# For example, if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and K = 23,
# one of the quadruple is “3 5 7 8” (3 + 5 + 7 + 8 = 23).
#
# Input:
# The first line of input contains an integer T denoting the no of test cases.
# Then T test cases follow. Each test case contains two lines.
# The first line of input contains two integers N and K. Then in the next line
#  are N space separated values of the array.
#
# Output:
# For each test case in a new line print all the quadruples
# present in the array separated by space which sums up to value of K.
# Each quadruple is unique which are separated by a delimeter "$" and are in increasing order.
#
# Constraints:
# 1<=T<=100
# 1<=N<=100
# -1000<=K<=1000
# -100<=A[]<=100
#
# Example:
# Input:
# 2
# 5 3
# 0 0 2 1 1
# 7 23
# 10 2 3 4 5 7 8
# Output:
# 0 0 1 2 $
# 2 3 8 10 $2 4 7 10 $3 5 7 8 $

# I don't think it's possible to do better than O(n^2) here


def find_four_sum(array, goal):
    pairs = {}
    result = []
    for i in range(len(array[:-1])):
        for j in range(i + 1, len(array)):
            pair_sum = array[i] + array[j]
            if pair_sum <= goal:
                if pair_sum not in pairs:
                    pairs[pair_sum] = (i, j)
    for i in range(len(array)):
        for j in range(len(array[i+1:])):
            new_sum = array[i] + array[j]
            new_goal = goal - new_sum
            if new_goal in pairs:
                i1, j1 = pairs[new_goal]
                if i1 != i and j1 != i and i1 != j and j1 != j:
                    new_result = sorted([array[x] for x in [i, j, i1, j1]])
                    result.append(new_result)
    return result


MAX_FACTORS = 4
# K = 3
# A = "0 0 2 1 1"
# K = 23
# A = "10 2 3 4 5 7 8"
K = 179
# A = "88 84 3 51 54 99 32 60 76 68 39 12 26 86 94 39 95 70 34 78 67 1 97 2 17 92 52"
A = "1 39 39 51 88 100"
A = [int(x) for x in A.split(" ")]
A = sorted(A)
print(A)
ss = find_four_sum(A, K)
print(ss)

