def solution(s):
    answer = 0
    
    idx = 0
    cnt_x = 0
    cnt_y = 0
    
    for i in range(len(s)):
        if s[i] == s[idx]:
            cnt_x += 1
        else:
            cnt_y += 1
        
        if cnt_x == cnt_y:
            answer += 1
            idx = i + 1
            
        elif cnt_x != cnt_y and i == len(s) - 1:
            answer += 1
    
    
    
    return answer