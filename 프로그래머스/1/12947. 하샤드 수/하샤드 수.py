def solution(x):
    answer = True
    a = x
    divide_number = 0
    
    while x > 0:
        divide_number += x % 10
        x = x // 10
    
    
    if a % divide_number != 0:
        answer = False
    
    return answer