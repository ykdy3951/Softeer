for i in range(int(input())):
    x, y = input().split()
    print(y[x.upper().index('X')].upper(), end='')