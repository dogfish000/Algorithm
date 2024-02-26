def solution(N, stages):
    answer = []
    
    fail_percent = []
    
    users = len(stages)
    
    for i in range(1, N + 1):
        if users == 0:
            tmp = [i, 0]
        else:
            tmp = [i, stages.count(i) / users]
        fail_percent.append(tmp)
        users = users - stages.count(i)
        
    
    # print(fail_percent)
    fail_percent.sort(key=lambda x: -x[1])
    # print(fail_percent)
    
    for item in fail_percent:
          answer.append(item[0])
    return answer