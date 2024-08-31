t=0
for _ in range(5):
    a, b = input().split()
    h1, m1 = map(int, a.split(':'))
    h2, m2 = map(int, b.split(':'))
    t += (h2 - h1) * 60 + m2 - m1
print(t)