#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    snew = ""
    num = 0
    for i in range(0,len(s),3):
        snew = s[i:i+3]
        comp = "SOS"
        j = 0
        while j < 3:
            if snew[j] != comp[j]:
                num += 1
                j += 1
            else:
                j += 1
    return(num)


if __name__ == '__main__':

    s = input()

    result = marsExploration(s)
    print(result)