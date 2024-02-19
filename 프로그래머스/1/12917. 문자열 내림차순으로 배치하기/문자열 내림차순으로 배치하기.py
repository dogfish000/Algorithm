def solution(s):
    answer = ''
    
    lst = list(s)
    lst.sort(reverse=True)
    for i in range(len(lst)):
        answer += lst[i]
    
    return answer