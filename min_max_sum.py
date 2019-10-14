#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    # arr.sort()
    # minsum, maxsum, i = (0,0,0)
    # while i < len(arr):
    #     minsum = minsum + arr[i]
    #     maxsum = maxsum + arr[i]
    #     i += 1
    # minsum = minsum - arr[i-1]
    # maxsum = maxsum - arr[0]
    # print(minsum, " ", maxsum)
    x = sum(arr)
    print(x-min(arr), x-max(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
