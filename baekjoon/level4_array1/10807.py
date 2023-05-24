n = int(input())
sList = input().split()
v = int(input())
ct = 0
for s in sList:
    if int(s) == v:
        ct = ct+1
print(ct)