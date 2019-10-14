import numpy

P = list(map(float,input().split()))
x = int(input())
Proot = numpy.polyval(P,x)

print(Proot,end="")