import itertools as it
from itertools import groupby

wording = input()

print(list(groupby(wording, key = lambda x : x)))

