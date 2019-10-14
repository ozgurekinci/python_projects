#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from collections import OrderedDict
# Complete the alternate function below.
def alternate(s):
    counts = Counter(s).most_common() 
    counts = counts[::-1]
    print(counts)

    for v in counts:
        del counts[v]
        print(counts)

    
if __name__ == '__main__':
    l = int(input().strip())

    s = input()

    result = alternate(s)