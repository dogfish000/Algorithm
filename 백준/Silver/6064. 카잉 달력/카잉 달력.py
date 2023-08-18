import sys

input = sys.stdin.readline


def GCD(a, b):
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b
    else:
        c = a % b
        a, b = b, c
        return GCD(a, b)


T = int(input())

for tc in range(1, T + 1):
    M, N, x, y = map(int, input().split())

    num = int(M * N / GCD(M, N))
    answer = -1

    lst = []

    i = 0
    while True:
        tmp = i * M + x

        if tmp > num:
            break

        lst.append(tmp)
        i += 1

    for l in lst:
        a = l % N
        if a == 0:
            a = N

        if a == y:
            answer = l
            break

    print(answer)

