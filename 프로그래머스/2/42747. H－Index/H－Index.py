def solution(citations):
    answer = -1
    citations.sort(reverse=True)
    n = len(citations)
    
    max_val = citations[0]
    
    for i in range(n):
        tmp = min(i + 1, citations[i])
        answer = max(answer, tmp)
            
    
    return answer