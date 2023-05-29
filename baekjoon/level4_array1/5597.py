
temp = []
for i in range(10):
    temp.append(i+1);
print('temp =',temp)
result = []
for j in range(8):
    num = input()
    print('num = ', num)
    if num not in temp:
        result.append(num)
print('result =',result)

for r in result:
    print('r = ',r)
