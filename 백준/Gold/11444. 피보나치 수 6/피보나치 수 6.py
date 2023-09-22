n = int(input())
# 메모이제이션을 위한 딕셔너리
d = {}

# 모듈러 연산에 사용할 상수
mod = 1000000007

# 피보나치 수열 계산 함수
def fibo(n):
    # n이 0 이하일 때는 0 반환
    if n <= 0:
        return 0
    # n이 1 또는 2일 때는 1 반환
    elif n == 1 or n == 2:
        return 1
    # 이미 계산한 값이 메모이제이션 딕셔너리에 있는 경우 반환
    elif n in d:
        return d[n]
    else:
        # 홀수일 때
        if n % 2 == 1:
            m = (n + 1) // 2
            t1 = fibo(m)
            t2 = fibo(m - 1)
            d[n] = (t1 * t1 + t2 * t2) % mod
            return d[n]
        # 짝수일 때
        else:
            m = n // 2
            t1 = fibo(m - 1)
            t2 = fibo(m)
            d[n] = ((2 * t1 + t2) * t2) % mod
            return d[n]

print(fibo(n))