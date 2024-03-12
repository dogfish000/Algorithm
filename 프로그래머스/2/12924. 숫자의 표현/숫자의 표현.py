def solution(n):
    answer = 1
    
    for i in range(1, n):
        tmp = i
        
        for j in range(i + 1, n):
            tmp += j
            if tmp == n:
                answer += 1
                print(j)
                break
            if tmp > n:
                break
    
    
    return answer