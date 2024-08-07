import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        tmp1 = heapq.heappop(scoville)
        if tmp1 >= K:
            break
        

        tmp2 = heapq.heappop(scoville)
        new_sco = tmp1 + tmp2 * 2
        heapq.heappush(scoville, new_sco)
        answer += 1
    
    if len(scoville) == 0 or max(scoville) < K:
        answer = -1
        
        
        
    
    
    return answer