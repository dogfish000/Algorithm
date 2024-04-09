from collections import deque

def solution(cacheSize, cities):
    time = 0
    
    dq = deque()
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        _city = city.lower()
        if _city in dq:
            dq.remove(_city)
            dq.append(_city)
            time += 1
            
            
        if _city not in dq:
            if len(dq) < cacheSize:
                dq.append(_city)
                time += 5
            elif len(dq) == cacheSize:
                dq.popleft()
                dq.append(_city)
                time += 5
        
        
    
    
    
    answer = time
    return answer