def owf(n):
    if n%3 == 0: return str(4)
    else: return str(n%3)
n=int(input())
answer = ''
while 1:
    answer = owf(n)+answer
    if n%3 == 0: n=n-1
    n= int(n/3)
    if n==0 : break
print(answer)