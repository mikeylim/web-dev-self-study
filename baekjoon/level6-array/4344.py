c = input()
total = 0
average = 0
rounded = 0
smartStudents = 0
rateOfSmartStudents = 0

for i in range(int(c)):
    grade = input().split(" ")
    # finding sum & average
    numOfStudents = int(grade[0])
    for s in range(numOfStudents):
        total += int(grade[s+1])
        average = total / numOfStudents
    
    for f in range(numOfStudents):
        if int(grade[f+1]) > float(average):
            smartStudents += 1

    rateOfSmartStudents = round((smartStudents / numOfStudents) * 100, 3)
    total = 0
    smartStudents = 0
    average = 0
    print("{:.3f}%".format(rateOfSmartStudents))