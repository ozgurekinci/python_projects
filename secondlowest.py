while True :
    n = int(input())
    if 2 <= n <= 5:
        break

biglist = []
for i in range(n):
    clist = []
    clist.append(input())
    clist.append(float(input()))
    biglist.append(clist)

sortedlist = sorted(biglist, key=lambda x:x[1])
finallist = [item[1] for item in sortedlist]

mingrade = min(finallist)
secondgrade = []

for i in sortedlist:
    if i[1] == mingrade:
        pass
    else:
        mingrade = i[1]
        break

for i in sortedlist:
    if i[1] == mingrade:
        secondgrade.append(i[0])
        # sorted(secondgrade)
        secondgrade.sort()
    else:
        pass

print(*secondgrade, sep="\n")