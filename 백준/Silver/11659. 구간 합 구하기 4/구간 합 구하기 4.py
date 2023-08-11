import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = [0]
lst = lst + list(map(int, input().split()))

dp = [0] * (N + 1)

dp[0] = 0

for i in range(1, N + 1):
    dp[i] = dp[i - 1] + lst[i]


for _ in range(M):
    S, G = map(int, input().split())

    S = S - 1

    print(dp[G] - dp[S])

