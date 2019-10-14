import numpy

nxm = list(map(int,input().strip().split()))
a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))

# print((a+b))
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(a**b)

print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.divide(a,b))
print(numpy.mod(a,b))
print(numpy.power(a,b))