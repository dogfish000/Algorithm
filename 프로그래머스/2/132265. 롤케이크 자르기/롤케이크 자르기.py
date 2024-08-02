def solution(topping):
    answer = 0
    
    left = {}
    right = {}
    
    
    for to in topping:
        if to in right:
            right[to] += 1
        else:
            right[to] = 1
            
    
    for to in topping:
        if right[to] == 1:
            del right[to]
        else:
            right[to] -= 1
            
        if to in left:
            left[to] += 1
        else:
            left[to] = 1
            
        if len(left) == len(right):
            answer += 1
    
    return answer