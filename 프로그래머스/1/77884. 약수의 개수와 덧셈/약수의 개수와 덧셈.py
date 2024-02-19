def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        answer += cnt_div(i)
        
    
    return answer


def cnt_div(num):
    temp_cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            temp_cnt += 1
    
    if temp_cnt % 2 == 0:
        return num
    else:
        return -num