def solution(n, t, m, p):
    answer = ''
    res = ''
    i = 0
    while len(res) < t * m:
        res += change_base(i, n)
        i += 1
    print(res)
    answer = res[p - 1::m]
    answer = answer[:t]
        
    
    return answer



def change_base(num, base):
    tmp = ''
    if num == 0:
        return '0'
    
    while num > 0:
        a = num % base
        if a >= 10:
            tmp += chr(ord('A') + a - 10)
        else:
            tmp += str(a)
        num = num // base
    
    tmp = tmp[::-1]
    return tmp