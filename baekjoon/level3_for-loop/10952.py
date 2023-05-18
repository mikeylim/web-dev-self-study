# while(True):
#     inputs = input().split(" ")
#     a,b = map(int, inputs)
#     if a == 0 and b == 0:
#         break
#     print(a + b)

while(True):
    inputs = input()
    a,b = map(int, inputs.split(" "))
    if inputs == "0 0":
        break
    print(a + b)