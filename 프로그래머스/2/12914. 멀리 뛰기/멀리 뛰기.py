def solution(n):
    if n == 1:
        return 1
    answer = [0] * (n + 1)
    
    answer[1] = 1
    answer[2] = 2
    
    for i in range(3, n + 1):
        answer[i] = answer[i - 1] + answer[i - 2]
        
    
    
    
    
    return answer[n] % 1234567