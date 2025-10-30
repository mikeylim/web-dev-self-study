# brute-force method
import sys 
str_input = sys.stdin.readline()
bomb_input = sys.stdin.readline()
firstIf = len(str_input) >= 1 and len(str_input) <= 1000000
secondIf = len(bomb_input) >= 1 and len(bomb_input) <= 36
thirdIf = len(set(bomb_input)) == len(bomb_input)

while (bomb_input in str_input):
    if (firstIf and secondIf and thirdIf):
        str_input = str_input.replace(bomb_input, "")
    else:
        break
if (len(str_input) == 0):
    print("FRULA")
else:
    print(str_input)