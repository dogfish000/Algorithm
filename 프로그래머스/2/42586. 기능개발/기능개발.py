def solution(progresses, speeds):
    answer = []
    N = len(speeds)
    lst = []
    
    for i in range(N):
        a = 100 - progresses[i]
        tmp = a // speeds[i]
        if a % speeds[i] != 0:
            tmp += 1
        lst.append(tmp)
        
    print(lst)
    
    max_val = -1
    streak = 0
    
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            if i != 0:
                answer.append(streak)
            streak = 0
        
        if lst[i] <= max_val:
            streak += 1
        
    answer.append(streak)
    
    return answer