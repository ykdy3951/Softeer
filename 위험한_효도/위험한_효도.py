a, b, d = map(int, input().split())
s = a + b
t = s * (d // a) + d % a if d > a else d
t += s * (d // b) + d % b if d > b else d
print(t)