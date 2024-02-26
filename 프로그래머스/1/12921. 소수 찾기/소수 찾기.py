def solution(n):
    answer = 0
    
    for i in range(2, n + 1):
        if chk_prime(i):
            answer += 1
    
    
    return answer

def chk_prime(n_):
    for i in range(2, int(n_ ** (1/2)) + 1):
        if n_ % i == 0:
            return False
    
    return True