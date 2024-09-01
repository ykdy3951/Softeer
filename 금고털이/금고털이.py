from heapq import *

h = []
b, n = map(int, input().split())

for i in range(n):
    x, y = map(int, input().split())
    heappush(h, [-y, x])

ans = 0
while h:
    y, x = heappop(h)
    y *= -1
    ans += min(x, b) * y
    b -= x

    if b <= 0:
        break

print(ans)