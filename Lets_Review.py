# Enter your code here. Read input from STDIN. Print output to STDOUT
while True:
    t = int(input())
    if 1 <= t <= 10:
        break
slist = []

for i in range(t):
    s = input()
    slist.append(s)
for i in slist:
    seven= []
    sodd = []
    for j in range(len(i)):
        if j%2==0:
            seven.append(i[j])
        else:
            sodd.append(i[j])

    print(*seven,"  ", *sodd,sep="")
        