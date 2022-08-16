import sys
n, m = map(int, sys.stdin.readline().split())
run = []
for _ in range(n):
    sm=0
    grp=list(map(int, sys.stdin.readline().split()))
    sml=[]
    for i in grp:
        sm+=i
        sml.append(sm)
    run.append(sml)
print(run)
anslst=[]
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans=0
    for j in range(x1-1, x2):
        if y1>1:
            ans+=(run[j][y2-1]-run[j][y1-2])
        else:
            ans+=run[j][y2-1]
    anslst.append(ans)
for a in anslst:
    print(a)