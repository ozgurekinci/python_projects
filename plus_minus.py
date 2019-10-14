#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus,minus,zeros = ([],[],[])
    for i in arr:
        plus = [i for i in arr if i > 0]
        minus = [i for i in arr if i < 0]
        zeros = [i for i in arr if i == 0]

        plus2 = len(plus)/n
        minus2 = len(minus)/n
        zeros2 = len(zeros)/n
    print("{0:8.6f}".format(plus2))
    print("{0:8.6f}".format(minus2))
    print("{0:8.6f}".format(zeros2))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
