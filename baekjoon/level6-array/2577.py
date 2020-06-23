a = int(input())
b = int(input())
c = int(input())
strAnswer = str(a*b*c)
for x in range(10):
    count = len(strAnswer.split(str(x)))-1
    print(count)