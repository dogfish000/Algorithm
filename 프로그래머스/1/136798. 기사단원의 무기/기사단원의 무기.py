def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        tmp_cnt = cnt_div(i)
        if tmp_cnt > limit:
            answer += power
        else:
            answer += tmp_cnt
            
        
    
    
    return answer


def cnt_div(n):
    cnt = 0
    for i in range(1, int(n ** (1/2)) + 1):
        if i == n ** (1/ 2):
            cnt += 1
        else:
            if n % i == 0:
                cnt += 2
    
    return cnt