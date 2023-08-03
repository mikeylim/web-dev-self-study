# 2750번

# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	178760	101895	70283	57.959%
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 5
# 5
# 2
# 3
# 4
# 1
# 예제 출력 1 
# 1
# 2
# 3
# 4
# 5

n = input()
arr = []
for num in range(int(n)):
    arr.append(int(input()))

# using bubble sort
for i in arr:
    # keeps swapping by comparing with previous element
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+ 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# prints arr
for answer in arr:
    print(answer)