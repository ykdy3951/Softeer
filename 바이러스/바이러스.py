k, p, n = map(int, input().split())
MOD = 1000000007

l = [-1] * (n + 1)
l[0] = 1
l[1] = p

def power(p, n):
    if l[n] != -1:
        return l[n]
    if n % 2:
        l[n] = p * power(p, n - 1) % MOD
        return l[n]
    else:
        l[n] = power(p, n // 2) ** 2 % MOD
        return l[n]

print(k * power(p, n) % MOD)