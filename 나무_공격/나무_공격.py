n, m = map(int, input().split())
a = [sum(map(int, input().split())) for _ in range(n)]

for i in range(2):
    x, y = map(int, input().split())
    for j in range(x - 1, y):
        a[j] = max(a[j] - 1, 0)

print(sum(a))