#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    ampm = s[-2:]
    if ampm =="AM" and int(s[0:2]) == 12:
        print("00" + s[2:-2])
    elif (ampm == "PM" and int(s[0:2]) == 12) or ampm == "AM":
        print(s[:-2])
    elif ampm == "PM":
        print((str(int(s[:2])+12)) + s[2:-2])



if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
