import numpy

xyz = [int(x) for x in (input().split())]
  
for i in xyz:
    if not 1 <= i <=3:
        quit()
zeros = numpy.zeros((xyz), dtype = int)
ones = numpy.ones((xyz), dtype = int)
print(zeros)
print(ones)