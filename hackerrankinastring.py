#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
# def hackerrankInString(s):
#     comp = "hackerrank"
#     p = 0
#     for i in comp:
#         if p < s.index(i):
#             if i in s[p:]:
#                 p = s.index(i)
#                 continue
#             else:
#                 return "NO"
#                 break
#         else:
#             if i in s[p:]:
#                 p = s.index(i,p) +1
#                 continue
#             else:
#                 return "NO"
#                 break
#     return "YES"

def hackerrankInString(s):
    comp = "hackerrank"
    p = 0
    for i in comp:
        if i in s[p:]:
            p = s.index(i,p) + 1
        else:
            return "NO"
    return "YES"
        
    # numlist = []
    # for i in comp:
    #     if i in s:
    #         if numlist == []:
    #             # s = s[s.index(i):]
    #             numlist.append(s.index(i))
    #         else :
    #             numlist.append(numlist[-1] + s.index(i))                
    #             s = s[s.index(i)+1:]
    #     else:
    #         return "NO"
    # numlistsorted = sorted(numlist)
    # if numlistsorted == numlist:
    #     return "YES"
    # else:
    #     return "NO"



if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)
        print(result)
