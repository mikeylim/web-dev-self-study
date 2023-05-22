n = input()
grade = list(map(float, input().split(" ")))
maxGrade = max(grade)
sum = 0
for g in grade:
    newGrade = g / maxGrade * 100
    sum += newGrade
print(sum / len(grade))