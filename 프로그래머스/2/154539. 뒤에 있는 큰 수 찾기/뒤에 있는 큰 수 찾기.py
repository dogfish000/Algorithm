
def solution(numbers):
    answer = []
    lst = []
    
    numbers.reverse()
    for num in numbers:
        is_next = False
        
        while is_next == False:
            if lst:
                a = lst.pop()
                if num < a:
                    lst.append(a)
                    answer.append(a)
                    lst.append(num)
                    is_next = True
                    
            else:
                answer.append(-1)
                lst.append(num)
                is_next = True
                
    answer.reverse()
            
        
        
        
        
    
    
    
    
    return answer