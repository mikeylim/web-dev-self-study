import sys

num = int(sys.stdin.readline())

for x in range(num):
    word = sys.stdin.readline().rstrip().split(" ")
    print(int(word[0]) + int(word[1]))