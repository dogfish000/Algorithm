def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            max_val = 0
            for k in range(4):
                if j != k:
                    max_val = max(max_val, land[i -1][k])
            land[i][j] += max_val
                    
                    
    answer = max(land[-1])
                
            
            
            
    return answer