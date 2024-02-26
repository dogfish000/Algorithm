def solution(n, m, section):
    answer = 0
    
    
    while True:
        if section:
            answer += 1
            start_wall = section.pop(0)
            end_wall = start_wall + m - 1

            while True:
                if section and section[0] <= end_wall:
                    section.pop(0)
                else:
                    break
                    
        else:
            break
    
    
    return answer