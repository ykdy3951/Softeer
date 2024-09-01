l = [list(map(int, input().split())) for _ in range(3)]

ans = 10
for i in range(3):
    cnt = [0] * 3
    for j in range(3):
        cnt[0] += abs(1-l[i][j])
        cnt[1] += abs(2-l[i][j])
        cnt[2] += abs(3-l[i][j])
    ans = min(ans, cnt[0], cnt[1], cnt[2])

for i in range(3):
    cnt = [0] * 3
    for j in range(3):
        cnt[0] += abs(1-l[j][i])
        cnt[1] += abs(2-l[j][i])
        cnt[2] += abs(3-l[j][i])
    ans = min(ans, cnt[0], cnt[1], cnt[2])

print(ans)