from itertools import combinations
n=int(input())
lst=[list(map(int, input().split())) for i in range(n)]
ans=[]
frlst=list(combinations(list(range(n)), n//2))
for i in range(len(frlst)//2):
    start = list(combinations(frlst[i], 2))
    link = list(combinations(frlst[len(frlst)-i-1], 2))
    st_rank=0
    lk_rank=0
    for j in range(len(start)):
        st_rank+=lst[start[j][0]][start[j][1]]+lst[start[j][1]][start[j][0]]
        lk_rank+=lst[link[j][0]][link[j][1]]+lst[link[j][1]][link[j][0]]
    ans.append(abs(st_rank-lk_rank))
print(min(ans))