time = input("").split(" ")
h = int(time[0])
if h == 0:
    h = 24
m = int(time[1])
inputTimeInMin = h * 60 + m
alarmTimeInMin = inputTimeInMin - 45
h = alarmTimeInMin // 60
m = alarmTimeInMin % 60

print(h, m)