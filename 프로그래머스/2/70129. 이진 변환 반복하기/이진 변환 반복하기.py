def solution(s):
    answer = []
    num_zero = 0
    cnt_bin = 0
    
    while (s != '1'):
        num_zero += s.count('0')
        s = s.replace('0', '')
        tmp = len(s)
        s = bin(tmp)[2:]
    
        cnt_bin += 1
        
    answer = [cnt_bin, num_zero]
    
    return answer