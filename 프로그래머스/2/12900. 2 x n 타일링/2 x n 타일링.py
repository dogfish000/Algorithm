def solution(n):
    answer = 0
    
    
    lst = [0, 1, 2]
    
    for i in range(3, n + 1):
        tmp = (lst[-1] + lst[-2]) % 1000000007
        lst.append(tmp)
        
    answer = lst[-1]
    
    return answer