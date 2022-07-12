n=int(input())
lst=list(map(int, input().split()))
d=0
slst=sorted(lst)
ans={slst[0] : 0}
for i in range(1, n):
    if slst[i] > slst[i-1]:
        d+=1
    ans[slst[i]]=d
for i in lst:
    print(ans[i], end=' ')