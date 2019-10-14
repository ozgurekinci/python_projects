ksayi = int(input())

klist = []
for i in range(ksayi):
    command = input().split()
    if command[0] == "insert":
        klist.insert(int(command[1]),int(command[2]))
    elif command[0] == "remove":
        klist.remove(int(command[1]))
    elif command[0] == "append":
        klist.append(int(command[1]))
    elif command[0] == "sort":
        klist.sort()
    elif command[0] == "pop":
        klist.pop()
    elif command[0] == "reverse":
        klist.reverse()
    elif command[0] == "print":
        print(klist)
