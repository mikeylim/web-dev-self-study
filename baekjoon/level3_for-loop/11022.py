n = int(input())
for x in range(1, n + 1):
    cases = input().split(" ")
    print("Case #{}: {} = {}".format(x, cases[0] + " + " + cases[1], int(cases[0]) + int(cases[1])))