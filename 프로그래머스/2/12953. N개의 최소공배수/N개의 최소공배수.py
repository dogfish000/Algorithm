def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer = answer * arr[i] / get_gcd(answer, arr[i])
    
    return answer



def get_gcd(a, b):
    if a < b:
        a, b = b, a
    
    if a % b == 0:
        return b
    
    while a % b != 0:
        r = a % b
        a = b
        b = r
        if a % b == 0:
            return b
    

print(get_gcd(17, 4))