import sys
import copy
from collections import deque

input = sys.stdin.readline


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    # print(dp)


    dp[0][0] = lst[0][0]
    dp[1][0] = lst[1][0]

    if N == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = dp[1][0] + lst[0][1]
    dp[1][1] = dp[0][0] + lst[1][1]

    if N == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    else:
        for i in range(2, N):
            dp[0][i] = max(max(dp[0][i - 2], dp[1][i - 2]), dp[1][i - 1]) + lst[0][i]
            dp[1][i] = max(max(dp[1][i - 2], dp[0][i - 2]), dp[0][i - 1]) + lst[1][i]



    print(max(dp[0][N - 1], dp[1][N - 1]))



