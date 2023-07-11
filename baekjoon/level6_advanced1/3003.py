# BIJELE 성공다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	92618	51196	45312	56.371%
# 문제
# Mirko has found an old chessboard and a set of pieces in his attic. Unfortunately, the set contains only white pieces, and apparently an incorrect number of them. A set of pieces should contain: 

# One king 
# One queen 
# Two rooks 
# Two bishops 
# Two knights 
# Eight pawns 
# Mirko would like to know how many pieces of each type he should add or remove to make a valid set. 

# 입력
# The input consists of 6 integers on a single line, each between 0 and 10 (inclusive). The numbers are, in order, the numbers of kings, queens, rooks, bishops, knights and pawns in the set Mirko found. 

# 출력
# Output should consist of 6 integers on a single line; the number of pieces of each type Mirko should add or remove. If a number is positive, Mirko needs to add that many pieces. If a number is negative, Mirko needs to remove pieces. 

# 예제 입력 1 
# 0 1 2 2 2 7
# 예제 출력 1 
# 1 0 0 0 0 1
# 예제 입력 2 
# 2 1 2 1 2 1
# 예제 출력 2 
# -1 0 0 1 0 7
# 출처
# Contest > Croatian Open Competition in Informatics > COCI 2007/2008 > Contest #2 1번

chessList = [1, 1, 2, 2, 2, 8]
given = input().split()
newList = []
for i in range(len(given)):
    newList.append(chessList[i] - int(given[i]))
print(*newList)