
def solution(storey):
    answer = 0
    
    lst = []
    
    while storey >= 1:
        a = storey % 10
        lst.append(a)
        
        storey = storey // 10
        
    
    for i in range(len(lst)):
        if i <= len(lst) -2:
            if lst[i] > 5:
                answer += 10 - lst[i]
                lst[i + 1] += 1
            elif lst[i] < 5:
                answer += lst[i]
            else:
                if lst[i + 1] >= 5:
                    answer += 5
                    lst[i + 1] += 1
                else:
                    answer += 5
        
        else:
            answer += min(lst[i], 10 - lst[i] + 1)
            
    
    
    return answer