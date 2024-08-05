def solution(dirs):
    answer = 0
    
    cur = [0, 0]
    route = []
    
    dirs = list(dirs)
    
    for dir in dirs:
        if dir == 'L':
            if cur[0] > -5:
                new_cur = [cur[0] -1, cur[1]]
                tmp = [new_cur, cur]
                tmp.sort()
                if tmp not in route:
                    route.append(tmp)
                
                cur = new_cur
                    
        elif dir == 'R':
            if cur[0] < 5:
                new_cur = [cur[0] + 1, cur[1]]
                tmp = [new_cur, cur]
                tmp.sort()
                if tmp not in route:
                    route.append(tmp)
                cur = new_cur
                    
        elif dir == 'U':
            if cur[1] < 5:
                new_cur = [cur[0], cur[1] + 1]
                tmp = [new_cur, cur]
                tmp.sort()
                if tmp not in route:
                    route.append(tmp)
                cur = new_cur
                    
                    
        elif dir == 'D':
            if cur[1] > -5:
                new_cur = [cur[0], cur[1] - 1]
                tmp = [new_cur, cur]
                tmp.sort()
                if tmp not in route:
                    route.append(tmp)
                cur = new_cur
        
        
                
    answer = len(route)
    
    
    return answer