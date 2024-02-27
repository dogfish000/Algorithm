def solution(participant, completion):
    
    dic = {}
    
    for part in participant:
        dic[part] = dic.get(part, 0) + 1
        
    for comp in completion:
        dic[comp] = dic.get(comp) - 1
    
    answer = ''
    
    for d in dic:
        if dic[d] == 1:
            answer = d
        
    
    
    return answer