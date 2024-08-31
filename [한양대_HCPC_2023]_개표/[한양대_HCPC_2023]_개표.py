for i in range(int(input())):
    n = int(input())
    print(' '.join(['++++']*(n//5)+['|'*(n%5)]))