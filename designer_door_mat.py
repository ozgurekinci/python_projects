while True:
    N, M = map(int,(input().split()))
    if 5 < N < 101 and 15 < M < 303:
        break
K=(N+1)//2
noktadash = ".|."
for i in range(1,K):
    print((noktadash*i).center(M,"-"))
print("WELCOME".center(M,"-"))
for i in range(1,K):
    print((noktadash*(K-i)).center(M,"-"),sep="")
