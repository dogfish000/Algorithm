import sys
import math

input = sys.stdin.readline


N = int(input())

if N == 0:
    print(0)
else:
    lst = []

    for _ in range(N):
        lst.append(int(input()))

    lst.sort()
    M = round(N * 0.15 + 10 ** -8)

    lst = lst[M: N - M]

    print(round(sum(lst) / len(lst) + 10 ** -8))
