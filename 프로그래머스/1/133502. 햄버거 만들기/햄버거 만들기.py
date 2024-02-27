def solution(ingredient):
    answer = 0
    
    lst = []
    
    for i in ingredient:
        lst.append(i)
        if len(lst) >= 4:
            if chk_burger(lst):
                answer += 1
                for _ in range(4):
                    lst.pop()
                
    
    
    return answer

def chk_burger(lst):
    if lst[-1] == 1 and lst[-2] == 3 and lst[-3] == 2 and lst[-4] == 1:
        
        return True
    
    return False