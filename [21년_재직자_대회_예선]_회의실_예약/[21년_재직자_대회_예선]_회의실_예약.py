d = {}
n, m = map(int, input().split())

for i in range(n):
    s = input()
    d[s] = [0] * 9

for i in range(m):
    s, x, y = input().split()
    for j in range(int(x) + 1 - 10, int(y) + 1 - 10):
        d[s][j] = 1

for i, key in enumerate(sorted(list(d.keys()))):
    print(f'Room {key}:')
    
    avail = []

    temp = -1; now = []
    for j in range(9):
        if d[key][j]:
            if len(now):
                avail.append(now)
                now = []
        else:
            if len(now):
                now[1] = j
            else:
                now = [j, j]
    if len(now):
        avail.append(now)
    
    if avail:
        print(f"{len(avail)} available:")
        for t in avail:
            print(f"{t[0]+9:02d}-{t[1]+10:02d}")

    else:
        print("Not available")

    if i != n - 1:
        print('-----')