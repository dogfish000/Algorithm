import sys

N = int(input())

lst = [0]

dp = [0] * (N + 1)

for _ in range(N):
    lst.append(int(sys.stdin.readline()))
if N >= 1:
    dp[1] = lst[1]
if N >= 2:
    dp[2] = lst[1] + lst[2]
if N >= 3:
    dp[3] = max(lst[1], lst[2]) + lst[3]

    for i in range(4, N + 1):
        a = dp[i - 3] + lst[i - 1] + lst[i]
        b = dp[i - 2] + lst[i]
        dp[i] = max(a, b)

print(dp[N])
