n, m, k = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

if n > m:
    print("normal")

else:
    for i in range(m-n+1):
        if x == y[i:i+n]:
            print("secret")
            exit()
    print("normal")
