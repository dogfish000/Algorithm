from collections import deque

def solution(order):
    answer = 0
    
    box = deque()
    container = deque()
    
    for i in range(1, len(order) + 1):
        box.append(i)
    
    
    for o in order:
        if box and o >= box[0]:
            while True:
                tmp = box.popleft()
                if tmp == o:
                    answer += 1
                    break
                else:
                    container.append(tmp)
            
                
        else:
            if container and container[-1] == o:
                container.pop()
                answer += 1
            else:
                break
            

        
                
        
        
            
                    
                
            
    
    
    return answer