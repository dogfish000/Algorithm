def solution(n):
    answer = 0
    
    lst = list(map(int, str(n)))
    
    lst.sort()
    
    print(lst)
    
    for i in range(len(lst)):
        answer += 10 ** i * lst[i]
    
    return answer