n = int(input())
for x in range(1, n + 1):
    cases = input().split(" ")
    print("Case #{}: {}".format(x, int(cases[0]) + int(cases[1])))