import numpy as np

num = input()
num = num.replace(" ","")
num = int(num[0])
def list_len(num):
    global z
    z = []
    for k in range(num):
        y = input()
        y = y.replace(" ","")
        y = [int(x) for x in y]
        z.append(y)

list_len(num)

my_array = np.array(z)
print(np.transpose(my_array))
print(my_array.flatten())