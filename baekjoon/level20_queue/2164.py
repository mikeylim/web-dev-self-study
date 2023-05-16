N = int(input())
queue = []
for i in range(N):
    queue.append(i+1)
for x in range(N-1):
    queue.pop(0)
    addNum = queue.pop(0)
    queue.append(addNum)
print(queue[0])