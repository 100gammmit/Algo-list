n=int(input())
m=n
ans=int(n/5)
m=m%5
while 1:
    if m%3==0: break
    m+=5
    ans-=1
    if m > n: break
if m > n: ans=-1
else: ans+=m/3
print(int(ans))