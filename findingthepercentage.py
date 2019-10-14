while True:
    n = int(input())
    if 2 <= n <= 10:
        break

studandmarks = {}


for i in range(n):
    marklist = []
    uname = []
    uname_mark = input()
    marklist = [float(x)  if 0 <=float(x) <=100 else quit() for x in uname_mark.split(" ")[1:]]

    uname = uname_mark.split(" ")[0]
    studandmarks[uname] = marklist

averageq = input()

print("%.2f"%(sum(studandmarks[averageq]) / len(studandmarks[averageq])))