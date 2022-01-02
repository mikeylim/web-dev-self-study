x = input()
sList = list(x)

total = 0
for s in sList:
    if s == '(':
        total += 1
    elif s == ')':
        total -= 1
    if s == '[':
        total += 2
    elif s == ']':
        total -= 2
    if total < 0:
        print('no')
        print(total)
        break
    if s == '.':
        break
if total == 0:
    print('yes')
    print(total)
if total > 0:
    print('no')