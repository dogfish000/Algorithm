def solution(n,a,b):
    if a > b:
        a, b = b, a
    answer = 1

    while True:
        if b % 2 == 0 and b - a == 1:
            break
            
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        answer += 1

    return answer