'''
n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans=0
tmp=0
for i in range(m):
    if tmp<k:
        ans+=lst[-1]
        tmp+=1
    else:
        ans+=lst[-2]
        tmp=0
print(ans)
'''

'''
arr=[]
n, m = map(int, input().split())
for i in range(n):
    lst = list(map(int, input().split()))
    arr.append(min(lst))
print(max(arr))
'''

'''
n, m = map(int, input().split())
ans=0
while True:
    if n%m==0:
        n/=m
        ans+=1
    else:
        n-=1
        ans+=1
    if n==1: break
print(ans)
'''
