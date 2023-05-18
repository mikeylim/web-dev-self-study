# nX = input().split(" ")
# fN = input().split(" ")
# answerList = []
# for number in fN:
#     if int(number) < int(nX[1]):
#         answerList.append(int(number))
# print(" ".join(map(str, answerList)))

# >> using map() function
n,x = map(int, input().split(" "))
fN = list(map(int, input().split(" ")))
answerList = []
for number in fN:
    if int(number) < x:
        answerList.append(int(number))
print(" ".join(map(str, answerList)))