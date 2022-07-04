n, k = map(int, input().split())
ans=0
coin=[]
for i in range(n):
    coin.append(int(input()))
if coin[-1] <= k:
    ans+=int(k/coin[-1])
    k=k%coin[-1]
for i in range(n-2, -1, -1):
    if coin[i] <= k <= coin[i+1]:
        ans+=int(k/coin[i])
        k=k%coin[i]
print(ans)