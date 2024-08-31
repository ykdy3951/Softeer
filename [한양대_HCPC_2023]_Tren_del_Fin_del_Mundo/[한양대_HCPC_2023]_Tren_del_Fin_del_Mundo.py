class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} {self.y}"
    
l = []
for i in range(int(input())):
    x, y = map(int, input().split())
    l.append(Point(x, y))

print(sorted(l, key=lambda o: o.y)[0])