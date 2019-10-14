import numpy as np

nmp = input()
nmp = nmp.replace(" ","")
n = int(nmp[0])
m = int(nmp[1])
p = int(nmp[2])

def nxp():
    global x
    x = []
    for i in range(n):
        y = input()
        y = y.replace(" ","")
        y = [int(z) for z in y]
        x.append(y)
    return x
def mxp():
    global t
    t = []
    for i in range(m):
        u = input()
        u = u.replace(" ","")
        u = [int(y) for y in u]
        t.append(u)
    return t
nxp()
mxp()

nxparr = np.array(x)
mxparr = np.array(t)
nmparr = np.concatenate((nxparr,mxparr))

print(nmparr)