def solution(elements):
    answer = 0
    dic = {}
    
    n = len(elements)
    
    elements = elements + elements[0: n - 1]
        
    for i in range(1, n + 1):
        for j in range(0, n):
            tmp = sum(elements[j: j + i])
            if tmp not in dic.keys():
                dic[tmp] = 1
                
    answer = len(dic)
        
        
    return answer