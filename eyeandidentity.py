import numpy

dimens = [int(x) for x in input().split()]

if dimens[0] == dimens[1]:
    print(str(numpy.identity(dimens[0])).replace("1", " 1").replace("0"," 0"),end="")
else:
    print(str(numpy.eye(dimens[0],dimens[1], k=1)).replace("1", " 1").replace("0"," 0"),end="")
