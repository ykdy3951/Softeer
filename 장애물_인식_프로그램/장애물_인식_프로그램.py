from collections import deque

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"{self.x} {self.y}"
        

n = int(input())
l = [list(map(int,list(input()))) for _ in range(n)]
vst = [[0]*n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = []
for i in range(n):
    for j in range(n):
        if l[i][j] == 0:
            continue
        if vst[i][j] != 0:
            continue

        d = deque()
        d.append(Point(i, j))
        cnt = 0
        vst[i][j] = 1
        while d:
            p = d.popleft()
            cnt += 1
            for k in range(4):
                np = p + Point(dx[k], dy[k])
                if np.x < 0 or np.x >= n or np.y < 0 or np.y >= n:
                    continue
                if l[np.x][np.y] == 0:
                    continue
                if vst[np.x][np.y] != 0:
                    continue
                vst[np.x][np.y] = 1
                d.append(np)
        
        ans.append(cnt)

print(len(ans))
for i in sorted(ans):
    print(i)