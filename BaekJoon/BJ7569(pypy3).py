from collections import deque
m, n, h = map(int, input().split())
grp={}
grow=[]
hh=[]
nn=[]
mm=[]
k=0
for r in range(1, h+1):
    for i in range(1, n+1):
        for j in range(1, m+1):
            if h > 1:
                if r==1:
                    hh=[k+(m*n)]
                elif r == h:
                    hh=[k-(m*n)]
                else:
                    hh=[k-(m*n), k+(m*n)]
            if n>1:    
                if i==1:
                    nn=[k+m]
                elif i == n:
                    nn=[k-m]
                else:
                    nn=[k-m, k+m]
            if m>1:    
                if j==1:
                    mm=[k+1]
                elif j == m:
                    mm=[k-1]
                else:
                    mm=[k-1, k+1]
            grp[k]=hh+nn+mm
            k+=1

for i in range(n*h):
    grow.append(list(map(int, input().split())))
grw = sum(grow, [])

v=deque([i for i in range(len(grw)) if grw[i]==1])
def TMT(graph, start, visited):
    ans=-1                  
    while start:
        queue = start.copy()
        for i in queue:
            start.popleft()
            for j in graph[i]:
                if visited[j] == 0:
                    visited[j] = 1
                    start.append(j)
        #print(start)
        ans+=1
    if 0 in visited:
        ans=-1
    #print('',visited)
    return ans
#print(grp, grw)
print(TMT(grp, v, grw))