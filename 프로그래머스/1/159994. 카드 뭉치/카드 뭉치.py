def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    for g in goal:
        if cards1 and cards1[0] == g:
            cards1.remove(g)
        elif cards2 and cards2[0] == g:
            cards2.remove(g)
        else:
            answer = 'No'
            break
    
    
    return answer