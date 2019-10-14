#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    t = []
    for i in s:
        if not t:
            t.append(i)
        elif t[-1] == i:
            t.pop(-1)
        else:
            t.append(i)
    if not t:
        print("Empty String")
    else:
        print ("".join(t))



if __name__ == '__main__':
    s = input()

    result = superReducedString(s)