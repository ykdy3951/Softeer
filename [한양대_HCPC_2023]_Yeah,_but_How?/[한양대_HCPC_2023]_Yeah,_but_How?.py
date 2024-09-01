s = input()
ans = s[0]
for i in range(1, len(s)):
    if s[i-1] == '(' and s[i] == ')':
        ans += '1'
    elif s[i-1] == ')' and s[i] == '(':
        ans += '+'
    ans += s[i]
print(ans)