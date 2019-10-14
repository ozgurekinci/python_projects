#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):

    albet = "abcdefghijklmnopqrstuvwxyz"
    nalbet = []
    for i in s:
        if i.islower() and i.lower() in albet:
            nalbet.append(albet[(albet.index(i.lower())+k)%26])
        elif i.isupper() and i.lower() in albet:
            nalbet.append(albet[(albet.index(i.lower())+k)%26].upper())
        else:
            nalbet.append(i)
    return("".join(nalbet))

if __name__ == '__main__':
    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)
    print(result)