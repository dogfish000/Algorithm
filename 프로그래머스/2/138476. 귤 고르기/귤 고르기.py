def solution(k, tangerine):
    answer = 0
    dic = {}
    lst = []
    cnt = 0
    
    for t in tangerine:
        dic[t] = dic.get(t, 0) + 1
    
    for key, value in dic.items():
        lst.append([value, key])
        
        
    lst.sort(key=lambda x: -x[0])
        
    for l in lst:
        cnt += l[0]
        answer += 1
        if cnt >= k:
            break
        
        
    
    return answer