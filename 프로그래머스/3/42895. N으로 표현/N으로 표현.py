import sys
sys.setrecursionlimit(1000000)

def solution(N, number):
    global answer
    answer = 987654321
    
    lst = [987654321] * 32001
    
    lst_rec = []
    tmp = N
    
    for i in range(1, 6):
        if tmp <= 32000:
            lst_rec.append([tmp, i])
            
        tmp = tmp * 10 + N
        
    if N != 1:
        tmp = 1
        for i in range(2, 7):
            if tmp <= 32000:
                lst_rec.append([tmp, i])
        
            tmp = tmp * 10 + 1
    
    
    lst[0] = 0
    
    def rec(num, cnt):
        global answer
        if cnt > 8:
            return
        
        if num == number:
            answer = min(answer, cnt)
            return
        
        if num > 32000 or num < 0:
            return
        
        if lst[num] > cnt or num == 0:
            lst[num] = cnt
        
            for tmp in lst_rec:
                root_a = num + tmp[0]
                root_b = num - tmp[0]
                root_c = num * tmp[0]
                root_d = num // tmp[0]

                rec(root_a, cnt + tmp[1])
                rec(root_b, cnt + tmp[1])
                rec(root_c, cnt + tmp[1])
                rec(root_d, cnt + tmp[1])
                
        else:
            return
                
            
    
    rec(0, 0)
    
    if answer == 987654321:
        answer = -1
    return answer