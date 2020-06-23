# # i = int(input())
# # cnt = 0
# # count = 0
# # score = 0

# # for x in range(i):
# #     cnt = 0
# #     for j in input():
# #         if j == 'X':
# #             cnt = 0
# #         else:
# #             cnt += 1
# #             print("cnt =", cnt)
# #         print("j =", j)
# #         print("cnt after else =", cnt)
# #         for addNum in range(cnt+1):
# #             print("addNum =", addNum)
# #             score += addNum
# #             print(f"score = {score}")
# #         # score += cnt * (cnt + 1) // 2
# #         print(f"score = {score} \i")
# #         # while(j != 'X'):
# #         #     print("j =", j)
# #         #     cnt += 1
# #         #     score = cnt * (cnt + 1) // 2
# #         #     print("cnt =", cnt)
# #         #     break
# #         # print("j =", j)
# #         # print("cnt =", cnt))
# #     # score = count * (count + 1) // 2
# # print(score)


n = int(input())
for i in range(n):
    Num = input()
    cnt = 0
    score = 0
    for j in range(len(Num)):
        if Num[j] == "O":
            cnt += 1
            score += cnt
        elif Num[j] == "X":
            cnt = 0
            score += 0
    print("score =", score)