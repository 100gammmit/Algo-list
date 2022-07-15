import heapq
def solution(sc, K):
    answer = 0
    heapq.heapify(sc)
    for i in range(len(sc)-1):
        if sc[0] >= K:
            break
        heapq.heappush(sc, heapq.heappop(sc)+(heapq.heappop(sc)*2))
        answer+=1
        print(sc)
    if sc[0] < K:
        answer=-1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))