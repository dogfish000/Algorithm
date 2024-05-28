from collections import deque

def solution(priorities, location):
    answer = 0
    
    dq = deque()
    
    for i in range(len(priorities)):
        dq.append([priorities[i], i])
    
    
    while True:
        tmp = dq.popleft()
        is_max = True
        for d in dq:
            if d[0] > tmp[0]:
                is_max = False
                dq.append(tmp)
                break
        
        if is_max:
            answer += 1
            if tmp[1] == location:
                break
                
            
    
    
    return answer