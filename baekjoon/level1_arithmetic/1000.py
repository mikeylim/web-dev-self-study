stringInput = input("")
numberList = stringInput.split(" ")
total = 0

for number in numberList:
    total += int(number)

print(total)