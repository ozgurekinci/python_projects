import numpy

def arrays(arr):
    x = numpy.array(arr,float)
    return x[::-1]
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)