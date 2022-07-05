lst=list(range(10000))
for i in range(10000):
    p=0
    for j in str(i):
        p+=int(j)
    p+=i
    if p in lst:
        lst.remove(p)
for i in lst:
    print(i)