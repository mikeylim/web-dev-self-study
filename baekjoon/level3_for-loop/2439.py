n = int(input())
for stars in range(1, n+1):
    print(f"{' ' * (n-stars)}{'*' * stars}")