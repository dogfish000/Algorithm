def solution(s):
    answer = ''
    
    max_num = -987654321
    min_num = 987654321
    
    lst = list(map(int, s.split()))
    
    for l in lst:
        max_num = max(max_num, l)
        min_num = min(min_num, l)
    
    answer = str(min_num) + ' ' + str(max_num)
    
    return answer