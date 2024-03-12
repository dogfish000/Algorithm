def solution(n):
    answer = 0
    num = n + 1
    while True:
        if bin(n).count('1') == bin(num).count('1'):
            answer = num
            break
        num += 1
    
    
    
    return answer