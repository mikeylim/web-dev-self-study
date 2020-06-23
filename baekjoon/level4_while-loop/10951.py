while(True):
    try:
        inputs = input().split(" ")
        a,b = map(int, inputs)
        print(a + b)
    except:
        break