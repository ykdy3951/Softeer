n=int(input());l=list(map(int,input().split()))
cnt,min=0,1000000
for i in range(1,n):
    t=l[i]-l[i-1]
    if t < min:
        cnt=1
        min=t
    elif t == min:
        cnt+=1
print(cnt)