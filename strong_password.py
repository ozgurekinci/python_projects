#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    # if len(password) < 6:
    #     print(6-n)
    #     quit()
    lc,uc,dig,spe = (0,0,0,0)

    for i in password:
        if i in numbers:
            dig += 1
        elif i in lower_case:
            lc += 1
        elif i in upper_case:
            uc += 1
        elif i in special_characters:
            spe += 1
        if lc >= 1 and uc >= 1 and dig >= 1 and spe >= 1:
            break
    need = len([i for i in (lc,uc,dig,spe) if i == 0])
    print(need if (6-n)<need else (6-n))
    list.remo

if __name__ == '__main__':
    n = int(input())

    password = input()

    answer = minimumNumber(n, password)
