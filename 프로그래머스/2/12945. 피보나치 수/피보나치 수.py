import sys
sys.setrecursionlimit(10**6)

def solution(n):
    answer = 0
    
    answer = fibo(n) % 1234567
    return answer



def fibo(n):
    if n == 0:
        return f[0]
    if n == 1:
        return f[1]
    
    if f[n] != 0:
        return f[n]
    else:
        f[n] = fibo(n - 1) + fibo(n - 2)
        return f[n]
        

f = [0] * 100001
f[0] = 0
f[1] = 1
