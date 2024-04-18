def solution(s):
    answer = []
    
    lst = []
    s = s.replace('},{', '}{')
    n = len(s)
    
    
    for i in range(1, n - 1):
        if s[i] == '{':
            tmp_set = []
            tmp = 0
            
        else:
            if s[i] == ',':
                tmp_set.append(tmp)
                tmp = 0
            elif s[i] == '}':
                tmp_set.append(tmp)
                tmp = 0
                lst.append(tmp_set)
            else:
                tmp = tmp * 10 + int(s[i])
            
    
    lst.sort(key=lambda x: len(x))
    
    for l in lst:
        for num in l:
            if num not in answer:
                answer.append(num)
    
    
    
    return answer