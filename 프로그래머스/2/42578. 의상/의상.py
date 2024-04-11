def solution(clothes):
    answer = 1
    
    dic = {}
    
    for cloth in clothes:
        dic[cloth[1]] = dic.get(cloth[1], 0) + 1
    
    for v in dic.values():
        answer *= (v + 1)
    
    answer -= 1
    
    return answer