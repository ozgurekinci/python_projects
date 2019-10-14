#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    t = []
    for i in s:
        if i.isupper():
            t.append(i)
        else:
            pass
    print(len(t)+1)

if __name__ == '__main__':
    s = input()

    result = camelcase(s)
