n, m = map(int, input().split())
x, y = [], []

for i in range(n):
    x.append(list(map(int,input().split())))
for j in range(m):
    y.append(list(map(int,input().split())))

i, j = 0, 0
di, dj = x[0][0], y[0][0]
ans = 0
while True:
    ans = max(y[j][1]-x[i][1], ans)

    if di > dj:
        j += 1
        dj += y[j][0]
    
    elif dj > di:
        i += 1
        di += x[i][0]

    else:
        i += 1
        j += 1

        if i >= n or j >= m:
            break

        di += x[i][0]
        dj += y[j][0]

print(ans)