def solution(n, lost, reserve):
    answer = 0
    
    lst = [1 for _ in range(n + 1)]
    
    lst[0] = -1
    
    for num in lost:
        lst[num] -= 1
    
    for num in reserve:
        lst[num] += 1
        
    print(lst)
        
    for i in range(1, n + 1):
        if lst[i] == 0:
            if lst[i - 1] == 2:
                lst[i - 1] -= 1
                lst[i] += 1
                continue
            
            if i != n and lst[i + 1] == 2:
                lst[i + 1] -= 1
                lst[i] += 1
                continue
                
    print(lst)
                
    answer = lst.count(1) + lst.count(2)
    
    
    
    
    return answer