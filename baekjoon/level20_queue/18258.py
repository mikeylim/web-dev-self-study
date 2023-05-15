queue = []
numCommands = int(input());

for i in range(numCommands):
    eachCommand = input()
    if "push" in eachCommand:
        comList = list(eachCommand.split(" "))
        queue.append(int(comList[1]))
    elif "pop" in eachCommand:
        if len(queue) < 1:
            print(-1)
        else:
            print(queue.pop(0))
    elif "size" in eachCommand:
        print(len(queue))
    elif "front" in eachCommand:
        if len(queue) < 1:
            print(-1)
        else:
            print(queue[0])
    elif "back" in eachCommand:
        if len(queue) < 1:
            print(-1)
        else:
            print(queue[-1])
    elif "empty" in eachCommand:
        if len(queue) < 1:
            print(1)
        else:
            print(0)