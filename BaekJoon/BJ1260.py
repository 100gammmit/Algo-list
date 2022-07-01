from collections import deque
n, m, v=map(int, input().split())
vstd={v: False}
grp={v:[]}
for _ in range(m):
    x, y=map(int, input().split())
    if x not in grp:
        grp[x]=[y]
        vstd[x]=False
    else:
        grp[x].append(y)
        grp[x].sort()
    if y not in grp:
        grp[y]=[x]
        vstd[y]=False
    else:
        grp[y].append(x)
        grp[y].sort()


print(grp, vstd)
def DFS(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        print(queue)
        p=queue.popleft()
        print(p, end=' ')
        for i in graph[p]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                     
DFS(grp, v, vstd)
for i in vstd:
    vstd[i]=False
print()
BFS(grp, v, vstd)