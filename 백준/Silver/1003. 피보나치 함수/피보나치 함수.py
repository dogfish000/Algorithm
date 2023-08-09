import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    if N == 0:
        print(1, 0)
        continue

    if N == 1:
        print(0, 1)
        continue

    lst = [0] * (N + 1)

    lst[N] = 1

    for i in range(N, 1, -1):
        lst[i - 1] += lst[i]
        lst[i - 2] += lst[i]

    print(lst[0], lst[1])
