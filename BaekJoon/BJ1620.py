import sys
n, m=map(int, sys.stdin.readline().split())
dict={}
dict2={}
quest=[]
for i in range(1, n+1):
    n=sys.stdin.readline().strip()
    dict[str(i)]=n
    dict2[n]=str(i)
for i in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit(): 
        quest.append(dict[q])
    else:
        quest.append(dict2[q])

for i in quest:
    sys.stdout.write(i+'\n')  