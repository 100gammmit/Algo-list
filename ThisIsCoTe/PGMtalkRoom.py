def solution(s):
    min=len(s)   
    for i in range(1, len(s)//2+1):
        t=1
        answer = len(s)
        lst=[]
        for j in range(i, len(s)+1, i): 
            comp=s[j:j+i]                          
            if comp == s[j-i:j]:
                answer-=i
                t+=1
                if comp==s[j+i:j+i+i]:
                    continue
                lst.append(t)                    
            else: t=1
        for k in lst:
            answer+=len(str(k))   
        if min > answer: min=answer
    return min
st = str(input())
print(solution(st))