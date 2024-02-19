def solution(s):
    answer = False
    
    s_len = len(s)
    
    if s_len == 4 or s_len == 6:
        for word in s:
            if ord(word) > 57:
                answer = False
                break
                
            answer = True
        
    
        
    
    
    return answer