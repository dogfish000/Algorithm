def solution(k, dungeons):
    global max_val
    max_val = -1
    N = len(dungeons)
    visited = []
    for i in range(N):
        visited.append(0)
    
    route(k, dungeons, visited, 0)
    
    
    return max_val


def route(k, dg, visited, depth):
    global max_val
    # 리턴
    if depth == len(dg):
        max_val = max(max_val, depth)
        return 
    
    
    # 다음 스텝
    for i in range(len(dg)):
        if k >= dg[i][0] and visited[i] == 0:
            visited[i] = 1
            route(k - dg[i][1], dg, visited, depth + 1)
            visited[i] = 0
    
    max_val = max(max_val, depth)
    return
            
            
    
    
    
    
    