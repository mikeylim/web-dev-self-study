# Who have not handed in ? 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	68193	36139	31875	53.388%
# 문제
# Professor M of JOI University teaches a course on computer programming.
# 30 students take the course and are numbered 1 to 30.
# 28 students have handed in their homework but the other two students have not yet.
# Write a program which, given the numbers of students who have handed in their homework,
# outputs the numbers of the students who have not handed in their homework.

# 입력
# The input file contains 28 lines.
# Each line of the input file contains a number of a student who has handed in her/his homework.
# The numbers in the input file are between 1 and 30, inclusive, and distinct from each other. The numbers are given in no particular order.

# 출력
# You should submit the output file which consists of two lines,
# and each of lines should contain the number of a student who has not handed in her/his homowork.
# The number in the first line should be less than the one in the second line.

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
