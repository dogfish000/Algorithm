def solution(keymap, targets):
    answer = []
    
    for target in targets:
        cnt = 0
        for t in target:
            min_cnt = 987654321
            for key in keymap:
                if key.find(t) != -1:
                    min_cnt = min(min_cnt, key.find(t) + 1)
            if min_cnt == 987654321:
                cnt = -1
                break
            else:
                cnt += min_cnt
                
        answer.append(cnt)
                
            
            
    
    
    
    
    return answer