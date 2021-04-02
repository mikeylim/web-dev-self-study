# 알파벳 찾기

# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치

# 예제 입력
# baekjoon

# 예제 출력
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1


# S = list(input())

# alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# for i in range(len(S)):
#     if(S[i] == )


# for alphabet in alphabetList:
#     if(S[0] == alphabet):
#         # print("letter - ", letter)
#         print(alphabetList.index(alphabet), end=" ")  # too early!
#         break
#     else:
#         # print("alphabet - ", alphabet)
#         print('-1', end=" ")
#         continue



s = list(map(str, input()))
print('s =', s)
aList = list('abcdefghijklmnopqrstuvwxyz')
print('aList =', aList)
array = [-1 for i in range(len(aList))]
print('array =', array)

for i in range(len(s)):
    print('s[i] =', s[i])
    print('aList.index(s[i]) =', aList.index(s[i]))
    print('array[aList.index(s[i])] =', array[aList.index(s[i])])
    if array[aList.index(s[i])] == -1:
        array[aList.index(s[i])] = i
        print('array in for loop =', array)

for j in array:
    print(j, end=" ")
    