import numpy

numpy.set_printoptions(sign=' ')

my_list = list(map(float,input().split()))
my_array = numpy.array(my_list)
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))
