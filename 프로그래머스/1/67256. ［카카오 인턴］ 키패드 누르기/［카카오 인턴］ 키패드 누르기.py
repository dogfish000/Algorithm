def solution(numbers, hand):
    answer = ''
    
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    
    location_l = [3, 0]
    location_r = [3, 2]
    
    
    dic = {}
    for i in range(len(keypad)):
        for j in range(len(keypad[0])):
            dic[keypad[i][j]] = [i, j]
    
    for n in numbers:
        if n in (1, 4, 7):
            answer += 'L'
            location_l = dic[n]
        
        elif n in (3, 6, 9):
            answer += 'R'
            location_r = dic[n]
        
        else:
            tmp = chk_hand(location_l, location_r, dic[n], hand)
            if tmp == 'right':
                answer += 'R'
                location_r = dic[n]
            else:
                answer += 'L'
                location_l = dic[n]
    
    
    
    
    
    return answer


def chk_hand(l, r, n, handed):
    
    dist_l = abs(l[0] - n[0]) + abs(l[1] - n[1])
    dist_r = abs(r[0] - n[0]) + abs(r[1] - n[1])
    
    if dist_l > dist_r:
        return 'right'
    elif dist_r > dist_l:
        return 'left'
    else:
        return handed