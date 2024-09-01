n = int(input())
l = list(map(int, input().split()))
m = max(l)

ans = 0
for i in range(2, m + 1):
    cnt = 0
    for j in l:
        if j % i == 0:
            cnt += 1
    ans = max(ans, cnt)
print(ans)