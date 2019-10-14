#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = s.replace(" ","#").split("#")
    for i,j in enumerate(l):
        if j.isalpha():
            l[i] = j.title()
    return " ".join(l)
if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)