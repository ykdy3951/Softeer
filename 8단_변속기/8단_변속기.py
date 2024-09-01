l = list(map(int,input().split()))
x = sorted(l)

if l == x:
    print('ascending')
elif l == x[::-1]:
    print('descending')
else:
    print('mixed')