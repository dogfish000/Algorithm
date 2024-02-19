def solution(s):
    answer = True
    
    cnt_p = 0
    cnt_y = 0
    
    lst = list(s)
    for i in range(len(lst)):
        if lst[i] == 'p' or lst[i] == 'P':
            cnt_p += 1
        if lst[i] == 'y' or lst[i] == 'Y':
            cnt_y += 1
    print(cnt_p, cnt_y)
    if cnt_p != cnt_y :
        answer = False
    
    return answer