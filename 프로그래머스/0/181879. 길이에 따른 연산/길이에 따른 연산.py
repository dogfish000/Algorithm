def solution(num_list):
    answer = 0
    
    if len(num_list) >10:
        for num in num_list:
            answer += num
    
    else:
        answer = 1
        for num in num_list:
            answer *= num
    
    return answer