def solution(X, Y):
    answer = ''
    
    lst_x = [0 for _ in range(10)]
    lst_y = [0 for _ in range(10)]
    
    for x in X:
        lst_x[int(x)] += 1
    
    for y in Y:
        lst_y[int(y)] += 1
        
    lst = [0 for _ in range(10)]
    
    for i in range(10):
        lst[i] = min(lst_x[i], lst_y[i])
    
    print(lst)
    
    for i in range(9, -1, -1):
        
        if i == 0 and answer == '' and lst[i] != 0:
            answer = '0'
        
        else:
            answer += str(i) * lst[i]
        
            
    if answer == '':
        answer = '-1'
    return answer