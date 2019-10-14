import numpy

entry = int(input())
listlist = []
for i in range(entry):
    matlist = list(map(int,input().split()))
    listlist.append(matlist)
matrix = numpy.array(listlist).reshape(entry,entry)
print(round(numpy.linalg.det(matrix)))