def prime_num(num):
    if num == 1:
        return False

    idx = int(num ** 0.5 + 1)

    for i in range(2, idx):
        if num % i == 0:
            return False

    return True

M, N = map(int, input().split())

for i in range(M, N + 1):
    if prime_num(i):
        print(i)
