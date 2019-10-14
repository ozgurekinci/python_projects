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

seclow = sortedlist[1][1]
finallist = []

for item in sortedlist:
    if item[1] == seclow:
        finallist.append(item)
    else:
        pass

# finallist = sorted([sortedlist[0][0], sortedlist[1][0]])
# for i in range(len(sortedlist)):
#     if sortedlist[i][1] == seclow:
#         finallist.append(sortedlist[i])
#     else:
#         pass
finallist = sorted([i[0] for i in finallist])

print(*finallist, sep="\n")
