stringInput = input("")
strList = stringInput.split(" ")
x = int(strList[0])
y = int(strList[1])
if x > y:
    print(">")
elif x < y:
    print("<")
elif x == y:
    print("==")