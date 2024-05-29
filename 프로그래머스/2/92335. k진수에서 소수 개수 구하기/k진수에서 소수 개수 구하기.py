def solution(n, k):
    answer = 0
    
    conv_num = change_base(n, k)
    
    lst = conv_num.split('0')
    for li in lst:
        if li == '':
            continue
            
        if check_prime(int(li)):
            answer += 1
    
    
    
    
    
    return answer

def change_base (num, div):
    base = ''
    while num > 0:
        base += str(num % div)
        num = num // div
        
    base = base[::-1]
    return base

def check_prime (num):
    if num == 1:
        return False
    
    end = int(num ** (1 / 2)) + 1
    is_prime = True
    
    for i in range(2, end):
        if num % i == 0:
            is_prime = False
            break
            
    return is_prime

    