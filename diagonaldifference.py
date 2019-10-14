#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    #primary diagonal
    primsum = 0
    for i in range(n):
        primsum += arr[i][i]
    #secondary diagonal
    secsum = 0
    for i in range(n):
        secsum += arr[i][n-1-i]
    print(abs(primsum-secsum))

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)