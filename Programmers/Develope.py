import math
def solution(progresses, speeds):
    answer = [1]
    p=[math.ceil((100-progresses[0])/speeds[0])]
    j=0
    for i in range(1, len(progresses)):
        t=math.ceil((100-progresses[i])/speeds[i])
        if p[j]<t:
            p.append(t)
            answer.append(1)
            j+=1
        else:
            answer[j]+=1
            
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))