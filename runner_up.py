while True:
    n = int(input("n: "))
    if 2 <= n <=10:
        break

while True:
    a = input("a: ")
    a = [int(x) for x in a.split()]
    if len(a) != n:
        pass
    else:
        break

for i in a:
    if -100 <= i <=100:
        pass
    else:
        quit()
a.sort(reverse=True)
amax = max(a)

for i in a:
    if i == amax:
        pass
    else:
        print(i)
        break
    
