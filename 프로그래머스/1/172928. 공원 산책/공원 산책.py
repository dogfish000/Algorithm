def solution(park, routes):
    answer = []
    
    dir = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    
    lst = []
    for p in park:
        lst.append(list(p))
    
    start_i = 0
    start_j = 0
    
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 'S':
                start_i = i
                start_j = j
    
    for route in routes:
        tmp_i, tmp_j = start_i, start_j
        is_possible = 1
        
        d, l = route.split()
        di, dj = dir[d]
        l = int(l)
        
        for _ in range(l):
            tmp_i += di
            tmp_j += dj
            if 0 > tmp_i or tmp_i >= len(lst) or tmp_j < 0 or tmp_j >= len(lst[0]) or lst[tmp_i][tmp_j] == 'X':
                is_possible = 0
                break
                
        if is_possible == 1:
            start_i, start_j = tmp_i, tmp_j
            
            
                
    answer = [start_i, start_j]    
    
    return answer