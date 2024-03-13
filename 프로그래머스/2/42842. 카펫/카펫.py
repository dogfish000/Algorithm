def solution(brown, yellow):
    answer = []
    
    n = int((brown - 4) / 2)
    for i in range(n - 1, 0, -1):
        if i * (n - i) == yellow:
            answer = [i + 2, n - i + 2]
            break
    
    
    
    return answer